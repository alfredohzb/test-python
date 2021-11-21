import json

class filterData:
	def __init__(self): 
		self._inputHeight = 0

	@property
	def inputHeight(self): 
		return self._inputHeight
      
	@inputHeight.setter 
	def inputHeight(self, inputUser): 
			self._inputHeight = inputUser

	def get_height_inches(self,user):
		return user.get('h_in')

	def filter(self,usersData):
		return [print("-",data['first_name'],data['last_name']) for data in usersData if data['h_in'] == self.inputHeight]

	def getResults(self):
		#Load the file
		f = open('playerlist.txt',)
		data = json.load(f)
		#Select just the values
		users = data["values"]
		#Sort the Array of values
		users.sort(key=self.get_height_inches)
		result = self.filter(users)
		if not result:
			return "No matches found"
		f.close()

if __name__ == '__main__':
	filter = filterData()
	filter.inputHeight = input("Which height are looking for: ")
	filter.getResults()