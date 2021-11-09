import mysql.connector
from mysql.connector import Error

class DataBase:
	def __init__(self, host_name, user_name, user_password, db_name):
		self.host_name = host_name
		self.user_name = user_name
		self.user_password = user_password
		self.db_name = db_name
		self.connection = self.CreateConnection()
	

	def CreateConnection(self,):
		connection = None
		try:
			connection = mysql.connector.connect(
				host = self.host_name,
				user = self.user_name,
				passwd = self.user_password,
				database = self.db_name
			)
			print("Connection to MySQL DB successful")
		except Error as e:
			print(f"The error '{e}' occurred")

		return connection


	def GetCursor(self):
		try:
			cursor = self.connection.cursor()
			return cursor
		except Error as e:
			print("ERRRROR!!!")
			print(f"The error '{e}' occurred")
			if (e.errno == -1):
				connection = self.CreateConnection()
				if (connection):
					self.connection = connection


	def CreateDatabase(self, db_name):
		query = "CREATE DATABASE " + db_name
		cursor = self.GetCursor()
		try:
			cursor.execute(query)
			print("Database created successfully")
		except Error as e:
			print(f"The error '{e}' occurred")


	def ExecuteQuery(self, query):
		cursor = self.GetCursor()
		try:
			cursor.execute(query)
			self.connection.commit()
			print("Query(E) executed successfully")
		except Error as e:
			print(f"The error '{e}' occurred")


	def ExecuteManyQuery(self, query, data):
		cursor = self.GetCursor()
		try:
			cursor.executemany(query, data)
			self.connection.commit()
			print("Query(EM) executed successfully")
		except Error as e:
			print(f"The error '{e}' occurred")


	def ExecuteReadQuery(self, query):
		cursor = self.GetCursor()
		result = None
		try:
			cursor.execute(query)
			result = cursor.fetchall()
			return result
		except Error as e:
			print(f"The error '{e}' occurred")
	

	#def AddComments(self, comments):
	#	NewComments = []
	#	for comment in comments:
	#		NewFields = []
	#		for field in comment:
	#			NewFields.append(str(field))
	#		NewComments.append(NewFields)
	#	create_comments = """
	#		INSERT INTO  `comments`
	#		(`user_id`, `text`, `toxic`) 
	#		VALUES ( %s, %s, %s )
	#	"""
	#	self.ExecuteManyQuery(create_comments, NewComments) 
	#
	#
	#def DelComment(self, id):
	#	delete_comment = f"DELETE FROM comments WHERE id='{id}'"
	#	self.ExecuteQuery(delete_comment)

	def AddTableElement(self, tableName, colNames, data):
		columns = ", ".join(list(map(lambda name : "`" + str(name) 		 + "`", colNames)))
		values  = ", ".join(list(map(lambda name : "'" + str(data[name]) + "'", colNames)))
		print(columns)
		print(values)
		self.ExecuteQuery(f"INSERT INTO `{tableName}` ( {columns} ) VALUES ( {values} )")


	def GetTableElements(self, tableName, where = None, start = -1, count = 65536):
		select_elements = f"SELECT * FROM {tableName} " +(f"WHERE {where} " if where != None else "")  + "LIMIT " + (f"{start}, " if start >= 0 else "") + f"{count}"
		print(select_elements)
		return self.ExecuteReadQuery(select_elements)
	

	def GetTableSize(self, tableName):
		select_comments = f"SELECT COUNT(*) FROM {tableName}"
		return self.ExecuteReadQuery(select_comments)[0][0]


	def GetTableElementsNames(self, tableName):
		return self.ExecuteReadQuery("DESCRIBE " + tableName)


	def GetTableJson(self, tableName, where = None, start = -1, count = 65536):
		DBData = self.GetTableElements(tableName, where = where, start = start, count = count)
		DBColData = self.GetTableElementsNames(tableName)
		result = []
		for data in DBData:
			line = {}
			for field, name in zip(data, DBColData):
				line.update({name[0] : field})
			result.append(line)
		return result