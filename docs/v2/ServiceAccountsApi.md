# datadog_api_client.v2.ServiceAccountsApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                                                                                     | HTTP request                                                                           | Description                                        |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [**create_service_account_application_key**](ServiceAccountsApi.md#create_service_account_application_key) | **POST** /api/v2/service_accounts/{service_account_id}/application_keys                | Create an application key for this service account |
| [**delete_service_account_application_key**](ServiceAccountsApi.md#delete_service_account_application_key) | **DELETE** /api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id} | Delete an application key for this service account |
| [**get_service_account_application_key**](ServiceAccountsApi.md#get_service_account_application_key)       | **GET** /api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}    | Get one application key for this service account   |
| [**list_service_account_application_keys**](ServiceAccountsApi.md#list_service_account_application_keys)   | **GET** /api/v2/service_accounts/{service_account_id}/application_keys                 | List application keys for this service account     |
| [**update_service_account_application_key**](ServiceAccountsApi.md#update_service_account_application_key) | **PATCH** /api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}  | Edit an application key for this service account   |

# **create_service_account_application_key**

> ApplicationKeyResponse create_service_account_application_key(service_account_id, body)

Create an application key for this service account.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    body = ApplicationKeyCreateRequest(
        data=ApplicationKeyCreateData(
            attributes=ApplicationKeyCreateAttributes(
                name="Application Key for submitting metrics",
            ),
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyCreateRequest |

    # example passing only required values which don't have defaults set
    try:
        # Create an application key for this service account
        api_response = api_instance.create_service_account_application_key(service_account_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->create_service_account_application_key: %s\n" % e)
```

### Parameters

| Name                   | Type                                                              | Description                    | Notes |
| ---------------------- | ----------------------------------------------------------------- | ------------------------------ | ----- |
| **service_account_id** | **str**                                                           | The ID of the service account. |
| **body**               | [**ApplicationKeyCreateRequest**](ApplicationKeyCreateRequest.md) |                                |

### Return type

[**ApplicationKeyResponse**](ApplicationKeyResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **201**     | Created           | -                |
| **400**     | Bad Request       | -                |
| **403**     | Forbidden         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_service_account_application_key**

> delete_service_account_application_key(service_account_id, app_key_id)

Delete an application key owned by this service account.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application key for this service account
        api_instance.delete_service_account_application_key(service_account_id, app_key_id)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->delete_service_account_application_key: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                    | Notes |
| ---------------------- | ------- | ------------------------------ | ----- |
| **service_account_id** | **str** | The ID of the service account. |
| **app_key_id**         | **str** | The ID of the application key. |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **204**     | No Content        | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_service_account_application_key**

> PartialApplicationKeyResponse get_service_account_application_key(service_account_id, app_key_id)

Get an application key owned by this service account.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    app_key_id = "app_key_id_example"  # str | The ID of the application key.

    # example passing only required values which don't have defaults set
    try:
        # Get one application key for this service account
        api_response = api_instance.get_service_account_application_key(service_account_id, app_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->get_service_account_application_key: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                    | Notes |
| ---------------------- | ------- | ------------------------------ | ----- |
| **service_account_id** | **str** | The ID of the service account. |
| **app_key_id**         | **str** | The ID of the application key. |

### Return type

[**PartialApplicationKeyResponse**](PartialApplicationKeyResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_service_account_application_keys**

> ListApplicationKeysResponse list_service_account_application_keys(service_account_id)

List all application keys available for this service account.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = ApplicationKeysSort("name")  # ApplicationKeysSort | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. (optional)
    filter = "filter_example"  # str | Filter application keys by the specified string. (optional)
    filter_created_at_start = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or after the specified date. (optional)
    filter_created_at_end = "2020-11-24T18:46:21+00:00"  # str | Only include application keys created on or before the specified date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List application keys for this service account
        api_response = api_instance.list_service_account_application_keys(service_account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->list_service_account_application_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List application keys for this service account
        api_response = api_instance.list_service_account_application_keys(service_account_id, page_size=page_size, page_number=page_number, sort=sort, filter=filter, filter_created_at_start=filter_created_at_start, filter_created_at_end=filter_created_at_end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->list_service_account_application_keys: %s\n" % e)
```

### Parameters

| Name                        | Type                    | Description                                                                                                                                                        | Notes                                                             |
| --------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **service_account_id**      | **str**                 | The ID of the service account.                                                                                                                                     |
| **page_size**               | **int**                 | Size for a given page.                                                                                                                                             | [optional] if omitted the server will use the default value of 10 |
| **page_number**             | **int**                 | Specific page number to return.                                                                                                                                    | [optional] if omitted the server will use the default value of 0  |
| **sort**                    | **ApplicationKeysSort** | Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign. | [optional]                                                        |
| **filter**                  | **str**                 | Filter application keys by the specified string.                                                                                                                   | [optional]                                                        |
| **filter_created_at_start** | **str**                 | Only include application keys created on or after the specified date.                                                                                              | [optional]                                                        |
| **filter_created_at_end**   | **str**                 | Only include application keys created on or before the specified date.                                                                                             | [optional]                                                        |

### Return type

[**ListApplicationKeysResponse**](ListApplicationKeysResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_service_account_application_key**

> PartialApplicationKeyResponse update_service_account_application_key(service_account_id, app_key_id, body)

Edit an application key owned by this service account.

### Example

- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import service_accounts_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_id = "00000000-0000-0000-0000-000000000000"  # str | The ID of the service account.
    app_key_id = "app_key_id_example"  # str | The ID of the application key.
    body = ApplicationKeyUpdateRequest(
        data=ApplicationKeyUpdateData(
            attributes=ApplicationKeyUpdateAttributes(
                name="Application Key for submitting metrics",
            ),
            id="00112233-4455-6677-8899-aabbccddeeff",
            type=ApplicationKeysType("application_keys"),
        ),
    )  # ApplicationKeyUpdateRequest |

    # example passing only required values which don't have defaults set
    try:
        # Edit an application key for this service account
        api_response = api_instance.update_service_account_application_key(service_account_id, app_key_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceAccountsApi->update_service_account_application_key: %s\n" % e)
```

### Parameters

| Name                   | Type                                                              | Description                    | Notes |
| ---------------------- | ----------------------------------------------------------------- | ------------------------------ | ----- |
| **service_account_id** | **str**                                                           | The ID of the service account. |
| **app_key_id**         | **str**                                                           | The ID of the application key. |
| **body**               | [**ApplicationKeyUpdateRequest**](ApplicationKeyUpdateRequest.md) |                                |

### Return type

[**PartialApplicationKeyResponse**](PartialApplicationKeyResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Forbidden         | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
