import psycopg2

class PGDB:
	""" Simple postgres wrapper """

	def __init__(self, database, host, user, password):
		""" """
		self.database = database
		self.host = host
		self.user = user
		self.password = password
		self.conn = None
		self.connect_to_db()

	def connect_to_db(self):
		""" """
		self.conn = psycopg2.connect (
			database = self.database,
			host	 = self.host,
			user	 = self.user,
			password = self.password
		)
		return conn # Optional

	def query(self, qu, *params):
		""" """
		cur = self.conn.cursor()
		if not qu.endswith(';'): qu += ';'

		# print(f"{cur.mogrify(qu, params)}")
		cur.execute(qu, params)

		try:
			return cur.fetchall(), 0

		except psycopg2.ProgrammingError:
			return None, 0
