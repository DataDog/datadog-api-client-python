# datadog_api_client.v2.IncidentsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_incident**](IncidentsApi.md#create_incident) | **POST** /api/v2/incidents | Create an incident
[**delete_incident**](IncidentsApi.md#delete_incident) | **DELETE** /api/v2/incidents/{incident_id} | Delete an existing incident
[**get_incident**](IncidentsApi.md#get_incident) | **GET** /api/v2/incidents/{incident_id} | Get the details of an incident
[**list_incidents**](IncidentsApi.md#list_incidents) | **GET** /api/v2/incidents | Get a list of incidents
[**update_incident**](IncidentsApi.md#update_incident) | **PATCH** /api/v2/incidents/{incident_id} | Update an existing incident


# **create_incident**
> IncidentResponse create_incident(body)

Create an incident

Create an incident.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["create_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    body = IncidentCreateRequest(
        data=IncidentCreateData(
            attributes=IncidentCreateAttributes(
                customer_impacted=False,
                fields={
                    "key": IncidentFieldAttributes(),
                },
                initial_timeline_cells=[
                    IncidentTimelineCellCreateAttributes(),
                ],
                notification_handles=[
                    "@test.user@test.com",
                ],
                title="A test incident title",
            ),
            relationships=IncidentCreateRelationships(
                commander=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
            ),
            type=IncidentType("incidents"),
        ),
    )  # IncidentCreateRequest | Incident payload.

    # example passing only required values which don't have defaults set
    try:
        # Create an incident
        api_response = api_instance.create_incident(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->create_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncidentCreateRequest**](IncidentCreateRequest.md)| Incident payload. |

### Return type

[**IncidentResponse**](IncidentResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_incident**
> delete_incident(incident_id)

Delete an existing incident

Deletes an existing incident from the users organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["delete_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_id = "incident_id_example"  # str | The UUID the incident.

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing incident
        api_instance.delete_incident(incident_id)
    except ApiException as e:
        print("Exception when calling IncidentsApi->delete_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**| The UUID the incident. |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_incident**
> IncidentResponse get_incident(incident_id)

Get the details of an incident

Get the details of an incident by `incident_id`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["get_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_id = "incident_id_example"  # str | The UUID the incident.
    include = [
        IncidentRelatedObject("users"),
    ]  # [IncidentRelatedObject] | Specifies which types of related objects should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the details of an incident
        api_response = api_instance.get_incident(incident_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the details of an incident
        api_response = api_instance.get_incident(incident_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**| The UUID the incident. |
 **include** | [**[IncidentRelatedObject]**](IncidentRelatedObject.md)| Specifies which types of related objects should be included in the response. | [optional]

### Return type

[**IncidentResponse**](IncidentResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_incidents**
> IncidentsResponse list_incidents()

Get a list of incidents

Get all incidents for the user's organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["list_incidents"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    include = [
        IncidentRelatedObject("users"),
    ]  # [IncidentRelatedObject] | Specifies which types of related objects should be included in the response. (optional)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_offset = 0  # int | Specific offset to use as the beginning of the returned page. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of incidents
        api_response = api_instance.list_incidents(include=include, page_size=page_size, page_offset=page_offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->list_incidents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**[IncidentRelatedObject]**](IncidentRelatedObject.md)| Specifies which types of related objects should be included in the response. | [optional]
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_offset** | **int**| Specific offset to use as the beginning of the returned page. | [optional] if omitted the server will use the default value of 0

### Return type

[**IncidentsResponse**](IncidentsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_incident**
> IncidentResponse update_incident(incident_id, body)

Update an existing incident

Updates an incident. Provide only the attributes that should be updated as this request is a partial update.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
configuration.unstable_operations["update_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_id = "incident_id_example"  # str | The UUID the incident.
    body = IncidentUpdateRequest(
        data=IncidentUpdateData(
            attributes=IncidentUpdateAttributes(
                customer_impact_end=dateutil_parser('1970-01-01T00:00:00.00Z'),
                customer_impact_scope="Example customer impact scope",
                customer_impact_start=dateutil_parser('1970-01-01T00:00:00.00Z'),
                customer_impacted=False,
                detected=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields={
                    "key": IncidentFieldAttributes(),
                },
                notification_handles=[
                    "@test.user@test.com",
                ],
                resolved=dateutil_parser('1970-01-01T00:00:00.00Z'),
                title="A test incident title",
            ),
            id="00000000-0000-0000-0000-000000000000",
            relationships=IncidentUpdateRelationships(
                commander_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                created_by_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                integrations=RelationshipToIncidentIntegrationMetadatas(
                    data=[{"id":"00000000-0000-0000-0000-000000000000","type":"incident_integration_metadata"},{"id":"00000000-0000-0000-0000-000000000000","type":"incident_integration_metadata"}],
                ),
                last_modified_by_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                postmortem=RelationshipToIncidentPostmortem(
                    data=RelationshipToIncidentPostmortemData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=IncidentPostmortemType("incident_postmortems"),
                    ),
                ),
            ),
            type=IncidentType("incidents"),
        ),
    )  # IncidentUpdateRequest | Incident Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing incident
        api_response = api_instance.update_incident(incident_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->update_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**| The UUID the incident. |
 **body** | [**IncidentUpdateRequest**](IncidentUpdateRequest.md)| Incident Payload. |

### Return type

[**IncidentResponse**](IncidentResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

