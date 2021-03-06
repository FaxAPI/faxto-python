# swagger-client
This is Fax.to REST API client for Python.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://fax.to/contact-us](https://fax.to/contact-us)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FaxReceivingApi(swagger_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.fax.to/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FaxReceivingApi* | [**area_codes_country_code_state_id_get**](docs/FaxReceivingApi.md#area_codes_country_code_state_id_get) | **GET** /areacodes/{COUNTRY_CODE}/{STATE_ID} | This API gets a list of countries with its area code
*FaxReceivingApi* | [**countries_country_code_did_groups_get**](docs/FaxReceivingApi.md#countries_country_code_did_groups_get) | **GET** /countries/{countryCode}/didgroups | This API gets a list of DID groups
*FaxReceivingApi* | [**countries_get**](docs/FaxReceivingApi.md#countries_get) | **GET** /countries | This API gets a list of countries available in the Fax.to coverage
*FaxReceivingApi* | [**incoming_faxes_get**](docs/FaxReceivingApi.md#incoming_faxes_get) | **GET** /incoming-faxes | This API gets a list of incoming faxes
*FaxReceivingApi* | [**incoming_faxes_recipient_get**](docs/FaxReceivingApi.md#incoming_faxes_recipient_get) | **GET** /incoming-faxes/{recipient} | This API gets a list of incoming faxes for a specific recipient
*FaxReceivingApi* | [**numbers_get**](docs/FaxReceivingApi.md#numbers_get) | **GET** /numbers | This API gets a list of numbers to get the current configuration of one or multiple number
*FaxReceivingApi* | [**provision_numbers_get**](docs/FaxReceivingApi.md#provision_numbers_get) | **GET** /countries/didgroups/{did_group_id}/provision | This API gets a list of provisioned numbers
*FaxReceivingApi* | [**states_country_code_get**](docs/FaxReceivingApi.md#states_country_code_get) | **GET** /states/{COUNTRY_CODE} | This API gets a list of states of a given country available in the Fax.to coverage
*FaxSendingApi* | [**fax_document_id_costs_get**](docs/FaxSendingApi.md#fax_document_id_costs_get) | **GET** /fax/{document_id}/costs | This API is for computing the cost of the fax to be sent
*FaxSendingApi* | [**fax_history_get**](docs/FaxSendingApi.md#fax_history_get) | **GET** /fax-history | This API gets the history of a fax
*FaxSendingApi* | [**fax_job_id_status_get**](docs/FaxSendingApi.md#fax_job_id_status_get) | **GET** /fax/{fax_job_id}/status | This API gets the status of a fax
*FaxSendingApi* | [**fax_post**](docs/FaxSendingApi.md#fax_post) | **POST** /fax | This API is for sending a new fax in any fax numbers anywhere in the world
*FaxSendingApi* | [**file_clean_get**](docs/FaxSendingApi.md#file_clean_get) | **GET** /file-clean | This API is used for cleaning a document
*FaxSendingApi* | [**file_generate_preview_get**](docs/FaxSendingApi.md#file_generate_preview_get) | **GET** /file-generate-preview | This API generates a preview of a document
*FaxSendingApi* | [**files_document_id_delete**](docs/FaxSendingApi.md#files_document_id_delete) | **DELETE** /files/{document_id} | This API deletes a document
*FaxSendingApi* | [**files_get**](docs/FaxSendingApi.md#files_get) | **GET** /files | This API gets all the files of a certain user
*UserApi* | [**balance_get**](docs/UserApi.md#balance_get) | **GET** /balance | This API gets the balance of a user account
*UserManagementApi* | [**sub_user_post**](docs/UserManagementApi.md#sub_user_post) | **POST** /subuser | This API creates a subuser
*UserManagementApi* | [**user_login_post**](docs/UserManagementApi.md#user_login_post) | **POST** /user/login | This API is used for logging in on an existing user account
*UserManagementApi* | [**user_post**](docs/UserManagementApi.md#user_post) | **POST** /user | This API registers a new user account


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20012Data](docs/InlineResponse20012Data.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013States](docs/InlineResponse20013States.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20014Areacodes](docs/InlineResponse20014Areacodes.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20015Data](docs/InlineResponse20015Data.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20016Data](docs/InlineResponse20016Data.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20017Numbers](docs/InlineResponse20017Numbers.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Created](docs/InlineResponse2003Created.md)
 - [InlineResponse2003History](docs/InlineResponse2003History.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2004Inbox](docs/InlineResponse2004Inbox.md)
 - [InlineResponse2004Meta](docs/InlineResponse2004Meta.md)
 - [InlineResponse2004MetaPagination](docs/InlineResponse2004MetaPagination.md)
 - [InlineResponse2004MetaPaginationLinks](docs/InlineResponse2004MetaPaginationLinks.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Files](docs/InlineResponse2008Files.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse400](docs/InlineResponse400.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author

inquiries@fax.to

