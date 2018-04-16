# Code to Initialize new versions of the test database
# Because I'm freggin' lazy and tired of messing up

import sqlite3

# Name of the database to be created.
# (We are using data.db instead to do analysis, but test.db is the name of the empty database)
conn = sqlite3.connect('data.db')
c = conn.cursor()

create_description = ''' CREATE TABLE IF NOT EXISTS description (
                        name      TEXT    NOT NULL,
                        target    TEXT    NOT NULL,
                        info      TEXT    NOT NULL,
                        IDnum     INT     PRIMARY KEY
                        );'''

create_granularity = ''' CREATE TABLE IF NOT EXISTS granularity (
                        first       DATETIME    NOT NULL,
                        last        DATETIME    NOT NULL,
                        type        TEXT        NOT NULL,
                        itemNum     INT         NOT NULL,
                        IDnum       INT         PRIMARY KEY
                        );'''

create_privacy = ''' CREATE TABLE IF NOT EXISTS privacy (
                        user        TEXT    NOT NULL,
                        setting     TEXT    NOT NULL,
                        IDnum       INT     PRIMARY KEY
                        );'''

create_tags = ''' CREATE TABLE IF NOT EXISTS tags (
                        tag1    TEXT    NOT NULL,
                        tag2    TEXT    NOT NULL,
                        tag3    TEXT    NOT NULL,
                        tag4    TEXT    NOT NULL,
                        IDnum   INT     PRIMARY KEY
                        );'''

c.execute(create_description)
c.execute(create_granularity)
c.execute(create_privacy)
c.execute(create_tags)

conn.close()