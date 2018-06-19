# swagger_client.FaxReceivingApi

All URIs are relative to *https://api.fax.to/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**area_codes_country_code_state_id_get**](FaxReceivingApi.md#area_codes_country_code_state_id_get) | **GET** /areacodes/{COUNTRY_CODE}/{STATE_ID} | This API gets a list of countries with its area code
[**countries_country_code_did_groups_get**](FaxReceivingApi.md#countries_country_code_did_groups_get) | **GET** /countries/{countryCode}/didgroups | This API gets a list of DID groups
[**countries_get**](FaxReceivingApi.md#countries_get) | **GET** /countries | This API gets a list of countries available in the Fax.to coverage
[**incoming_faxes_get**](FaxReceivingApi.md#incoming_faxes_get) | **GET** /incoming-faxes | This API gets a list of incoming faxes
[**incoming_faxes_recipient_get**](FaxReceivingApi.md#incoming_faxes_recipient_get) | **GET** /incoming-faxes/{recipient} | This API gets a list of incoming faxes for a specific recipient
[**numbers_get**](FaxReceivingApi.md#numbers_get) | **GET** /numbers | This API gets a list of numbers to get the current configuration of one or multiple number
[**provision_numbers_get**](FaxReceivingApi.md#provision_numbers_get) | **GET** /countries/didgroups/{did_group_id}/provision | This API gets a list of provisioned numbers
[**states_country_code_get**](FaxReceivingApi.md#states_country_code_get) | **GET** /states/{COUNTRY_CODE} | This API gets a list of states of a given country available in the Fax.to coverage


# **area_codes_country_code_state_id_get**
> InlineResponse20014 area_codes_country_code_state_id_get(country_code, state_id, api_key)

This API gets a list of countries with its area code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
country_code = 56 # int | Indicates the country code in its ISO 3166-1 alpha-3 format
state_id = 56 # int | The numerical identifier for the state
api_key = 'api_key_example' # str | 

try:
    # This API gets a list of countries with its area code
    api_response = api_instance.area_codes_country_code_state_id_get(country_code, state_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->area_codes_country_code_state_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| Indicates the country code in its ISO 3166-1 alpha-3 format | 
 **state_id** | **int**| The numerical identifier for the state | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countries_country_code_did_groups_get**
> InlineResponse20015 countries_country_code_did_groups_get(country_code, area_code, api_key, did_group_ids=did_group_ids, state_id=state_id, city_name_pattern=city_name_pattern)

This API gets a list of DID groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
country_code = 56 # int | Indicates the country code of the DID group in its ISO 3166-1 alpha-3 format
area_code = 56 # int | The area code of the DID group
api_key = 'api_key_example' # str | 
did_group_ids = 56 # int | Used to display more information about specific DID groups (optional)
state_id = 56 # int | The numerical identifier for the didGroup's state (optional)
city_name_pattern = 56 # int | A string pattern for the beginning of city name (optional)

try:
    # This API gets a list of DID groups
    api_response = api_instance.countries_country_code_did_groups_get(country_code, area_code, api_key, did_group_ids=did_group_ids, state_id=state_id, city_name_pattern=city_name_pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->countries_country_code_did_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| Indicates the country code of the DID group in its ISO 3166-1 alpha-3 format | 
 **area_code** | **int**| The area code of the DID group | 
 **api_key** | **str**|  | 
 **did_group_ids** | **int**| Used to display more information about specific DID groups | [optional] 
 **state_id** | **int**| The numerical identifier for the didGroup&#39;s state | [optional] 
 **city_name_pattern** | **int**| A string pattern for the beginning of city name | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countries_get**
> InlineResponse20012 countries_get(api_key)

This API gets a list of countries available in the Fax.to coverage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
api_key = 'api_key_example' # str | 

try:
    # This API gets a list of countries available in the Fax.to coverage
    api_response = api_instance.countries_get(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->countries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_faxes_get**
> InlineResponse2004 incoming_faxes_get(api_key, limit=limit, page=page)

This API gets a list of incoming faxes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
api_key = 'api_key_example' # str | 
limit = 'limit_example' # str | The number of record to return (optional)
page = 'page_example' # str | The page you want to get (optional)

try:
    # This API gets a list of incoming faxes
    api_response = api_instance.incoming_faxes_get(api_key, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->incoming_faxes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **limit** | **str**| The number of record to return | [optional] 
 **page** | **str**| The page you want to get | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_faxes_recipient_get**
> InlineResponse2004 incoming_faxes_recipient_get(recipient, api_key, limit=limit, page=page)

This API gets a list of incoming faxes for a specific recipient

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
recipient = 56 # int | The recipient's fax number
api_key = 'api_key_example' # str | 
limit = 'limit_example' # str | The number of record to return (optional)
page = 'page_example' # str | The page you want to get (optional)

try:
    # This API gets a list of incoming faxes for a specific recipient
    api_response = api_instance.incoming_faxes_recipient_get(recipient, api_key, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->incoming_faxes_recipient_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient** | **int**| The recipient&#39;s fax number | 
 **api_key** | **str**|  | 
 **limit** | **str**| The number of record to return | [optional] 
 **page** | **str**| The page you want to get | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numbers_get**
> InlineResponse20017 numbers_get(api_key, limit=limit, page=page)

This API gets a list of numbers to get the current configuration of one or multiple number

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
api_key = 'api_key_example' # str | 
limit = 'limit_example' # str | The number of record to return (optional)
page = 'page_example' # str | The page you want to get (optional)

try:
    # This API gets a list of numbers to get the current configuration of one or multiple number
    api_response = api_instance.numbers_get(api_key, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->numbers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **limit** | **str**| The number of record to return | [optional] 
 **page** | **str**| The page you want to get | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_numbers_get**
> InlineResponse20016 provision_numbers_get(did_group_id, api_key)

This API gets a list of provisioned numbers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
did_group_id = 56 # int | The id of the did group
api_key = 'api_key_example' # str | 

try:
    # This API gets a list of provisioned numbers
    api_response = api_instance.provision_numbers_get(did_group_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->provision_numbers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did_group_id** | **int**| The id of the did group | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **states_country_code_get**
> InlineResponse20013 states_country_code_get(country_code, api_key)

This API gets a list of states of a given country available in the Fax.to coverage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi()
country_code = 56 # int | Indicates the country code in its ISO 3166-1 alpha-3 format
api_key = 'api_key_example' # str | 

try:
    # This API gets a list of states of a given country available in the Fax.to coverage
    api_response = api_instance.states_country_code_get(country_code, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxReceivingApi->states_country_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **int**| Indicates the country code in its ISO 3166-1 alpha-3 format | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

