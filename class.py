#!/usr/bin/python3

class Book():
	name = ""
	author = ""
	type = ""
	pages = ""
	
	def description(self):
		desc = "%s is the book of %s by %s of %.0f pages" % (self.name, self.type, self.author, self.pages)
		return desc

book1 = Book()
book1.name = "programmer 101"
book1.type = "programming fundamentals"
book1.author = "Djena"
book1.pages = 512

print(book1.description())
