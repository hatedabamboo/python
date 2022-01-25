#!/usr/bin/python3

import datetime
import os
import sqlite3


DATABASE = "{}/{}.db".format(os.getenv('HOME'), os.getenv('USER'))


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


def selectData()
