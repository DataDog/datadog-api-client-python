# datadog_api_client.v2.RolesApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permission_to_role**](RolesApi.md#add_permission_to_role) | **POST** /api/v2/roles/{role_id}/permissions | Grant permission to a role
[**add_user_to_role**](RolesApi.md#add_user_to_role) | **POST** /api/v2/roles/{role_id}/users | Add a user to a role
[**create_role**](RolesApi.md#create_role) | **POST** /api/v2/roles | Create role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/v2/roles/{role_id} | Delete role
[**get_role**](RolesApi.md#get_role) | **GET** /api/v2/roles/{role_id} | Get a role
[**list_permissions**](RolesApi.md#list_permissions) | **GET** /api/v2/permissions | List permissions
[**list_role_permissions**](RolesApi.md#list_role_permissions) | **GET** /api/v2/roles/{role_id}/permissions | List permissions for a role
[**list_role_users**](RolesApi.md#list_role_users) | **GET** /api/v2/roles/{role_id}/users | Get all users of a role
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/v2/roles | List roles
[**remove_permission_from_role**](RolesApi.md#remove_permission_from_role) | **DELETE** /api/v2/roles/{role_id}/permissions | Revoke permission
[**remove_user_from_role**](RolesApi.md#remove_user_from_role) | **DELETE** /api/v2/roles/{role_id}/users | Remove a user from a role
[**update_role**](RolesApi.md#update_role) | **PATCH** /api/v2/roles/{role_id} | Update a role


# **add_permission_to_role**
> PermissionsResponse add_permission_to_role(role_id, body)

Grant permission to a role

Adds a permission to a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    body = RelationshipToPermission(
        data=RelationshipToPermissionData(
            id="id_example",
            type=PermissionsType("permissions"),
        ),
    )  # RelationshipToPermission | 

    # example passing only required values which don't have defaults set
    try:
        # Grant permission to a role
        api_response = api_instance.add_permission_to_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->add_permission_to_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **body** | [**RelationshipToPermission**](RelationshipToPermission.md)|  |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **add_user_to_role**
> UsersResponse add_user_to_role(role_id, body)

Add a user to a role

Adds a user to a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    body = RelationshipToUser(
        data=RelationshipToUserData(
            id="00000000-0000-0000-0000-000000000000",
            type=UsersType("users"),
        ),
    )  # RelationshipToUser | 

    # example passing only required values which don't have defaults set
    try:
        # Add a user to a role
        api_response = api_instance.add_user_to_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->add_user_to_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **body** | [**RelationshipToUser**](RelationshipToUser.md)|  |

### Return type

[**UsersResponse**](UsersResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_role**
> RoleCreateResponse create_role(body)

Create role

Create a new role for your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    body = RoleCreateRequest(
        data=RoleCreateData(
            attributes=RoleCreateAttributes(
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                modified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                name="developers",
            ),
            relationships=RoleRelationships(
                permissions=RelationshipToPermissions(
                    data=[
                        RelationshipToPermissionData(
                            id="id_example",
                            type=PermissionsType("permissions"),
                        ),
                    ],
                ),
                users=RelationshipToUsers(
                    data=[
                        RelationshipToUserData(
                            id="00000000-0000-0000-0000-000000000000",
                            type=UsersType("users"),
                        ),
                    ],
                ),
            ),
            type=RolesType("roles"),
        ),
    )  # RoleCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create role
        api_response = api_instance.create_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleCreateRequest**](RoleCreateRequest.md)|  |

### Return type

[**RoleCreateResponse**](RoleCreateResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_role**
> delete_role(role_id)

Delete role

Disables a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.

    # example passing only required values which don't have defaults set
    try:
        # Delete role
        api_instance.delete_role(role_id)
    except ApiException as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |

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

# **get_role**
> RoleResponse get_role(role_id)

Get a role

Get a role in the organization specified by the role’s `role_id`.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.

    # example passing only required values which don't have defaults set
    try:
        # Get a role
        api_response = api_instance.get_role(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |

### Return type

[**RoleResponse**](RoleResponse.md)

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

# **list_permissions**
> PermissionsResponse list_permissions()

List permissions

Returns a list of all permissions, including name, description, and ID.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List permissions
        api_response = api_instance.list_permissions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_permissions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_role_permissions**
> PermissionsResponse list_role_permissions(role_id)

List permissions for a role

Returns a list of all permissions for a single role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.

    # example passing only required values which don't have defaults set
    try:
        # List permissions for a role
        api_response = api_instance.list_role_permissions(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |

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

# **list_role_users**
> UsersResponse list_role_users(role_id)

Get all users of a role

Gets all users of a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = "name"  # str | User attribute to order results by. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `email`, `status`. (optional) if omitted the server will use the default value of "name"
    filter = "filter_example"  # str | Filter all users by the given string. Defaults to no filtering. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all users of a role
        api_response = api_instance.list_role_users(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all users of a role
        api_response = api_instance.list_role_users(role_id, page_size=page_size, page_number=page_number, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_role_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| User attribute to order results by. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example &#x60;sort&#x3D;-name&#x60;. Options: &#x60;name&#x60;, &#x60;email&#x60;, &#x60;status&#x60;. | [optional] if omitted the server will use the default value of "name"
 **filter** | **str**| Filter all users by the given string. Defaults to no filtering. | [optional]

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
**403** | Authentication error |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_roles**
> RolesResponse list_roles()

List roles

Returns all roles, including their names and IDs.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    page_size = 10  # int | Size for a given page. (optional) if omitted the server will use the default value of 10
    page_number = 0  # int | Specific page number to return. (optional) if omitted the server will use the default value of 0
    sort = RolesSort("name")  # RolesSort | Sort roles depending on the given field. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example: `sort=-name`. (optional)
    filter = "filter_example"  # str | Filter all roles by the given string. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List roles
        api_response = api_instance.list_roles(page_size=page_size, page_number=page_number, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Size for a given page. | [optional] if omitted the server will use the default value of 10
 **page_number** | **int**| Specific page number to return. | [optional] if omitted the server will use the default value of 0
 **sort** | **RolesSort**| Sort roles depending on the given field. Sort order is **ascending** by default. Sort order is **descending** if the field is prefixed by a negative sign, for example: &#x60;sort&#x3D;-name&#x60;. | [optional]
 **filter** | **str**| Filter all roles by the given string. | [optional]

### Return type

[**RolesResponse**](RolesResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **remove_permission_from_role**
> PermissionsResponse remove_permission_from_role(role_id, body)

Revoke permission

Removes a permission from a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    body = RelationshipToPermission(
        data=RelationshipToPermissionData(
            id="id_example",
            type=PermissionsType("permissions"),
        ),
    )  # RelationshipToPermission | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke permission
        api_response = api_instance.remove_permission_from_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_permission_from_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **body** | [**RelationshipToPermission**](RelationshipToPermission.md)|  |

### Return type

[**PermissionsResponse**](PermissionsResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **remove_user_from_role**
> UsersResponse remove_user_from_role(role_id, body)

Remove a user from a role

Removes a user from a role.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    body = RelationshipToUser(
        data=RelationshipToUserData(
            id="00000000-0000-0000-0000-000000000000",
            type=UsersType("users"),
        ),
    )  # RelationshipToUser | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a user from a role
        api_response = api_instance.remove_user_from_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_user_from_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **body** | [**RelationshipToUser**](RelationshipToUser.md)|  |

### Return type

[**UsersResponse**](UsersResponse.md)

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_role**
> RoleUpdateResponse update_role(role_id, body)

Update a role

Edit a role. Can only be used with application keys belonging to administrators.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    role_id = "role_id_example"  # str | The ID of the role.
    body = RoleUpdateRequest(
        data=RoleUpdateData(
            attributes=RoleUpdateAttributes(
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                modified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                name="name_example",
            ),
            id="00000000-0000-0000-0000-000000000000",
            type=RolesType("roles"),
        ),
    )  # RoleUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a role
        api_response = api_instance.update_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The ID of the role. |
 **body** | [**RoleUpdateRequest**](RoleUpdateRequest.md)|  |

### Return type

[**RoleUpdateResponse**](RoleUpdateResponse.md)

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

