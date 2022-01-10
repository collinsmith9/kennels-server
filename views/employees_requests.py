EMPLOYEES = [
    # {
    #   "id": 1,
    #   "name": "Jessica Younker",
    #   "email": "jessica@younker.com",
    #   "employee": True
    # },
    # {
    #   "id": 2,
    #   "name": "Jordan Nelson",
    #   "email": "jordan@nelson.com",
    #   "employee": True
    # },
    # {
    #   "id": 3,
    #   "name": "Zoe LeBlanc",
    #   "email": "zoe@leblanc.com",
    #   "employee": True
    # },
    # {
    #   "name": "Meg Ducharme",
    #   "email": "meg@ducharme.com",
    #   "id": 4,
    #   "employee": True
    # },
    # {
    #   "name": "Hannah Hall",
    #   "email": "hannah@hall.com",
    #   "id": 5,
    #   "employee": True
    # },
    # {
    #   "name": "Emily Lemmon",
    #   "email": "emily@lemmon.com",
    #   "id": 6,
    #   "employee": True
    # },
    # {
    #   "name": "Jordan Castelloe",
    #   "email": "jordan@castelloe.com",
    #   "id": 7,
    #   "employee": True
    # },
    # {
    #   "name": "Leah Gwin",
    #   "email": "leah@gwin.com",
    #   "id": 8,
    #   "employee": True
    # },
    # {
    #   "name": "Caitlin Stein",
    #   "email": "caitlin@stein.com",
    #   "id": 9,
    #   "employee": True
    # },
    # {
    #   "name": "Greg Korte",
    #   "email": "greg@korte.com",
    #   "id": 10,
    #   "employee": True
    # },
    # {
    #   "name": "Charisse Lambert",
    #   "email": "charisse@lambert.com",
    #   "id": 11,
    #   "employee": True
    # },
    # {
    #   "name": "Madi Peper",
    #   "email": "madi@peper.com",
    #   "id": 12,
    #   "employee": True
    # },
    # {
    #   "name": "Jenna Solis",
    #   "email": "jenna@solis.com",
    #   "id": 14,
    #   "employee": True
    # }
    {
        "name": "python collin",
        "email": "python@collin.com",
        "id": 2,
        "locationId": 1
    },
    {
        "name": "Emma Beaton", 
        "email": "emma@beaton.com",
        "id": 3,
        "locationId": 2
    }
]

def get_all_employees():
    return EMPLOYEES 

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee