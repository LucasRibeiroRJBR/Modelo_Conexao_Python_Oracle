import cx_Oracle, os

try:
    connection = cx_Oracle.connect(
        user='PY',
        password='123456',
        dsn='localhost:1521/XE',
        encoding='UTF-8'
    )
    print(connection.version)

    while True:
        id = input('\nDigite o ID do aluno (0 para sair) -> ')
        os.system('cls')

        if id == '0':
            break
        else:
            pass

        c = connection.cursor()
        rows = c.execute(f'SELECT * FROM XPTO.STUDENTS WHERE ID = {id}').fetchall()

        print(f'+{"-"*3}+{"-"*50}+{"-"*80}+')
        print(f'|{"ID":^3}|{"NOME":^50}|{"E-MAIL":^80}|')
        print(f'|{"-"*3}+{"-"*50}+{"-"*80}|')
        print(f'|{rows[0][0]:^3}|{rows[0][1]:^50}|{rows[0][2]:^80}|')
        print(f'+{"-"*3}+{"-"*50}+{"-"*80}+')

except:
    pass

