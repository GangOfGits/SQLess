# SQLess Main Library file

#A class fo using tables
class table():
    path = ''  # the location of a CSV file
    form = []  # the format of the CSV file (eg. ID, name, DoB,)
    content = [] # a 2d array, will be filled with sub arrays, each ub array is a row

    def read(p): #read in a database from the path p, poupulate the variables content, form and path


    def new(self, f, p):  #creates a new CSV file with the format row f filled in at path p
        
    
    def get(self, r, c):  # get at a value (r and c can be nubers for row and 
                          # column or some key and some feild name)


    def update(self, r, c, v):  # fill in a value v (//)


    def delete(self, r):  # remove row r (r can be a rown index ie. an int or it can be a key)


    def insert(self, row_conntent):  # add a new row to bottom of the table, content in list form


    def query(self, cond = '', form_opts):  # SQL style queries with this table (ie. no FROM
                                            # key word), eg:
                                            # table.query(" SELECT ID WHERE name = '%c' " , username)


    def save(self, p = path):  # save the current table at the path p 

    
    
