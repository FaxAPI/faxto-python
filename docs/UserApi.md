# swagger_client.UserApi

All URIs are relative to *https://api.fax.to/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_get**](UserApi.md#balance_get) | **GET** /balance | This API gets the balance of a user account


# **balance_get**
> InlineResponse2007 balance_get(api_key)

This API gets the balance of a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | 

try:
    # This API gets the balance of a user account
    api_response = api_instance.balance_get(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

