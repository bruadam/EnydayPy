# UserDetailsResponsePeriods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_begin** | **datetime** |  | [optional] 
**period_end** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.user_details_response_periods import UserDetailsResponsePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsResponsePeriods from a JSON string
user_details_response_periods_instance = UserDetailsResponsePeriods.from_json(json)
# print the JSON string representation of the object
print(UserDetailsResponsePeriods.to_json())

# convert the object into a dict
user_details_response_periods_dict = user_details_response_periods_instance.to_dict()
# create an instance of UserDetailsResponsePeriods from a dict
user_details_response_periods_from_dict = UserDetailsResponsePeriods.from_dict(user_details_response_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


