# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.slo_list_response import SLOListResponse
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_bulk_delete_response import SLOBulkDeleteResponse
from datadog_api_client.v1.model.slo_bulk_delete import SLOBulkDelete
from datadog_api_client.v1.model.check_can_delete_slo_response import CheckCanDeleteSLOResponse
from datadog_api_client.v1.model.slo_delete_response import SLODeleteResponse
from datadog_api_client.v1.model.slo_response import SLOResponse
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective
from datadog_api_client.v1.model.slo_correction_list_response import SLOCorrectionListResponse
from datadog_api_client.v1.model.slo_history_response import SLOHistoryResponse


class ServiceLevelObjectivesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._check_can_delete_slo_endpoint = _Endpoint(
            settings={
                "response_type": (CheckCanDeleteSLOResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/can_delete",
                "operation_id": "check_can_delete_slo",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "ids": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ids",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._create_slo_endpoint = _Endpoint(
            settings={
                "response_type": (SLOListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo",
                "operation_id": "create_slo",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceLevelObjectiveRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_slo_endpoint = _Endpoint(
            settings={
                "response_type": (SLODeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/{slo_id}",
                "operation_id": "delete_slo",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_id",
                    "location": "path",
                },
                "force": {
                    "openapi_types": (str,),
                    "attribute": "force",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_slo_timeframe_in_bulk_endpoint = _Endpoint(
            settings={
                "response_type": (SLOBulkDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/bulk_delete",
                "operation_id": "delete_slo_timeframe_in_bulk",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SLOBulkDelete,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_slo_endpoint = _Endpoint(
            settings={
                "response_type": (SLOResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/slo/{slo_id}",
                "operation_id": "get_slo",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_id",
                    "location": "path",
                },
                "with_configured_alert_ids": {
                    "openapi_types": (bool,),
                    "attribute": "with_configured_alert_ids",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_slo_corrections_endpoint = _Endpoint(
            settings={
                "response_type": (SLOCorrectionListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/slo/{slo_id}/corrections",
                "operation_id": "get_slo_corrections",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_slo_history_endpoint = _Endpoint(
            settings={
                "response_type": (SLOHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/slo/{slo_id}/history",
                "operation_id": "get_slo_history",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_id",
                    "location": "path",
                },
                "from_ts": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "from_ts",
                    "location": "query",
                },
                "to_ts": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "to_ts",
                    "location": "query",
                },
                "target": {
                    "validation": {
                        "exclusive_maximum": 100,
                        "exclusive_minimum": 0,
                    },
                    "openapi_types": (float,),
                    "attribute": "target",
                    "location": "query",
                },
                "apply_correction": {
                    "openapi_types": (bool,),
                    "attribute": "apply_correction",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_slos_endpoint = _Endpoint(
            settings={
                "response_type": (SLOListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/slo",
                "operation_id": "list_slos",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "ids": {
                    "openapi_types": (str,),
                    "attribute": "ids",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "tags_query": {
                    "openapi_types": (str,),
                    "attribute": "tags_query",
                    "location": "query",
                },
                "metrics_query": {
                    "openapi_types": (str,),
                    "attribute": "metrics_query",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_slo_endpoint = _Endpoint(
            settings={
                "response_type": (SLOListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/slo/{slo_id}",
                "operation_id": "update_slo",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "slo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "slo_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ServiceLevelObjective,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def check_can_delete_slo(self, ids, **kwargs):
        """Check if SLOs can be safely deleted.

        Check if an SLO can be safely deleted. For example,
        assure an SLO can be deleted without disrupting a dashboard.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.check_can_delete_slo(ids, async_req=True)
        >>> result = thread.get()

        :param ids: A comma separated list of the IDs of the service level objectives objects.
        :type ids: str
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
        :rtype: CheckCanDeleteSLOResponse
        """
        kwargs = self._check_can_delete_slo_endpoint.default_arguments(kwargs)
        kwargs["ids"] = ids

        return self._check_can_delete_slo_endpoint.call_with_http_info(**kwargs)

    def create_slo(self, body, **kwargs):
        """Create an SLO object.

        Create a service level objective object.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_slo(body, async_req=True)
        >>> result = thread.get()

        :param body: Service level objective request object.
        :type body: ServiceLevelObjectiveRequest
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
        :rtype: SLOListResponse
        """
        kwargs = self._create_slo_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_slo_endpoint.call_with_http_info(**kwargs)

    def delete_slo(self, slo_id, **kwargs):
        """Delete an SLO.

        Permanently delete the specified service level objective object.

        If an SLO is used in a dashboard, the `DELETE /v1/slo/` endpoint returns
        a 409 conflict error because the SLO is referenced in a dashboard.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_slo(slo_id, async_req=True)
        >>> result = thread.get()

        :param slo_id: The ID of the service level objective.
        :type slo_id: str
        :param force: Delete the monitor even if it's referenced by other resources (for example SLO, composite monitor).
        :type force: str, optional
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
        :rtype: SLODeleteResponse
        """
        kwargs = self._delete_slo_endpoint.default_arguments(kwargs)
        kwargs["slo_id"] = slo_id

        return self._delete_slo_endpoint.call_with_http_info(**kwargs)

    def delete_slo_timeframe_in_bulk(self, body, **kwargs):
        """Bulk Delete SLO Timeframes.

        Delete (or partially delete) multiple service level objective objects.

        This endpoint facilitates deletion of one or more thresholds for one or more
        service level objective objects. If all thresholds are deleted, the service level
        objective object is deleted as well.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_slo_timeframe_in_bulk(body, async_req=True)
        >>> result = thread.get()

        :param body: Delete multiple service level objective objects request body.
        :type body: SLOBulkDelete
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
        :rtype: SLOBulkDeleteResponse
        """
        kwargs = self._delete_slo_timeframe_in_bulk_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_slo_timeframe_in_bulk_endpoint.call_with_http_info(**kwargs)

    def get_slo(self, slo_id, **kwargs):
        """Get an SLO's details.

        Get a service level objective object.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slo(slo_id, async_req=True)
        >>> result = thread.get()

        :param slo_id: The ID of the service level objective object.
        :type slo_id: str
        :param with_configured_alert_ids: Get the IDs of SLO monitors that reference this SLO.
        :type with_configured_alert_ids: bool, optional
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
        :rtype: SLOResponse
        """
        kwargs = self._get_slo_endpoint.default_arguments(kwargs)
        kwargs["slo_id"] = slo_id

        return self._get_slo_endpoint.call_with_http_info(**kwargs)

    def get_slo_corrections(self, slo_id, **kwargs):
        """Get Corrections For an SLO.

        Get corrections applied to an SLO

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slo_corrections(slo_id, async_req=True)
        >>> result = thread.get()

        :param slo_id: The ID of the service level objective object.
        :type slo_id: str
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
        :rtype: SLOCorrectionListResponse
        """
        kwargs = self._get_slo_corrections_endpoint.default_arguments(kwargs)
        kwargs["slo_id"] = slo_id

        return self._get_slo_corrections_endpoint.call_with_http_info(**kwargs)

    def get_slo_history(self, slo_id, from_ts, to_ts, **kwargs):
        """Get an SLO's history.

        Get a specific SLO’s history, regardless of its SLO type.

        The detailed history data is structured according to the source data type.
        For example, metric data is included for event SLOs that use
        the metric source, and monitor SLO types include the monitor transition history.

        **Note:** There are different response formats for event based and time based SLOs.
        Examples of both are shown.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slo_history(slo_id, from_ts, to_ts, async_req=True)
        >>> result = thread.get()

        :param slo_id: The ID of the service level objective object.
        :type slo_id: str
        :param from_ts: The `from` timestamp for the query window in epoch seconds.
        :type from_ts: int
        :param to_ts: The `to` timestamp for the query window in epoch seconds.
        :type to_ts: int
        :param target: The SLO target. If `target` is passed in, the response will include the remaining error budget and a timeframe value of `custom`.
        :type target: float, optional
        :param apply_correction: Defaults to `true`. If any SLO corrections are applied and this parameter is set to `false`,
            then the corrections will not be applied and the SLI values will not be affected.
        :type apply_correction: bool, optional
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
        :rtype: SLOHistoryResponse
        """
        kwargs = self._get_slo_history_endpoint.default_arguments(kwargs)
        kwargs["slo_id"] = slo_id

        kwargs["from_ts"] = from_ts

        kwargs["to_ts"] = to_ts

        return self._get_slo_history_endpoint.call_with_http_info(**kwargs)

    def list_slos(self, **kwargs):
        """Get all SLOs.

        Get a list of service level objective objects for your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_slos(async_req=True)
        >>> result = thread.get()

        :param ids: A comma separated list of the IDs of the service level objectives objects.
        :type ids: str, optional
        :param query: The query string to filter results based on SLO names.
        :type query: str, optional
        :param tags_query: The query string to filter results based on a single SLO tag.
        :type tags_query: str, optional
        :param metrics_query: The query string to filter results based on SLO numerator and denominator.
        :type metrics_query: str, optional
        :param limit: The number of SLOs to return in the response.
        :type limit: int, optional
        :param offset: The specific offset to use as the beginning of the returned response.
        :type offset: int, optional
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
        :rtype: SLOListResponse
        """
        kwargs = self._list_slos_endpoint.default_arguments(kwargs)
        return self._list_slos_endpoint.call_with_http_info(**kwargs)

    def update_slo(self, slo_id, body, **kwargs):
        """Update an SLO.

        Update the specified service level objective object.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_slo(slo_id, body, async_req=True)
        >>> result = thread.get()

        :param slo_id: The ID of the service level objective object.
        :type slo_id: str
        :param body: The edited service level objective request object.
        :type body: ServiceLevelObjective
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
        :rtype: SLOListResponse
        """
        kwargs = self._update_slo_endpoint.default_arguments(kwargs)
        kwargs["slo_id"] = slo_id

        kwargs["body"] = body

        return self._update_slo_endpoint.call_with_http_info(**kwargs)
