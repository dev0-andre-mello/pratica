import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1010',
    database='primeirobanco'
)

cursor = bd.cursor()

sql_alunos = '''
CREATE TABLE IF NOT EXISTS alunos(
    id INT AUTO_INCREMENT,
    nome VARCHAR(100) UNIQUE,
    idade INT,
    PRIMARY KEY (id)
)
'''

cursor.execute(sql_alunos)

sql_notas = '''
CREATE TABLE IF NOT EXISTS notas(
    id INT AUTO_INCREMENT,
    aluno_id INT,
    disciplina VARCHAR(100),
    nota FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
'''

cursor.execute(sql_notas)

sql_insert_aluno = 'INSERT INTO alunos (nome, idade) VALUES (%s, %s)'

data = [
    ('Fernando', 20),
    ('Kelly', 22)
]

cursor.executemany(sql_insert_aluno, data)

bd.commit()

sql_insert_notas = '''
INSERT INTO notas (aluno_id, disciplina, nota)
VALUES (%s, %s, %s)
'''

data_notas = [
    (1, 'Matematica', 8.5),
    (2, 'Portugues', 9.0)
]

cursor.executemany(sql_insert_notas, data_notas)

bd.commit()

