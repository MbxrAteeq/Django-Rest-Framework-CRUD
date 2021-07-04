import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"


# retriving data from api (If id will be given only id related data will show otherwise all data will show)
# READ Operaton
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)
# Calling the get_data function to retrieve data
#get_data()



# Create Operation
# TO write data in database
def post_data():
    data = {
        'name':'atif',
        'roll':'206',
        'city':'Islamabad',
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    data = r.json()
    print(data)
# Calling Post data function
#post_data()



# Update operation
# Update database with new data from 3rd party app
def update_data():
    data = {
        'id' : 3,
        'name':'Rizwan',
        'roll':'109',
        'city':'gadyala',
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)
# Calling Post data function
update_data()



def delete_data():
    
    data = {'id' : 14}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)
# Calling Post data function
# delete_data()


