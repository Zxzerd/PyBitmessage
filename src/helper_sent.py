from helper_sql import *

def insert(t):
    sqlExecute('''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', *t)
