from cliente.cliente_modbus import ClienteMODBUS

if __name__ == '__main__':
    c = ClienteMODBUS('localhost', 502)
    c.atendimento()