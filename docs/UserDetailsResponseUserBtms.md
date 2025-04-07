# UserDetailsResponseUserBtms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btm_id** | **int** |  | [optional] 
**btm_name** | **str** |  | [optional] 
**access_address_id** | **int** |  | [optional] 
**access_address** | **str** |  | [optional] 
**use_buildings** | **int** |  | [optional] 
**nordpool_area** | **str** |  | [optional] 
**periods** | [**List[UserDetailsResponsePeriods]**](UserDetailsResponsePeriods.md) |  | [optional] 
**new_price_model** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.user_details_response_user_btms import UserDetailsResponseUserBtms

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsResponseUserBtms from a JSON string
user_details_response_user_btms_instance = UserDetailsResponseUserBtms.from_json(json)
# print the JSON string representation of the object
print(UserDetailsResponseUserBtms.to_json())

# convert the object into a dict
user_details_response_user_btms_dict = user_details_response_user_btms_instance.to_dict()
# create an instance of UserDetailsResponseUserBtms from a dict
user_details_response_user_btms_from_dict = UserDetailsResponseUserBtms.from_dict(user_details_response_user_btms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


