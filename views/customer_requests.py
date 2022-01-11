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
    return CUSTOMERS

def get_single_customer(id):
    requested_cusotmer = None

    for customer in CUSTOMERS:
      if customer["id"] == id:
        requested_cusotmer = customer

    return requested_cusotmer

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



  