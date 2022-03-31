# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.logs_archive_order import LogsArchiveOrder
from datadog_api_client.v2.model.logs_archives import LogsArchives
from datadog_api_client.v2.model.logs_archive import LogsArchive
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequest
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.roles_response import RolesResponse


class LogsArchivesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._add_read_role_to_archive_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}/readers",
                "operation_id": "add_read_role_to_archive",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToRole,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_logs_archive_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchive,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archives",
                "operation_id": "create_logs_archive",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsArchiveCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_logs_archive_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}",
                "operation_id": "delete_logs_archive",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_archive_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchive,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}",
                "operation_id": "get_logs_archive",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_archive_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchiveOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/archive-order",
                "operation_id": "get_logs_archive_order",
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

        self._list_archive_read_roles_endpoint = _Endpoint(
            settings={
                "response_type": (RolesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}/readers",
                "operation_id": "list_archive_read_roles",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_logs_archives_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchives,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/archives",
                "operation_id": "list_logs_archives",
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

        self._remove_role_from_archive_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}/readers",
                "operation_id": "remove_role_from_archive",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToRole,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_logs_archive_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchive,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archives/{archive_id}",
                "operation_id": "update_logs_archive",
                "http_method": "PUT",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "archive_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LogsArchiveCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_logs_archive_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsArchiveOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/archive-order",
                "operation_id": "update_logs_archive_order",
                "http_method": "PUT",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsArchiveOrder,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_read_role_to_archive(self, archive_id, body, **kwargs):
        """Grant role to an archive.

        Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/))

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.add_read_role_to_archive(archive_id, body, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
        :type body: RelationshipToRole
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
        kwargs = self._add_read_role_to_archive_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        kwargs["body"] = body

        return self._add_read_role_to_archive_endpoint.call_with_http_info(**kwargs)

    def create_logs_archive(self, body, **kwargs):
        """Create an archive.

        Create an archive in your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_logs_archive(body, async_req=True)
        >>> result = thread.get()

        :param body: The definition of the new archive.
        :type body: LogsArchiveCreateRequest
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
        :rtype: LogsArchive
        """
        kwargs = self._create_logs_archive_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_logs_archive_endpoint.call_with_http_info(**kwargs)

    def delete_logs_archive(self, archive_id, **kwargs):
        """Delete an archive.

        Delete a given archive from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_logs_archive(archive_id, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
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
        kwargs = self._delete_logs_archive_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        return self._delete_logs_archive_endpoint.call_with_http_info(**kwargs)

    def get_logs_archive(self, archive_id, **kwargs):
        """Get an archive.

        Get a specific archive from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_archive(archive_id, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
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
        :rtype: LogsArchive
        """
        kwargs = self._get_logs_archive_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        return self._get_logs_archive_endpoint.call_with_http_info(**kwargs)

    def get_logs_archive_order(self, **kwargs):
        """Get archive order.

        Get the current order of your archives.
        This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_archive_order(async_req=True)
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
        :rtype: LogsArchiveOrder
        """
        kwargs = self._get_logs_archive_order_endpoint.default_arguments(kwargs)
        return self._get_logs_archive_order_endpoint.call_with_http_info(**kwargs)

    def list_archive_read_roles(self, archive_id, **kwargs):
        """List read roles for an archive.

        Returns all read roles a given archive is restricted to.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_archive_read_roles(archive_id, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
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
        kwargs = self._list_archive_read_roles_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        return self._list_archive_read_roles_endpoint.call_with_http_info(**kwargs)

    def list_logs_archives(self, **kwargs):
        """Get all archives.

        Get the list of configured logs archives with their definitions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_logs_archives(async_req=True)
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
        :rtype: LogsArchives
        """
        kwargs = self._list_logs_archives_endpoint.default_arguments(kwargs)
        return self._list_logs_archives_endpoint.call_with_http_info(**kwargs)

    def remove_role_from_archive(self, archive_id, body, **kwargs):
        """Revoke role from an archive.

        Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/))

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.remove_role_from_archive(archive_id, body, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
        :type body: RelationshipToRole
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
        kwargs = self._remove_role_from_archive_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        kwargs["body"] = body

        return self._remove_role_from_archive_endpoint.call_with_http_info(**kwargs)

    def update_logs_archive(self, archive_id, body, **kwargs):
        """Update an archive.

        Update a given archive configuration.

        **Note**: Using this method updates your archive configuration by **replacing**
        your current configuration with the new one sent to your Datadog organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_archive(archive_id, body, async_req=True)
        >>> result = thread.get()

        :param archive_id: The ID of the archive.
        :type archive_id: str
        :param body: New definition of the archive.
        :type body: LogsArchiveCreateRequest
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
        :rtype: LogsArchive
        """
        kwargs = self._update_logs_archive_endpoint.default_arguments(kwargs)
        kwargs["archive_id"] = archive_id

        kwargs["body"] = body

        return self._update_logs_archive_endpoint.call_with_http_info(**kwargs)

    def update_logs_archive_order(self, body, **kwargs):
        """Update archive order.

        Update the order of your archives. Since logs are processed sequentially, reordering an archive may change
        the structure and content of the data processed by other archives.

        **Note**: Using the `PUT` method updates your archive's order by replacing the current order
        with the new one.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_archive_order(body, async_req=True)
        >>> result = thread.get()

        :param body: An object containing the new ordered list of archive IDs.
        :type body: LogsArchiveOrder
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
        :rtype: LogsArchiveOrder
        """
        kwargs = self._update_logs_archive_order_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._update_logs_archive_order_endpoint.call_with_http_info(**kwargs)
