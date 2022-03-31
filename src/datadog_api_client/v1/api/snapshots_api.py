# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.graph_snapshot import GraphSnapshot


class SnapshotsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._get_graph_snapshot_endpoint = _Endpoint(
            settings={
                "response_type": (GraphSnapshot,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/graph/snapshot",
                "operation_id": "get_graph_snapshot",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "metric_query": {
                    "openapi_types": (str,),
                    "attribute": "metric_query",
                    "location": "query",
                },
                "start": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "start",
                    "location": "query",
                },
                "end": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "end",
                    "location": "query",
                },
                "event_query": {
                    "openapi_types": (str,),
                    "attribute": "event_query",
                    "location": "query",
                },
                "graph_def": {
                    "openapi_types": (str,),
                    "attribute": "graph_def",
                    "location": "query",
                },
                "title": {
                    "openapi_types": (str,),
                    "attribute": "title",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_graph_snapshot(self, start, end, **kwargs):
        """Take graph snapshots.

        Take graph snapshots.
        **Note**: When a snapshot is created, there is some delay before it is available.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_graph_snapshot(start, end, async_req=True)
        >>> result = thread.get()

        :param start: The POSIX timestamp of the start of the query.
        :type start: int
        :param end: The POSIX timestamp of the end of the query.
        :type end: int
        :param metric_query: The metric query.
        :type metric_query: str, optional
        :param event_query: A query that adds event bands to the graph.
        :type event_query: str, optional
        :param graph_def: A JSON document defining the graph. `graph_def` can be used instead of `metric_query`.
            The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar)
            and should be formatted to a single line then URL encoded.
        :type graph_def: str, optional
        :param title: A title for the graph. If no title is specified, the graph does not have a title.
        :type title: str, optional
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
        :rtype: GraphSnapshot
        """
        kwargs = self._get_graph_snapshot_endpoint.default_arguments(kwargs)
        kwargs["start"] = start

        kwargs["end"] = end

        return self._get_graph_snapshot_endpoint.call_with_http_info(**kwargs)
