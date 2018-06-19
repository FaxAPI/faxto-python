# swagger_client.FaxSendingApi

All URIs are relative to *https://api.fax.to/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_document_id_costs_get**](FaxSendingApi.md#fax_document_id_costs_get) | **GET** /fax/{document_id}/costs | This API is for computing the cost of the fax to be sent
[**fax_history_get**](FaxSendingApi.md#fax_history_get) | **GET** /fax-history | This API gets the history of a fax
[**fax_job_id_status_get**](FaxSendingApi.md#fax_job_id_status_get) | **GET** /fax/{fax_job_id}/status | This API gets the status of a fax
[**fax_post**](FaxSendingApi.md#fax_post) | **POST** /fax | This API is for sending a new fax in any fax numbers anywhere in the world
[**file_clean_get**](FaxSendingApi.md#file_clean_get) | **GET** /file-clean | This API is used for cleaning a document
[**file_generate_preview_get**](FaxSendingApi.md#file_generate_preview_get) | **GET** /file-generate-preview | This API generates a preview of a document
[**files_document_id_delete**](FaxSendingApi.md#files_document_id_delete) | **DELETE** /files/{document_id} | This API deletes a document
[**files_get**](FaxSendingApi.md#files_get) | **GET** /files | This API gets all the files of a certain user


# **fax_document_id_costs_get**
> InlineResponse2001 fax_document_id_costs_get(document_id, api_key, fax_number=fax_number)

This API is for computing the cost of the fax to be sent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
document_id = 56 # int | The id of the document to be sent
api_key = 'api_key_example' # str | 
fax_number = 'fax_number_example' # str | The fax number of the recipient (optional)

try:
    # This API is for computing the cost of the fax to be sent
    api_response = api_instance.fax_document_id_costs_get(document_id, api_key, fax_number=fax_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->fax_document_id_costs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| The id of the document to be sent | 
 **api_key** | **str**|  | 
 **fax_number** | **str**| The fax number of the recipient | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_history_get**
> InlineResponse2003 fax_history_get(api_key, limit=limit, page=page)

This API gets the history of a fax

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
api_key = 'api_key_example' # str | 
limit = 'limit_example' # str | The number of record to return (optional)
page = 'page_example' # str | The page you want to get (optional)

try:
    # This API gets the history of a fax
    api_response = api_instance.fax_history_get(api_key, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->fax_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **limit** | **str**| The number of record to return | [optional] 
 **page** | **str**| The page you want to get | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_job_id_status_get**
> InlineResponse2002 fax_job_id_status_get(fax_job_id, api_key)

This API gets the status of a fax

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
fax_job_id = 56 # int | The id of the fax job
api_key = 'api_key_example' # str | 

try:
    # This API gets the status of a fax
    api_response = api_instance.fax_job_id_status_get(fax_job_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->fax_job_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_job_id** | **int**| The id of the fax job | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fax_post**
> InlineResponse200 fax_post(fax_number, document_id, api_key)

This API is for sending a new fax in any fax numbers anywhere in the world

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
fax_number = swagger_client.null() #  | The fax number of the recipient
document_id = swagger_client.null() #  | The id of the document to be sent
api_key = 'api_key_example' # str | 

try:
    # This API is for sending a new fax in any fax numbers anywhere in the world
    api_response = api_instance.fax_post(fax_number, document_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->fax_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fax_number** | [****](.md)| The fax number of the recipient | 
 **document_id** | [****](.md)| The id of the document to be sent | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_clean_get**
> InlineResponse2009 file_clean_get(document_id, api_key)

This API is used for cleaning a document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
document_id = 56 # int | The id of the document
api_key = 'api_key_example' # str | 

try:
    # This API is used for cleaning a document
    api_response = api_instance.file_clean_get(document_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->file_clean_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| The id of the document | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_generate_preview_get**
> InlineResponse20010 file_generate_preview_get(document_id, api_key)

This API generates a preview of a document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
document_id = 56 # int | The id of the document
api_key = 'api_key_example' # str | 

try:
    # This API generates a preview of a document
    api_response = api_instance.file_generate_preview_get(document_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->file_generate_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| The id of the document | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_document_id_delete**
> InlineResponse20011 files_document_id_delete(document_id, api_key)

This API deletes a document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
document_id = 56 # int | The id of the document
api_key = 'api_key_example' # str | 

try:
    # This API deletes a document
    api_response = api_instance.files_document_id_delete(document_id, api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->files_document_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| The id of the document | 
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get**
> InlineResponse2008 files_get(api_key, limit=limit, page=page)

This API gets all the files of a certain user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxSendingApi()
api_key = 'api_key_example' # str | 
limit = 'limit_example' # str | The number of record to return (optional)
page = 'page_example' # str | The page you want to get (optional)

try:
    # This API gets all the files of a certain user
    api_response = api_instance.files_get(api_key, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaxSendingApi->files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **limit** | **str**| The number of record to return | [optional] 
 **page** | **str**| The page you want to get | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

