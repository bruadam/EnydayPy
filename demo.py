# %% Import the necessary libraries
from EnydayPy import EnydayClient
from getpass import getpass
from datetime import datetime, timedelta

# %% Create an instance of the API class
username = input("Enter your Enyday email: ")
password = getpass("Enter your Enyday password: ")

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
# %% Plot the daily power consumption
import matplotlib.pyplot as plt

df_daily = Power.set_index("period_begin", inplace=True)
# %%
