# PowerConsumptionResponseInvoiced


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_begin** | **datetime** |  | [optional] 
**period_end** | **datetime** |  | [optional] 
**power_internal** | **float** |  | [optional] 
**power_external** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.power_consumption_response_invoiced import PowerConsumptionResponseInvoiced

# TODO update the JSON string below
json = "{}"
# create an instance of PowerConsumptionResponseInvoiced from a JSON string
power_consumption_response_invoiced_instance = PowerConsumptionResponseInvoiced.from_json(json)
# print the JSON string representation of the object
print(PowerConsumptionResponseInvoiced.to_json())

# convert the object into a dict
power_consumption_response_invoiced_dict = power_consumption_response_invoiced_instance.to_dict()
# create an instance of PowerConsumptionResponseInvoiced from a dict
power_consumption_response_invoiced_from_dict = PowerConsumptionResponseInvoiced.from_dict(power_consumption_response_invoiced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


