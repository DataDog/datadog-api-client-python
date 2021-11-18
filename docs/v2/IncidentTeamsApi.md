# datadog_api_client.v2.IncidentTeamsApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                                               | HTTP request                       | Description                      |
| -------------------------------------------------------------------- | ---------------------------------- | -------------------------------- |
| [**create_incident_team**](IncidentTeamsApi.md#create_incident_team) | **POST** /api/v2/teams             | Create a new incident team       |
| [**delete_incident_team**](IncidentTeamsApi.md#delete_incident_team) | **DELETE** /api/v2/teams/{team_id} | Delete an existing incident team |
| [**get_incident_team**](IncidentTeamsApi.md#get_incident_team)       | **GET** /api/v2/teams/{team_id}    | Get details of an incident team  |
| [**list_incident_teams**](IncidentTeamsApi.md#list_incident_teams)   | **GET** /api/v2/teams              | Get a list of all incident teams |
| [**update_incident_team**](IncidentTeamsApi.md#update_incident_team) | **PATCH** /api/v2/teams/{team_id}  | Update an existing incident team |

# **create_incident_team**

> IncidentTeamResponse create_incident_team(body)

Creates a new incident team.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_incident_team"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    body = IncidentTeamCreateRequest(
        data=IncidentTeamCreateData(
            attributes=IncidentTeamCreateAttributes(
                name="team name",
            ),
            type=IncidentTeamType("teams"),
        ),
    )  # IncidentTeamCreateRequest | Incident Team Payload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new incident team
        api_response = api_instance.create_incident_team(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->create_incident_team: %s\n" % e)
```

### Parameters

| Name     | Type                                                          | Description            | Notes |
| -------- | ------------------------------------------------------------- | ---------------------- | ----- |
| **body** | [**IncidentTeamCreateRequest**](IncidentTeamCreateRequest.md) | Incident Team Payload. |

### Return type

[**IncidentTeamResponse**](IncidentTeamResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **201**     | CREATED           | -                |
| **400**     | Bad Request       | -                |
| **401**     | Unauthorized      | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_incident_team**

> delete_incident_team(team_id)

Deletes an existing incident team.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["delete_incident_team"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    team_id = "team_id_example"  # str | The ID of the incident team.

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing incident team
        api_instance.delete_incident_team(team_id)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->delete_incident_team: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                  | Notes |
| ----------- | ------- | ---------------------------- | ----- |
| **team_id** | **str** | The ID of the incident team. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **204**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **401**     | Unauthorized      | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_incident_team**

> IncidentTeamResponse get_incident_team(team_id)

Get details of an incident team. If the `include[users]` query parameter is provided,
the included attribute will contain the users related to these incident teams.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_incident_team"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    team_id = "team_id_example"  # str | The ID of the incident team.
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of an incident team
        api_response = api_instance.get_incident_team(team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->get_incident_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of an incident team
        api_response = api_instance.get_incident_team(team_id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->get_incident_team: %s\n" % e)
```

### Parameters

| Name        | Type                      | Description                                                                  | Notes      |
| ----------- | ------------------------- | ---------------------------------------------------------------------------- | ---------- |
| **team_id** | **str**                   | The ID of the incident team.                                                 |
| **include** | **IncidentRelatedObject** | Specifies which types of related objects should be included in the response. | [optional] |

### Return type

[**IncidentTeamResponse**](IncidentTeamResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **401**     | Unauthorized      | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_incident_teams**

> IncidentTeamsResponse list_incident_teams()

Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_incident_teams"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    include = IncidentRelatedObject("users")  # IncidentRelatedObject | Specifies which types of related objects should be included in the response. (optional)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_offset = 0  # int | Specific offset to use as the beginning of the returned page. (optional) if omitted the server will use the default value of 0
    filter = "ExampleTeamName"  # str | A search query that filters teams by name. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all incident teams
        api_response = api_instance.list_incident_teams(include=include, page_size=page_size, page_offset=page_offset, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->list_incident_teams: %s\n" % e)
```

### Parameters

| Name            | Type                      | Description                                                                  | Notes                                                             |
| --------------- | ------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **include**     | **IncidentRelatedObject** | Specifies which types of related objects should be included in the response. | [optional]                                                        |
| **page_size**   | **int**                   | Size for a given page.                                                       | [optional] if omitted the server will use the default value of 10 |
| **page_offset** | **int**                   | Specific offset to use as the beginning of the returned page.                | [optional] if omitted the server will use the default value of 0  |
| **filter**      | **str**                   | A search query that filters teams by name.                                   | [optional]                                                        |

### Return type

[**IncidentTeamsResponse**](IncidentTeamsResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **401**     | Unauthorized      | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_incident_team**

> IncidentTeamResponse update_incident_team(team_id, body)

Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incident_teams_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_incident_team"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incident_teams_api.IncidentTeamsApi(api_client)
    team_id = "team_id_example"  # str | The ID of the incident team.
    body = IncidentTeamUpdateRequest(
        data=IncidentTeamUpdateData(
            attributes=IncidentTeamUpdateAttributes(
                name="team name",
            ),
            id="00000000-0000-0000-0000-000000000000",
            type=IncidentTeamType("teams"),
        ),
    )  # IncidentTeamUpdateRequest | Incident Team Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing incident team
        api_response = api_instance.update_incident_team(team_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentTeamsApi->update_incident_team: %s\n" % e)
```

### Parameters

| Name        | Type                                                          | Description                  | Notes |
| ----------- | ------------------------------------------------------------- | ---------------------------- | ----- |
| **team_id** | **str**                                                       | The ID of the incident team. |
| **body**    | [**IncidentTeamUpdateRequest**](IncidentTeamUpdateRequest.md) | Incident Team Payload.       |

### Return type

[**IncidentTeamResponse**](IncidentTeamResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **401**     | Unauthorized      | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
