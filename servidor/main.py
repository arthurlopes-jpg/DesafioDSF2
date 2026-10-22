from servidor.servidor_modbus import ServidorMODBUS

if __name__ == '__main__':
    s = ServidorMODBUS('localhost', 502)
    s.run()