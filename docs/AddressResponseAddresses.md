# AddressResponseAddresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**access_address_id** | **int** |  | [optional] 
**external_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**floor** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**is_virtual** | **int** |  | [optional] 
**door_number** | **int** |  | [optional] 
**total_doors_on_floor** | **int** |  | [optional] 
**building_id** | **int** |  | [optional] 
**btm_id** | **int** |  | [optional] 
**submeters** | [**List[AddressResponseSubmeters]**](AddressResponseSubmeters.md) |  | [optional] 

## Example

```python
from openapi_client.models.address_response_addresses import AddressResponseAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of AddressResponseAddresses from a JSON string
address_response_addresses_instance = AddressResponseAddresses.from_json(json)
# print the JSON string representation of the object
print(AddressResponseAddresses.to_json())

# convert the object into a dict
address_response_addresses_dict = address_response_addresses_instance.to_dict()
# create an instance of AddressResponseAddresses from a dict
address_response_addresses_from_dict = AddressResponseAddresses.from_dict(address_response_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


