from __future__ import print_function
import sys
import pprint 
import collections
pp = pprint.PrettyPrinter(indent=2)
if sys.version_info < (3, 0):
    input = raw_input

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("This is {0}.".format(self.name))
        inputText="Select the queries and type according to left side of option queries displayed below \n 1) d - display the items in the warehouse , \n 2) a  - add an item to the warehouse \n 3) sy,year1,year2  - setting the book according to publication year \n 4) si,ISBN - subsets of books stored in the specified ISBN \n 5) ol,ISBN - status of all books with a specified ISBN to on loan \n 6) nl-  status of all books with a specified ISBN to not on loan.\n "
        item = input(inputText).strip()
        if item=='d':
            print("The warehouse contains:", warehouse.list_contents())
        if item == 'a' :
            self.addStore(warehouse)
        if item == "si":
            self.localqueryisbn(warehouse)
        if item == "sy":
            self.retrievebookYear(warehouse)
        if item == "ol":
            self.onloanStatus(warehouse)
        if item =="nl":
            self.noloanStatus(warehouse)
              
        print("Thank you, come again! \n")

    def addStore(self, warehouse):
        additem = input("Add an item to the warehouse, Enter the input in the form of , a,author,ISBN,title,year :\n").strip()
        if additem:
            warehouse.store(self.name, additem)
            print("The warehouse contains:", convert(warehouse.list_contents()))
            print("\n")

    def retrievebookYear(self, warehouse):
        retrieveBook = input("Retreiving the book according according to published data, Enter the input in the form of, sy,year1,year2 :\n").strip()
        if retrieveBook:
            print("The book names that is published", convert(warehouse.retrieveBookYOP(self.name, retrieveBook)))
	
    def localqueryisbn(self,warehouse):
        inputISBN = input("Retreiving the book according according to ISBN, Enter the input in the form of, si,ISBN :\n").strip()
        if inputISBN:
            print("The book Names with same ISBN ", convert(warehouse.queryisbn(self.name, inputISBN)))
            print ("\n")

    def onloanStatus(self,warehouse):
        olinformation = input("Set the status of all books with a specified ISBN to on loan, Enter the input in the form of, ol,ISBN  :\n").strip()
        if olinformation:
            print("The current book is said to be on loan")
            pp.pprint(convert(warehouse.onLoan(self.name, olinformation)))

    def noloanStatus(self,warehouse):
        nlinformation = input("Set the status of all books with a specified ISBN to on loan, Enter the input in the form of, ol,ISBN  :\n").strip()
        if nlinformation:
            print("The current book is said to be on loan")
            pp.pprint(convert(warehouse.noLoan(self.name, nlinformation)))
            


