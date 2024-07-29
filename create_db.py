"""
Team members: 
Joelle Waugh, Manuel Manrique Lopez, Ricardo Rubin, Sadia Shoily.

Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import sqlite3
import os
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    people_table_query = """
    CREATE TABLE IF NOT EXISTS people
    (
        id              INTEGER PRIMARY KEY,
        name            TEXT NOT NULL,
        email           TEXT NOT NULL,
        address         TEXT NOT NULL,
        city            TEXT NOT NULL,
        age             INTEGER,
        created_at      DATETIME NOT NULL,
        updated_at      DATETIME NOT NULL
    );
"""
    cur.execute(people_table_query)
    con.commit()
    con.close()

    # Hint: See example code in lab instructions entitled "Creating a Table"
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    fake = Faker('en_CA')

    add_ppl_query = """
        INSERT INTO people
        (
            name,
            email,
            address,
            city,
            age,
            created_at,
            updated_at
        )
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """
    
    for _ in range (200):
        new_fperson = (
            fake.name(),
            fake.email(),
            fake.address(),
            fake.city(),
            fake.random_int(18, 99),
            datetime.now().strftime('%Y-%M-%D %H:%M:%S'),
            datetime.now().strftime('%Y-%M-%D %H:%M:%S')
        )
    
        cur.execute(add_ppl_query, new_fperson)
    con.commit()
    con.close()

    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    return

if __name__ == '__main__':
   main()

