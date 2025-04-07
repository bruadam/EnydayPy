# openapi_client.DefaultApi

All URIs are relative to *https://app.Enyday.com/connected/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses_by_user_id**](DefaultApi.md#get_addresses_by_user_id) | **GET** /2.0/address/address | Get Addresses By UserId
[**get_eloverblik_authorizations**](DefaultApi.md#get_eloverblik_authorizations) | **GET** /1.0/eloverblik/authorization | Get Eloverblik Authorizations
[**get_hourly_power_data**](DefaultApi.md#get_hourly_power_data) | **GET** /1.0/btm/invoice-line-graph | Get Hourly Power Internal and External By UserId and AddressId
[**get_user_auth_token**](DefaultApi.md#get_user_auth_token) | **POST** /1.0/user/user | Get User Auth Token
[**get_user_details**](DefaultApi.md#get_user_details) | **GET** /1.0/user/user | Get User Details


# **get_addresses_by_user_id**
> AddressResponse get_addresses_by_user_id(user_id)

Get Addresses By UserId

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.address_response import AddressResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.Enyday.com/connected/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.Enyday.com/connected/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 56 # int | The user ID to fetch addresses

    try:
        # Get Addresses By UserId
        api_response = api_instance.get_addresses_by_user_id(user_id)
        print("The response of DefaultApi->get_addresses_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_addresses_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user ID to fetch addresses | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Addresses retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eloverblik_authorizations**
> EloverblikAuthorizationResponse get_eloverblik_authorizations(user_id)

Get Eloverblik Authorizations

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.eloverblik_authorization_response import EloverblikAuthorizationResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.Enyday.com/connected/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.Enyday.com/connected/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 56 # int | The user ID to fetch authorizations

    try:
        # Get Eloverblik Authorizations
        api_response = api_instance.get_eloverblik_authorizations(user_id)
        print("The response of DefaultApi->get_eloverblik_authorizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_eloverblik_authorizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user ID to fetch authorizations | 

### Return type

[**EloverblikAuthorizationResponse**](EloverblikAuthorizationResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eloverblik authorizations fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hourly_power_data**
> PowerConsumptionResponse get_hourly_power_data(user_id, address_id, begin, end)

Get Hourly Power Internal and External By UserId and AddressId

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.power_consumption_response import PowerConsumptionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.Enyday.com/connected/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.Enyday.com/connected/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_id = 56 # int | The user ID for the data
    address_id = 56 # int | The address ID for the data
    begin = '2013-10-20T19:20:30+01:00' # datetime | Start time for the data
    end = '2013-10-20T19:20:30+01:00' # datetime | End time for the data

    try:
        # Get Hourly Power Internal and External By UserId and AddressId
        api_response = api_instance.get_hourly_power_data(user_id, address_id, begin, end)
        print("The response of DefaultApi->get_hourly_power_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_hourly_power_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user ID for the data | 
 **address_id** | **int**| The address ID for the data | 
 **begin** | **datetime**| Start time for the data | 
 **end** | **datetime**| End time for the data | 

### Return type

[**PowerConsumptionResponse**](PowerConsumptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Power consumption data retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_token**
> AuthTokenResponse get_user_auth_token(user_user_body)

Get User Auth Token

### Example


```python
import openapi_client
from openapi_client.models.auth_token_response import AuthTokenResponse
from openapi_client.models.user_user_body import UserUserBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.Enyday.com/connected/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.Enyday.com/connected/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_user_body = openapi_client.UserUserBody() # UserUserBody | 

    try:
        # Get User Auth Token
        api_response = api_instance.get_user_auth_token(user_user_body)
        print("The response of DefaultApi->get_user_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_user_body** | [**UserUserBody**](UserUserBody.md)|  | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auth token successfully generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_details**
> UserDetailsResponse get_user_details()

Get User Details

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.user_details_response import UserDetailsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.Enyday.com/connected/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.Enyday.com/connected/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get User Details
        api_response = api_instance.get_user_details()
        print("The response of DefaultApi->get_user_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDetailsResponse**](UserDetailsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details fetched successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

