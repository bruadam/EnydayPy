# AddressResponseSubmeters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submeter_id** | **int** |  | [optional] 
**submeter_external_id** | **str** |  | [optional] 
**submeter_name** | **str** |  | [optional] 
**submeter_direction** | **int** |  | [optional] 
**submeter_box_id** | **int** |  | [optional] 
**submeter_box_external_id** | **str** |  | [optional] 
**submeter_box_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.address_response_submeters import AddressResponseSubmeters

# TODO update the JSON string below
json = "{}"
# create an instance of AddressResponseSubmeters from a JSON string
address_response_submeters_instance = AddressResponseSubmeters.from_json(json)
# print the JSON string representation of the object
print(AddressResponseSubmeters.to_json())

# convert the object into a dict
address_response_submeters_dict = address_response_submeters_instance.to_dict()
# create an instance of AddressResponseSubmeters from a dict
address_response_submeters_from_dict = AddressResponseSubmeters.from_dict(address_response_submeters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


