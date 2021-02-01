# datadog_api_client.v2.UsersApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /api/v2/users | Create a user
[**disable_user**](UsersApi.md#disable_user) | **DELETE** /api/v2/users/{user_id} | Disable a user
[**get_invitation**](UsersApi.md#get_invitation) | **GET** /api/v2/user_invitations/{user_invitation_uuid} | Get a user invitation
[**get_user**](UsersApi.md#get_user) | **GET** /api/v2/users/{user_id} | Get user details
[**list_user_organizations**](UsersApi.md#list_user_organizations) | **GET** /api/v2/users/{user_id}/orgs | Get a user organization
[**list_user_permissions**](UsersApi.md#list_user_permissions) | **GET** /api/v2/users/{user_id}/permissions | Get a user permissions
[**list_users**](UsersApi.md#list_users) | **GET** /api/v2/users | List all users
[**send_invitations**](UsersApi.md#send_invitations) | **POST** /api/v2/user_invitations | Send invitation emails
[**update_user**](UsersApi.md#update_user) | **PATCH** /api/v2/users/{user_id} | Update a user


# **create_user**
> UserResponse create_user(body)

Create a user

Create a user for your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    body = UserCreateRequest(
        data=UserCreateData(
            attributes=UserCreateAttributes(
                email="jane.doe@example.com",
                name="name_example",
                title="title_example",
            ),
            relationships=UserRelationships(
                roles=RelationshipToRoles(
                    data=[
                        RelationshipToRoleData(
                            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
                            type=RolesType("roles"),
                        ),
                    ],
                ),
            ),
            type=UsersType("users"),
        ),
    )  # UserCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a user
        api_response = api_instance.create_user(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)|  |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **disable_user**
> disable_user(user_id)

Disable a user

Disable a user. Can only be used with an application key belonging to an administrator user.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example"  # str | The ID of the user.

    # example passing only required values which don't have defaults set
    try:
        # Disable a user
        api_instance.disable_user(user_id)
    except ApiException as e:
        print("Exception when calling UsersApi->disable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. |

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
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_invitation**
> UserInvitationResponse get_invitation(user_invitation_uuid)

Get a user invitation

Returns a single user invitation by its UUID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_invitation_uuid = "user_invitation_uuid_example"  # str | The UUID of the user invitation.

    # example passing only required values which don't have defaults set
    try:
        # Get a user invitation
        api_response = api_instance.get_invitation(user_invitation_uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invitation_uuid** | **str**| The UUID of the user invitation. |

### Return type

[**UserInvitationResponse**](UserInvitationResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_user**
> UserResponse get_user(user_id)

Get user details

Get a user in the organization specified by the user’s `user_id`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example"  # str | The ID of the user.

    # example passing only required values which don't have defaults set
    try:
        # Get user details
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK for get user |  -  |
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_user_organizations**
> UserResponse list_user_organizations(user_id)

Get a user organization

Get a user organization. Returns the user information and all organizations joined by this user.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example"  # str | The ID of the user.

    # example passing only required values which don't have defaults set
    try:
        # Get a user organization
        api_response = api_instance.list_user_organizations(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_user_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_user_permissions**
> PermissionsResponse list_user_permissions(user_id)

Get a user permissions

Get a user permission set. Returns a list of the user’s permissions granted by the associated user's roles.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example"  # str | The ID of the user.

    # example passing only required values which don't have defaults set
    try:
        # Get a user permissions
        api_response = api_instance.list_user_permissions(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_users**
> UsersResponse list_users()

List all users

Get the list of all users in the organization. This list includes all users even if they are deactivated or unverified.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = "name"  # str | User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `modified_at`, `user_count`. (optional) if omitted the server will use the default value of "name"
    sort_dir = QuerySortOrder("desc")  # QuerySortOrder | Direction of sort. Options: `asc`, `desc`. (optional)
    filter = "filter_example"  # str | Filter all users by the given string. Defaults to no filtering. (optional)
    filter_status = "filter[status]_example"  # str | Filter on status attribute. Comma separated list, with possible values `Active`, `Pending`, and `Disabled`. Defaults to no filtering. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all users
        api_response = api_instance.list_users(page_size=page_size, page_number=page_number, sort=sort, sort_dir=sort_dir, filter=filter, filter_status=filter_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example &#x60;sort&#x3D;-name&#x60;. Options: &#x60;name&#x60;, &#x60;modified_at&#x60;, &#x60;user_count&#x60;. | [optional] if omitted the server will use the default value of "name"
 **sort_dir** | **QuerySortOrder**| Direction of sort. Options: &#x60;asc&#x60;, &#x60;desc&#x60;. | [optional]
 **filter** | **str**| Filter all users by the given string. Defaults to no filtering. | [optional]
 **filter_status** | **str**| Filter on status attribute. Comma separated list, with possible values &#x60;Active&#x60;, &#x60;Pending&#x60;, and &#x60;Disabled&#x60;. Defaults to no filtering. | [optional]

### Return type

[**UsersResponse**](UsersResponse.md)

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
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **send_invitations**
> UserInvitationsResponse send_invitations(body)

Send invitation emails

Sends emails to one or more users inviting them to join the organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    body = UserInvitationsRequest(
        data=[],
    )  # UserInvitationsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Send invitation emails
        api_response = api_instance.send_invitations(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->send_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInvitationsRequest**](UserInvitationsRequest.md)|  |

### Return type

[**UserInvitationsResponse**](UserInvitationsResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_user**
> UserResponse update_user(user_id, body)

Update a user

Edit a user. Can only be used with an application key belonging to an administrator user.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v2.Configuration(
    host="https://api.datadoghq.com"
)

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example"  # str | The ID of the user.
    body = UserUpdateRequest(
        data=UserUpdateData(
            attributes=UserUpdateAttributes(
                disabled=True,
                email="email_example",
                name="name_example",
            ),
            id="00000000-0000-0000-0000-000000000000",
            type=UsersType("users"),
        ),
    )  # UserUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_user(user_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. |
 **body** | [**UserUpdateRequest**](UserUpdateRequest.md)|  |

### Return type

[**UserResponse**](UserResponse.md)

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
**403** | Authentication error |  -  |
**404** | Not found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

