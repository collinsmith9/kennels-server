import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals
from views import get_all_locations
from views import get_all_employees
from views.animal_requests import update_animal, get_single_animal, create_animal, delete_animal
from views.locations_requests import update_location, delete_location, get_single_location, create_location
from views.employees_requests import update_employee, delete_employee, get_single_employee, create_employee
from views import get_all_customers
from views.customer_requests import update_customer, delete_customer, get_single_customer, create_customer


# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError: #nothing at index
            pass
        except ValueError: #if it doesn't turn to int properly
            pass 
        return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"
            else:
                response = f"{get_all_locations()}"
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"
        elif resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"
        self.wfile.write(response.encode())
        # Your new console.log() that outputs to the terminal
        print(self.path)

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0)) # get length of what was passed
        post_body = self.rfile.read(content_len) # read file only reads to specified character (content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_resource = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            new_resource = create_animal(post_body)
        elif resource == "locations":
            new_resource = create_location(post_body)
        elif resource == "employees":
            new_resource = create_employee(post_body)
        elif resource == "customers":
            new_resource = create_customer(post_body)

        # Encode the new animal and send in response
        self.wfile.write(f"{new_resource}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
        elif resource == "locations":
            update_location(id, post_body)
        elif resource == "employees":
            update_employee(id, post_body)
        elif resource == "customers":
            update_customer(id, post_body)

    # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)
        elif resource == "locations":
            delete_location(id)
        elif resource == "employees":
            delete_employee(id)
        elif resource == "customers":
            delete_customer(id)
    # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()