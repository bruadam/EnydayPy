# UserUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_user_body import UserUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserBody from a JSON string
user_user_body_instance = UserUserBody.from_json(json)
# print the JSON string representation of the object
print(UserUserBody.to_json())

# convert the object into a dict
user_user_body_dict = user_user_body_instance.to_dict()
# create an instance of UserUserBody from a dict
user_user_body_from_dict = UserUserBody.from_dict(user_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


