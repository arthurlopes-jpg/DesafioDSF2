from pymodbus.client import ModbusTcpClient

class ClienteMODBUS():
    """Classe responsável apenas pela comunicação Modbus. Sem prints ou inputs."""
    def __init__(self, server_ip, porta):
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)

    def conectar(self):
        return self._cliente.connect()

    def desconectar(self):
        self._cliente.close()

    def ler_holding_registers(self, addr, count=1):
        resp = self._cliente.read_holding_registers(address=addr, count=count, device_id=1)
        if resp and not resp.isError():
            return resp.registers
        return None

    def escrever_holding_register(self, addr, valor):
        resp = self._cliente.write_register(address=addr, value=valor, device_id=1)
        return bool(resp and not resp.isError())

    # 3.1 Leitura e escrita de float

    def ler_float(self, addr):
        """Lê 2 registradores consecutivos e converte para float32."""
        regs = self.ler_holding_registers(addr, count=2)
        if regs:
            return self._cliente.convert_from_registers(regs, self._cliente.DATATYPE.FLOAT32)
        return None

    def escreve_float(self, addr, valor_float):
        """Converte float32 para 2 registradores e escreve."""
        regs = self._cliente.convert_to_registers(valor_float, self._cliente.DATATYPE.FLOAT32)
        resp = self._cliente.write_registers(address=addr, values=regs, device_id=1)
        return bool(resp and not resp.isError())
    
    # 3.2 Leitura dos bits do registrador

    def ler_bits(self, addr):
        """Lê um registrador e retorna uma lista com o estado dos 16 bits (0 a 15)."""
        regs = self.ler_holding_registers(addr, count=1)
        if regs:
            valor = regs[0]  # Extrai cada bit usando deslocamento (shift) e máscara lógica AND
            return [(valor >> i) & 1 for i in range(16)]
        return None
    
    # 3.3 Escrita de um bit individual

    def escreve_bit(self, addr, bit_index, valor_bit):
        """Altera um bit específico para 0 ou 1, preservando os restantes."""
        if not (0 <= bit_index <= 15):
            return False
            
        # Sequência: Leitura, alteração com máscara e escrita
        regs = self.ler_holding_registers(addr, count=1)
        if regs:
            valor = regs[0]
            if valor_bit == 1:
                valor = valor | (1 << bit_index)  # Aplica máscara OR para colocar a 1
            else:
                valor = valor & ~(1 << bit_index) # Aplica máscara AND invertida para colocar a 0
            
            # Escreve o novo valor no registrador
            return self.escrever_holding_register(addr, valor)
        return False