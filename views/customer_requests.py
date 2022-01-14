import sqlite3
import json
from models import Customer



CUSTOMERS = [
    {
      "id": 15,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com"
    },
    {
      "id": 16,
      "name": "Emma Beaton",
      "email": "emma@beaton.com"    
    },
    {
      "id": 17,
      "name": "Dani Adkins",
      "email": "dani.adkins.com"    
    },
    {
      "id": 18,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com"    
    },
    {
      "id": 19,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com"    
    },
    {
      "id": 20,
      "name": "Angela Lee",
      "email": "lee@lee.com"    
    },
    {
      "name": "mike mike",
      "email": "m@m.com",
      "id": 21
    },
    {
      "name": "collin smith",
      "email": "collin@email.com",
      "id": 23
    },
    {
      "name": "unknown notFound",
      "email": "unknown@notfound",
      "id": 24
    }
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor() #variable that's returned is what's used to write things to database

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email
        FROM Customer c
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row['email'])

            customers.append(customer.__dict__) #python __ is dunder
    #json.dumps needs whatever is passed to be a dictionary
    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email
        FROM Customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data['name'], data['email'])

        return json.dumps(customer.__dict__)


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)



def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Store the current index.
            customer_index = index

    # If the animal was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            new_customer["id"] = id
            CUSTOMERS[index] = new_customer
            break



  