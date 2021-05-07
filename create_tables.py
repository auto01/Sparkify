import psycopg2
from sql_queries import create_query_list,drop_query_list


def create_database():
	try:
		conn=psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
		cur=conn.cursor()
		conn.set_session(autocommit=True)
		cur.execute("drop database if exists sparkifydb")
		cur.execute("create database sparkifydb with encoding 'utf8' template template0")
		conn.close()

	except psycopg2.Error as e:
		print("Error..")
		print(e)
	try:
                conn=psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
                cur=conn.cursor()
                conn.set_session(autocommit=True)
                
	except psycopg2.Error as e:
                print("Error: sparkify conn")
                print(e)
       
	return conn,cur

def create_tables(conn,cur):
	try:
		for query in create_query_list:
			cur.execute(query)
	except psycopg2.Error as e:
		print("Error:...")
		print(e)

def drop_tables(conn,cur):
	try:
                for query in drop_query_list:
                        cur.execute(query)
	except psycopg2.Error as e:
		print("Error:...")
		print(e)	


def main():
	conn,cur=create_database()
	drop_tables(conn,cur)
	create_tables(conn,cur)
	conn.close()
if __name__== '__main__':
	main()
	
