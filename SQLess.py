# SQLess Main Library file
from json import loads, dumps

class Database(object):

    def __init__(self, dbfile):
        with open(dbfile, "r") as file:
            file = file.read()
            self.jsondata = loads(file)
            print(self.jsondata)

#A class fo using tables
class Table(object):
    path = ''  # the location of a CSV file
    form = []  # the format of the CSV file (eg. ID, name, DoB,)
    content = [] # a 2d array, will be filled with sub arrays, each ub array is a row

    def read_table(self, p): # read in a database from the path p, poupulate the variables content, form and path
        try:
            with open(p, 'r') as f:  # read in the content of a CSV file
                stream = f.read()
        except FileNotFoundError as E:
            raise FileNotFoundError('No such path: {}'.format(p))
           
        stream = stream.strip('\n').split('\n')  # split the file by line, after removing trailing whitespace
        
        self.form = stream[0].split(',')  # split the first line by comma and add into the form variable

        for i in range(len(self.form)):  # remove white space from the feild headings
            self.form[i] = self.form[i].strip(' ')

        stream = stream[1:]  # remove the format string from the string

        for i in range(len(stream)):  # for each row in string, split by commas and append to content
            self.content.append(stream[i].split(','))



    def new(self, f, p):  # creates a new CSV file with the format row f filled in at path p
        pass
    
    def get(self, r, c):  # get at a value (r and c can be nubers for row and 
                          # column or some key and some feild name)
        pass

    def update(self, r, c, v):  # fill in a value v (//)
        pass

    def delete(self, r):  # remove row r (r can be a rown index ie. an int or it can be a key)
        pass

    def insert(self, row_conntent):  # add a new row to bottom of the table, content in list form
        pass

    def query(self, form_opts, cond = ''):  # SQL style queries with this table (ie. no FROM
        pass                                # key word), eg:
                                            # table.query(" SELECT ID WHERE name = '%c' " , username)


    def save(self, p = path):  # save the current table at the path p 
        pass

Database("database.json")
    
##    
##t = table()
##t.read_table('test.txt')
##print(t.form)
##for i in t.content:
##    print(i)
