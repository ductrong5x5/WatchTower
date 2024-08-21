import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
  host=f"{os.getenv('host')}",
  user=f"{os.getenv('user')}",
  password=f"{os.getenv('password')}"
)

cursor = mydb.cursor()
cursor.execute('CREATE DATABASE IF NOT EXIST watchtower')
cursor.execute('USE watchtower')

# KEEPS ENVIRONMENT RUNNING FOR INPUT
while True:
  cursor = mydb.cursor()
  query = input()
  try:
    cursor.execute(query)
    for result in cursor:
      print(result)
  except:
    print("ERROR!")