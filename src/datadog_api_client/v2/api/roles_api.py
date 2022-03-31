# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.permissions_response import PermissionsResponse
from datadog_api_client.v2.model.roles_response import RolesResponse
from datadog_api_client.v2.model.roles_sort import RolesSort
from datadog_api_client.v2.model.role_create_response import RoleCreateResponse
from datadog_api_client.v2.model.role_create_request import RoleCreateRequest
from datadog_api_client.v2.model.role_response import RoleResponse
from datadog_api_client.v2.model.role_update_response import RoleUpdateResponse
from datadog_api_client.v2.model.role_update_request import RoleUpdateRequest
from datadog_api_client.v2.model.role_clone_request import RoleCloneRequest
from datadog_api_client.v2.model.relationship_to_permission import RelationshipToPermission
from datadog_api_client.v2.model.users_response import UsersResponse
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser


class RolesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._add_permission_to_role_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/permissions",
                "operation_id": "add_permission_to_role",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToPermission,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._add_user_to_role_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/users",
                "operation_id": "add_user_to_role",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToUser,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._clone_role_endpoint = _Endpoint(
            settings={
                "response_type": (RoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/clone",
                "operation_id": "clone_role",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RoleCloneRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_role_endpoint = _Endpoint(
            settings={
                "response_type": (RoleCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles",
                "operation_id": "create_role",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RoleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_role_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}",
                "operation_id": "delete_role",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_role_endpoint = _Endpoint(
            settings={
                "response_type": (RoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}",
                "operation_id": "get_role",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_permissions_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/permissions",
                "operation_id": "list_permissions",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_role_permissions_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/permissions",
                "operation_id": "list_role_permissions",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_roles_endpoint = _Endpoint(
            settings={
                "response_type": (RolesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles",
                "operation_id": "list_roles",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (RolesSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_role_users_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/users",
                "operation_id": "list_role_users",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._remove_permission_from_role_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/permissions",
                "operation_id": "remove_permission_from_role",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToPermission,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._remove_user_from_role_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}/users",
                "operation_id": "remove_user_from_role",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToUser,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_role_endpoint = _Endpoint(
            settings={
                "response_type": (RoleUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/roles/{role_id}",
                "operation_id": "update_role",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RoleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_permission_to_role(self, role_id, body, **kwargs):
        """Grant permission to a role.

        Adds a permission to a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.add_permission_to_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RelationshipToPermission
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PermissionsResponse
        """
        kwargs = self._add_permission_to_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._add_permission_to_role_endpoint.call_with_http_info(**kwargs)

    def add_user_to_role(self, role_id, body, **kwargs):
        """Add a user to a role.

        Adds a user to a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.add_user_to_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RelationshipToUser
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: UsersResponse
        """
        kwargs = self._add_user_to_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._add_user_to_role_endpoint.call_with_http_info(**kwargs)

    def clone_role(self, role_id, body, **kwargs):
        """Create a new role by cloning an existing role.

        Clone an existing role

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.clone_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RoleCloneRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RoleResponse
        """
        kwargs = self._clone_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._clone_role_endpoint.call_with_http_info(**kwargs)

    def create_role(self, body, **kwargs):
        """Create role.

        Create a new role for your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_role(body, async_req=True)
        >>> result = thread.get()

        :type body: RoleCreateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RoleCreateResponse
        """
        kwargs = self._create_role_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_role_endpoint.call_with_http_info(**kwargs)

    def delete_role(self, role_id, **kwargs):
        """Delete role.

        Disables a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_role(role_id, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs = self._delete_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        return self._delete_role_endpoint.call_with_http_info(**kwargs)

    def get_role(self, role_id, **kwargs):
        """Get a role.

        Get a role in the organization specified by the role’s `role_id`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_role(role_id, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RoleResponse
        """
        kwargs = self._get_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        return self._get_role_endpoint.call_with_http_info(**kwargs)

    def list_permissions(self, **kwargs):
        """List permissions.

        Returns a list of all permissions, including name, description, and ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_permissions(async_req=True)
        >>> result = thread.get()

        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PermissionsResponse
        """
        kwargs = self._list_permissions_endpoint.default_arguments(kwargs)
        return self._list_permissions_endpoint.call_with_http_info(**kwargs)

    def list_role_permissions(self, role_id, **kwargs):
        """List permissions for a role.

        Returns a list of all permissions for a single role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_role_permissions(role_id, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PermissionsResponse
        """
        kwargs = self._list_role_permissions_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        return self._list_role_permissions_endpoint.call_with_http_info(**kwargs)

    def list_roles(self, **kwargs):
        """List roles.

        Returns all roles, including their names and their unique identifiers.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_roles(async_req=True)
        >>> result = thread.get()

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Sort roles depending on the given field. Sort order is **ascending** by default.
            Sort order is **descending** if the field is prefixed by a negative sign, for example:
            `sort=-name`.
        :type sort: RolesSort, optional
        :param filter: Filter all roles by the given string.
        :type filter: str, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RolesResponse
        """
        kwargs = self._list_roles_endpoint.default_arguments(kwargs)
        return self._list_roles_endpoint.call_with_http_info(**kwargs)

    def list_role_users(self, role_id, **kwargs):
        """Get all users of a role.

        Gets all users of a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_role_users(role_id, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: User attribute to order results by. Sort order is **ascending** by default.
            Sort order is **descending** if the field is prefixed by a negative sign,
            for example `sort=-name`. Options: `name`, `email`, `status`.
        :type sort: str, optional
        :param filter: Filter all users by the given string. Defaults to no filtering.
        :type filter: str, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: UsersResponse
        """
        kwargs = self._list_role_users_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        return self._list_role_users_endpoint.call_with_http_info(**kwargs)

    def remove_permission_from_role(self, role_id, body, **kwargs):
        """Revoke permission.

        Removes a permission from a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.remove_permission_from_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RelationshipToPermission
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PermissionsResponse
        """
        kwargs = self._remove_permission_from_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._remove_permission_from_role_endpoint.call_with_http_info(**kwargs)

    def remove_user_from_role(self, role_id, body, **kwargs):
        """Remove a user from a role.

        Removes a user from a role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.remove_user_from_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RelationshipToUser
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: UsersResponse
        """
        kwargs = self._remove_user_from_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._remove_user_from_role_endpoint.call_with_http_info(**kwargs)

    def update_role(self, role_id, body, **kwargs):
        """Update a role.

        Edit a role. Can only be used with application keys belonging to administrators.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_role(role_id, body, async_req=True)
        >>> result = thread.get()

        :param role_id: The unique identifier of the role.
        :type role_id: str
        :type body: RoleUpdateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RoleUpdateResponse
        """
        kwargs = self._update_role_endpoint.default_arguments(kwargs)
        kwargs["role_id"] = role_id

        kwargs["body"] = body

        return self._update_role_endpoint.call_with_http_info(**kwargs)
