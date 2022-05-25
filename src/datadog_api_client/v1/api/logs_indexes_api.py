# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.logs_indexes_order import LogsIndexesOrder
from datadog_api_client.v1.model.logs_index_list_response import LogsIndexListResponse
from datadog_api_client.v1.model.logs_index import LogsIndex
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest


class LogsIndexesApi:
    """
    Manage configuration of `log indexes <https://docs.datadoghq.com/logs/indexes/>`_.
    You need an API and application key with Admin rights to interact with this endpoint.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes",
                "operation_id": "create_logs_index",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndex,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes/{name}",
                "operation_id": "get_logs_index",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_index_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/index-order",
                "operation_id": "get_logs_index_order",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_log_indexes_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/indexes",
                "operation_id": "list_log_indexes",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes/{name}",
                "operation_id": "update_logs_index",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndexUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_logs_index_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/index-order",
                "operation_id": "update_logs_index_order",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndexesOrder,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_index(self, body, **kwargs):
        """Create an index.

        Creates a new index. Returns the Index object passed in the request body when the request is successful.

        :param body: Object containing the new index.
        :type body: LogsIndex

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndex
        """
        kwargs["body"] = body

        return self._create_logs_index_endpoint.call_with_http_info(**kwargs)

    def get_logs_index(self, name, **kwargs):
        """Get an index.

        Get one log index from your organization. This endpoint takes no JSON arguments.

        :param name: Name of the log index.
        :type name: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndex
        """
        kwargs["name"] = name

        return self._get_logs_index_endpoint.call_with_http_info(**kwargs)

    def get_logs_index_order(self, **kwargs):
        """Get indexes order.

        Get the current order of your log indexes. This endpoint takes no JSON arguments.


        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndexesOrder
        """
        return self._get_logs_index_order_endpoint.call_with_http_info(**kwargs)

    def list_log_indexes(self, **kwargs):
        """Get all indexes.

        The Index object describes the configuration of a log index.
        This endpoint returns an array of the ``LogIndex`` objects of your organization.


        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndexListResponse
        """
        return self._list_log_indexes_endpoint.call_with_http_info(**kwargs)

    def update_logs_index(self, name, body, **kwargs):
        """Update an index.

        Update an index as identified by its name.
        Returns the Index object passed in the request body when the request is successful.

        Using the ``PUT`` method updates your index’s configuration by **replacing**
        your current configuration with the new one sent to your Datadog organization.

        :param name: Name of the log index.
        :type name: str
        :param body: Object containing the new ``LogsIndexUpdateRequest``.
        :type body: LogsIndexUpdateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndex
        """
        kwargs["name"] = name

        kwargs["body"] = body

        return self._update_logs_index_endpoint.call_with_http_info(**kwargs)

    def update_logs_index_order(self, body, **kwargs):
        """Update indexes order.

        This endpoint updates the index order of your organization.
        It returns the index order object passed in the request body when the request is successful.

        :param body: Object containing the new ordered list of index names
        :type body: LogsIndexesOrder

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: LogsIndexesOrder
        """
        kwargs["body"] = body

        return self._update_logs_index_order_endpoint.call_with_http_info(**kwargs)
