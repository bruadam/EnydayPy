# PowerConsumptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoiced** | [**List[PowerConsumptionResponseInvoiced]**](PowerConsumptionResponseInvoiced.md) |  | [optional] 

## Example

```python
from openapi_client.models.power_consumption_response import PowerConsumptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PowerConsumptionResponse from a JSON string
power_consumption_response_instance = PowerConsumptionResponse.from_json(json)
# print the JSON string representation of the object
print(PowerConsumptionResponse.to_json())

# convert the object into a dict
power_consumption_response_dict = power_consumption_response_instance.to_dict()
# create an instance of PowerConsumptionResponse from a dict
power_consumption_response_from_dict = PowerConsumptionResponse.from_dict(power_consumption_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


