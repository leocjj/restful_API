#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""

url = "http://localhost:5000/"

def print_result(r, method):
    if method == "None":
        print("RESPONSE FOR RESTFUL API MAIN PAGE.")
        print("\t {}".format(r))
        print("\t Body response:")
        print("\t\t- type: {}".format(type(r.text)))
        print("\t\t- content: {}".format(r.text))
        return
    if r:
        print("RESPONSE FOR {}".format(method))
        print("\t {}".format(r))
        print("\t Body response:")
        print("\t\t- type: {}".format(type(r.text)))
        print("\t\t- content: {}".format(r.text))
    else:
        print("\t Method not allowed.")
        print("\t Please run: python test.py <method>")
        print("\t Available Methods (uppercase): GET, POST, PUT, DELETE")

if __name__ == "__main__":
    import requests
    from sys import argv

    # https://requests.readthedocs.io/es/latest/user/quickstart.html#realizar-un-peticion

    if len(argv) <=1:
        print("\t To test individual method please run: python test.py <method>")
        print("\t Methods available (uppercase): GET, POST, PUT, DELETE")
        print()
        r = requests.get(url)
        print_result(r, "None")
        print()
        exit(0)

    r = None
    print("URL for testing: " + url)

    if  argv[1] == "GET":
        r = requests.get(url + argv[1])
        print_result(r, "GET")

    if  argv[1] == "POST":
        r = requests.post(url + argv[1])
        print_result(r, "POST")

    if  argv[1] == "PUT":
        r = requests.put(url + argv[1])
        print_result(r, "PUT")

    if  argv[1] == "DELETE":
        r = requests.delete(url + argv[1])
        print_result(r, "DELETE")

    if  argv[1] == "ALL":
        print("Testing all methods...")

        r = requests.get(url + "GET")
        print_result(r, "GET")
        print()

        r = requests.post(url + "POST")
        print_result(r, "POST")
        print()

        r = requests.put(url + "PUT")
        print_result(r, "PUT")
        print()

        r = requests.delete(url + "DELETE")
        print_result(r, "DELETE")
        print()

