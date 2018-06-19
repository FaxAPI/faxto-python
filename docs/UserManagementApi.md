# swagger_client.UserManagementApi

All URIs are relative to *https://api.fax.to/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sub_user_post**](UserManagementApi.md#sub_user_post) | **POST** /subuser | This API creates a subuser
[**user_login_post**](UserManagementApi.md#user_login_post) | **POST** /user/login | This API is used for logging in on an existing user account
[**user_post**](UserManagementApi.md#user_post) | **POST** /user | This API registers a new user account


# **sub_user_post**
> InlineResponse2006 sub_user_post(email, password, api_key)

This API creates a subuser

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserManagementApi()
email = swagger_client.null() #  | The unique email of the user
password = swagger_client.null() #  | The password of the subuser
api_key = 'api_key_example' # str | 

try:
    # This API creates a subuser
    api_response = api_instance.sub_user_post(email, password, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->sub_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [****](.md)| The unique email of the user | 
 **password** | [****](.md)| The password of the subuser | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login_post**
> InlineResponse2005 user_login_post(email, password)

This API is used for logging in on an existing user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserManagementApi()
email = swagger_client.null() #  | The unique email of the user
password = swagger_client.null() #  | The password of the user

try:
    # This API is used for logging in on an existing user account
    api_response = api_instance.user_login_post(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [****](.md)| The unique email of the user | 
 **password** | [****](.md)| The password of the user | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> InlineResponse2005 user_post(email, password)

This API registers a new user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserManagementApi()
email = swagger_client.null() #  | The unique email of the user
password = swagger_client.null() #  | The password of the user

try:
    # This API registers a new user account
    api_response = api_instance.user_post(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [****](.md)| The unique email of the user | 
 **password** | [****](.md)| The password of the user | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

