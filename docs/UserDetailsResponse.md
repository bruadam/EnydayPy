# UserDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**last_changed_password** | **str** |  | [optional] 
**complete_profile** | **str** |  | [optional] 
**has_user_registered_his_devices** | **bool** |  | [optional] 
**nr_of_devices** | **int** |  | [optional] 
**roles** | [**List[UserDetailsResponseRoles]**](UserDetailsResponseRoles.md) |  | [optional] 
**eloverblik_customer_key** | **str** |  | [optional] 
**user_btms** | [**List[UserDetailsResponseUserBtms]**](UserDetailsResponseUserBtms.md) |  | [optional] 
**admin_btms** | **List[object]** |  | [optional] 
**reg_date** | **str** |  | [optional] 
**post_number** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**has_battery** | **bool** |  | [optional] 
**has_ev** | **bool** |  | [optional] 
**subscription** | **bool** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**is_bot** | **bool** |  | [optional] 
**address_id** | **int** |  | [optional] 
**submeter_id** | **int** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**expo_push_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_details_response import UserDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsResponse from a JSON string
user_details_response_instance = UserDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(UserDetailsResponse.to_json())

# convert the object into a dict
user_details_response_dict = user_details_response_instance.to_dict()
# create an instance of UserDetailsResponse from a dict
user_details_response_from_dict = UserDetailsResponse.from_dict(user_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


