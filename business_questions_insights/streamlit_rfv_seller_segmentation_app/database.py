import psycopg2


class PostegreSQL:
    def __init__(self, host="localhost", user="postgres", password="********", database="postgres"):
        self.conn = psycopg2.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return [table for table in self.cursor.fetchall()]

    def columns(self, table_name):
        self.cursor.execute(F"""SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'""")
        return [table[0] for table in self.cursor.fetchall()]

    def tables(self):
        self.cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
        return [table for table in self.cursor.fetchall()]

    def rollback(self):
        self.cursor.execute("ROLLBACK;")