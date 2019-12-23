#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

#c.execute("DROP TABLE testTable")

########## CREATE TABLE ########################
c.execute("""CREATE TABLE testTable (
            name TEXT CHECK(TYPEOF(name) = 'text'),
            surname TEXT CHECK(TYPEOF(surname) = 'text'),
            age INTEGER CHECK(TYPEOF(age) = 'integer'),
            phoneNumber TEXT CHECK(TYPEOF(phoneNumber) = 'text')
            )""")

########## INVALID DATA TYPE VARIABLE (Integer)
phoneNumber = 666666666

########## INSERT #############################
try:
    c.execute("INSERT INTO testTable VALUES('Janina','Kowalska',30,'111111111')")
    c.execute("INSERT INTO testTable VALUES('Jan','Kowalski',33,'000000000')")
    print('Insert: Success')
except sqlite3.Error as e:
    print('ErrorHandle: '+str(e))

########### UPDATE ############################
try:
    c.execute("UPDATE testTable SET surname = 'Nowak' where name = 'Janina'")
    print('Update: Success')
except sqlite3.Error as e:
    print('ErrorHandle: '+str(e))

########## INSERT INVALID DATA TYPE ###########
try:
    c.execute("INSERT INTO testTable (name,surname,phoneNumber) VALUES('Józef','Nowak',?)",(phoneNumber,))
except sqlite3.Error as e:
    print('ErrorHandler: '+str(e))

c.execute("SELECT * FROM testTable")

print('QueryResult: '+str(c.fetchall()))

conn.commit()
conn.close
