##
- Arthur Ferreira 

## Execução
O sistema simula uma bancada de bombeamento (IP: `localhost`, Porta: `502`).
1. Inicie o servidor: `python servidor/main.py`
2. Num segundo terminal, inicie o cliente para ver as demonstrações: `python cliente/clientemodbus.py`

## Configurações e Convenções
- **Ordem de palavras (Float):** Big-Endian (Word Order / Byte Order padrão do struct `>f` e DATATYPE.FLOAT32).
- **Comportamento da simulação:** O servidor atualiza continuamente as medições com pequenas flutuações. A vazão (FIT01) apenas se aproxima do setpoint (SP_PID) se o motor estiver habilitado (Bit 6 do end. 1328 ativo). Quando desabilitado, a vazão decai até zero.

## Mapa de Dados (não mudados)
| Tag | Descrição | Tipo | Endereço | Qtd Regs | Bit | Div | Mult. | Unidade |
|---|---|---|---|---|---|---|---|---|
| bc.temp_r | Temperatura R | FP | 700-701 | - | 10 | 0.1 | °C |
| bc.temp_s | Temperatura S | FP | 702-703 | - | 10 | 0.1 | °C |
| bc.temp_t | Temperatura T | FP | 704-705 | - | 10 | 0.1 | °C |
| bc.temp_carc| Temperatura Carcaça| FP | 706-707 | - | 10 | 0.1 | °C |
| bc.pit01 | Pressão | FP | 710-711 | - | 1 | 1 | bar |
| bc.fit01 | Vazão | FP | 712-713 | - | 1 | 1 | L/s |
| bc.sp_pid | Setpoint de Vazão | FP | 1302-1303| - | 1 | 1 | L/s |
| bc.frequencia| Frequência | INT | 830 | 1 | - | 100 | 0.01 | Hz |
| bc.corrente_r| Corrente R | INT | 840 | 1 | - | 10 | 0.1 | A |
| bc.tensao_rs | Tensão R-S | INT | 847 | 1 | - | 10 | 0.1 | V |
| bc.fp_r | Fator de Potência R| INT | 868 | 1 | - | 1000| 0.001 | - |
| bc.habilita | Habilitar Motor | INT | 1328 | 1 | 6 | 1 | 1 | - | 