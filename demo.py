# %% Import the necessary libraries
from EnydayPy import EnydayClient
from getpass import getpass
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# %% Load environment variables from .env file
load_dotenv()

def get_variable(variable_name):
    """
    Get the value of a variable from the environment or return the default value.
    """
    if variable_name in os.environ:
        return os.environ[variable_name]
    else:
        if "PASSWORD" in variable_name:
            # If the variable is a password, prompt for it
            input_value = getpass(f"Enter the value for {variable_name}: ")
        else:
            # If the variable is not a password, prompt for it
            input_value = input(f"Enter the value for {variable_name}: ")
        
        # Set the environment variable for future use
        # This is optional, you can choose to store it or not
        os.environ[variable_name] = input_value
        return input_value
        

# %% Create an instance of the API class
username = get_variable("ENYDAY_USERNAME")
password = get_variable("ENYDAY_PASSWORD")

client = EnydayClient()
client.connect(username, password)

# %% Get the user details
User = client.get_user_details()
User
# %% Get the addresses
Addresses = client.get_address_by_user_id(User.id).addresses
Addresses

# %% Get the Eloverblik authorizations
Eloverblik = client.get_eloverblik_authorization(User.id)
Eloverblik

# %% Get the power consumption
import pytz

begin = datetime(2024, 6, 1, 0, 0, 0)
end = datetime.now()

# Set the timezone to Europe/Copenhagen
begin = pytz.timezone("Europe/Copenhagen").localize(begin)
end = pytz.timezone("Europe/Copenhagen").localize(end)

# Convert datetime from Europe/Copenhagen to UTC
begin = begin.astimezone(pytz.utc)
end = end.astimezone(pytz.utc)

print(f"Begin: {begin}")
print(f"End: {end}")

Power = client.get_power_consumption_by_user_and_address_ids(
    User.id, 
    Addresses[0].id, 
    begin, 
    end, 
    as_dataframe=True
    )
# Print the sum of the power consumption
print(f"Power from PV: {Power['power_internal'].sum()}")
print(f"Power from grid: {Power['power_external'].sum()}")