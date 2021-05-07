import psycopg2
from sql_queries import select_tables_head

def db_connect():
	try:
		conn=psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
		cur=conn.cursor()
		#return conn,cur
	except psycopg2.Error as e:
		print("Error: failed to connect sparkify")
		print(e)
	return conn,cur

def test_tables_heads(conn,cur):
	try:
		for query in select_tables_head:
			print("query:",query)
			cur.execute(query)
			row=cur.fetchone()
			while row:
				print(row)
				row=cur.fetchone()
		cur.close()
	except psycopg2.Error as e:
		print(e)

def main():
	conn,cur=db_connect()
	test_tables_heads(conn,cur)
	conn.close()
if __name__=='__main__':
	main()
