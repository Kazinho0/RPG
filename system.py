import mysql.connector
from mysql.connector import Error
from datetime import date, datetime

class database:
    def __init__ (self):
        try:
            self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',         
        password='teste12',    
        database='rpg',
        port=8000
        )
            
            if self.conexao.is_connected():
                self.cursor = self.conexao.cursor()
            
        except Error as erro:
            print(f"Conexão invalida, motivo: {erro}")
        
        finally:
            if 'conexao' in locals() and self.conexao.is_connected():
                self.cursor.close()
                self.conexao.close()
  
    def create_account(self, email: str,password: str, name: str):
        creationDate = date.today()
        self.cursor.execute("INSERT INTO users (email, password, name, creationDate) VALUES (%s,%s,%s,%s)", (email, password, name, creationDate))
        self.cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = self.cursor.fetchall()
        print(user)

        if user: 
            print("Usuario criado!")
        else:
            print("Falha na criação do usuario.")
    
    def close(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            #print("Conexão com o banco encerrada.")