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
		return self.conn # Optional

	def query(self, qu, *params):
		""" """
		def query_(qu_, *params_):
			cur = self.conn.cursor()
			if not qu_.endswith(';'): qu_ += ';'

			# print(f"{cur.mogrify(qu_, params_)}").replace(b'\t', b' ').replace(b'\n', b' ').strip()
			cur.execute(qu_, params_)

			try:
				return cur.fetchall(), 0
			except psycopg2.ProgrammingError:
				# Ignore this error code if you know you've executed
				# a query that returns nothing (fetchall() will fail here)
				return None, 1

			finally:
				try:
					self.conn.commit()
				except Exception as ex:
					# print(f"Warning :: error thrown on commit: {ex}")
					pass

		try:
			return query_(qu, *params)
		except (psycopg2.OperationalError, psycopg2.InterfaceError):
			# print(f"Restarting database connection...")
			self.connect_to_db()
			return query_(qu, *params)
