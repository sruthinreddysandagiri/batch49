import psycopg2
con = psycopg2.connect(host="localhost",user="postgres", password="sRu#1993 ", port=5432, database="batch49")
cur= con.cursor()
cur.executed
