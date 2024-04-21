# Devices-Price-Classification-System-using-Python-and-Django
Devices Price Classification System (AI System) using Python and linked with Django
Mainly the system include two small projects:
* Python project: will allow you to predict the prices, allowing the sellers to classify the device's prices according to their characteristics
* Django project: Will contain a simple entity, and a few endpoints, to call the service from the Python project for a bunch of test cases, and store them.
EndPoints: 
* POST /api/devices/: Retrieve a list of all devices
* GET /api/devices/{id}: Retrieve details of a specific device by ID.
* POST /api/devices: Add a new device.
* POST /api/predict/{deviceId}

# How to run : 
Go to django side and type the following command 
``` CMD
python manage.py runserver
```

Then four endpoints can be accessed : 
1. Adding a new device
2. Getting a list of all the devices
3. Getting a device from id
4. Predict the device price range based on the id

For more details check postman `Device Price.postman_collection.json` file 
