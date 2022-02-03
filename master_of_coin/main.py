#!/usr/bin/python3

# Written with passion by @hatedabamboo

import datetime
import os
import sqlite3


DATABASE = "{}/{}.db".format(os.getenv('HOME'), os.getenv('USER'))
CONFFIG = "{}/{}.conf".format(os.getenv('HOME'), os.getenv('USER'))


def parseParams():
    """
    TODO:
    Function to read default parameters from some json file (samename as database).
    At some point in future i should make function to remember user's choice for
    those parameters. If exists in json, than use them in queries (currencty for
    example). If not, use some default value.
    """


def checkDatabase(path):
    if os.path.exists(path):
        print('Database {} exists and will be used'.format(path))
    else:
        print('New database will be created')


def createDatabase():
    checkDatabase(DATABASE)
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    print('Connected to database {}'.format(DATABASE))
    query = """CREATE TABLE spendings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            sum REAL NOT NULL,
            currency TEXT NOT NULL,
            comment TEXT
        );"""
    try:
        cur.execute(query)
        conn.commit()
        print('Table spendings created')
    except sqlite3.ProgrammingError:
        print('Error while executing CREATE TABLE query')
    conn.close()


def insertData(input_data):
    if len(input_data) < 5:
        print('Not enough values to insert: {}'.format(len(input_data)))
        return
    query = """INSER INTO spendings (date, category, sum, currency, comment)
            VALUES (?, ?, ?, ?, ?);"""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    try:
        cur.execute(query, input_data)
        conn.commit()
    except sqlite3.ProgrammingError:
        print('Error while executing INSERT query')
    conn.close()


# Select some data with ‘key’ as main query parameter and ‘value‘ as search string
def selectData(key, value):
    dates = ['day', 'month', 'year']
    if key in dates:
        date = str(value) + '%'
        query = 'SELECT SUM(sum) FROM spendings WHERE date like ?'
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        try:
            cur.execute(query, (date,))
        except sqlite3.ProgrammingError:
            print('Error while executing SELECT query with date parameter')
    elif key == 'category':
        category = value
        query = 'SELECT SUM(sum) FROM spendings WHERE category = ?'
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        try:
            cur.execute(query, (category,))
        except sqlite3.ProgrammingError:
            print('Error while executing SELECT query with category parameter')

