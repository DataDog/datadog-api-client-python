# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.check_can_delete_monitor_response import CheckCanDeleteMonitorResponse
from datadog_api_client.v1.model.monitor_group_search_response import MonitorGroupSearchResponse
from datadog_api_client.v1.model.monitor_search_response import MonitorSearchResponse
from datadog_api_client.v1.model.deleted_monitor import DeletedMonitor
from datadog_api_client.v1.model.monitor_update_request import MonitorUpdateRequest


class MonitorsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._check_can_delete_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (CheckCanDeleteMonitorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/can_delete",
                "operation_id": "check_can_delete_monitor",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_ids": {
                    "required": True,
                    "openapi_types": ([int],),
                    "attribute": "monitor_ids",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._create_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (Monitor,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor",
                "operation_id": "create_monitor",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Monitor,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (DeletedMonitor,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}",
                "operation_id": "delete_monitor",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
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

        self._get_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (Monitor,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}",
                "operation_id": "get_monitor",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "group_states": {
                    "openapi_types": (str,),
                    "attribute": "group_states",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_monitors_endpoint = _Endpoint(
            settings={
                "response_type": ([Monitor],),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor",
                "operation_id": "list_monitors",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "group_states": {
                    "openapi_types": (str,),
                    "attribute": "group_states",
                    "location": "query",
                },
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "monitor_tags": {
                    "openapi_types": (str,),
                    "attribute": "monitor_tags",
                    "location": "query",
                },
                "with_downtimes": {
                    "openapi_types": (bool,),
                    "attribute": "with_downtimes",
                    "location": "query",
                },
                "id_offset": {
                    "openapi_types": (int,),
                    "attribute": "id_offset",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._search_monitor_groups_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorGroupSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/groups/search",
                "operation_id": "search_monitor_groups",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "per_page": {
                    "openapi_types": (int,),
                    "attribute": "per_page",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._search_monitors_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/search",
                "operation_id": "search_monitors",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "per_page": {
                    "openapi_types": (int,),
                    "attribute": "per_page",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (Monitor,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}",
                "operation_id": "update_monitor",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MonitorUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_existing_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}/validate",
                "operation_id": "validate_existing_monitor",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Monitor,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/validate",
                "operation_id": "validate_monitor",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Monitor,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def check_can_delete_monitor(self, monitor_ids, **kwargs):
        """Check if a monitor can be deleted.

        Check if the given monitors can be deleted.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.check_can_delete_monitor(monitor_ids, async_req=True)
        >>> result = thread.get()

        :param monitor_ids: The IDs of the monitor to check.
        :type monitor_ids: [int]
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
        :rtype: CheckCanDeleteMonitorResponse
        """
        kwargs = self._check_can_delete_monitor_endpoint.default_arguments(kwargs)
        kwargs["monitor_ids"] = monitor_ids

        return self._check_can_delete_monitor_endpoint.call_with_http_info(**kwargs)

    def create_monitor(self, body, **kwargs):
        """Create a monitor.

        Create a monitor using the specified options.

        #### Monitor Types

        The type of monitor chosen from:

        - anomaly: `query alert`
        - APM: `query alert` or `trace-analytics alert`
        - composite: `composite`
        - custom: `service check`
        - event: `event alert`
        - forecast: `query alert`
        - host: `service check`
        - integration: `query alert` or `service check`
        - live process: `process alert`
        - logs: `log alert`
        - metric: `query alert`
        - network: `service check`
        - outlier: `query alert`
        - process: `service check`
        - rum: `rum alert`
        - SLO: `slo alert`
        - watchdog: `event alert`
        - event-v2: `event-v2 alert`
        - audit: `audit alert`
        - error-tracking: `error-tracking alert`

        #### Query Types

        **Metric Alert Query**

        Example: `time_aggr(time_window):space_aggr:metric{tags} [by {key}] operator #`

        - `time_aggr`: avg, sum, max, min, change, or pct_change
        - `time_window`: `last_#m` (with `#` between 1 and 10080 depending on the monitor type) or `last_#h`(with `#` between 1 and 168 depending on the monitor type) or `last_1d`, or `last_1w`
        - `space_aggr`: avg, sum, min, or max
        - `tags`: one or more tags (comma-separated), or *
        - `key`: a 'key' in key:value tag syntax; defines a separate alert for each tag in the group (multi-alert)
        - `operator`: <, <=, >, >=, ==, or !=
        - `#`: an integer or decimal number used to set the threshold

        If you are using the `_change_` or `_pct_change_` time aggregator, instead use `change_aggr(time_aggr(time_window),
        timeshift):space_aggr:metric{tags} [by {key}] operator #` with:

        - `change_aggr` change, pct_change
        - `time_aggr` avg, sum, max, min [Learn more](https://docs.datadoghq.com/monitors/create/types/#define-the-conditions)
        - `time_window` last\\_#m (between 1 and 2880 depending on the monitor type), last\\_#h (between 1 and 48 depending on the monitor type), or last_#d (1 or 2)
        - `timeshift` #m_ago (5, 10, 15, or 30), #h_ago (1, 2, or 4), or 1d_ago

        Use this to create an outlier monitor using the following query:
        `avg(last_30m):outliers(avg:system.cpu.user{role:es-events-data} by {host}, 'dbscan', 7) > 0`

        **Service Check Query**

        Example: `"check".over(tags).last(count).by(group).count_by_status()`

        - **`check`** name of the check, for example `datadog.agent.up`
        - **`tags`** one or more quoted tags (comma-separated), or "*". for example: `.over("env:prod", "role:db")`; **`over`** cannot be blank.
        - **`count`** must be at greater than or equal to your max threshold (defined in the `options`). It is limited to 100.
        For example, if you've specified to notify on 1 critical, 3 ok, and 2 warn statuses, `count` should be at least 3.
        - **`group`** must be specified for check monitors. Per-check grouping is already explicitly known for some service checks.
        For example, Postgres integration monitors are tagged by `db`, `host`, and `port`, and Network monitors by `host`, `instance`, and `url`. See [Service Checks](https://docs.datadoghq.com/api/latest/service-checks/) documentation for more information.

        **Event Alert Query**

        Example: `events('sources:nagios status:error,warning priority:normal tags: "string query"').rollup("count").last("1h")"`

        - **`event`**, the event query string:
        - **`string_query`** free text query to match against event title and text.
        - **`sources`** event sources (comma-separated).
        - **`status`** event statuses (comma-separated). Valid options: error, warn, and info.
        - **`priority`** event priorities (comma-separated). Valid options: low, normal, all.
        - **`host`** event reporting host (comma-separated).
        - **`tags`** event tags (comma-separated).
        - **`excluded_tags`** excluded event tags (comma-separated).
        - **`rollup`** the stats roll-up method. `count` is the only supported method now.
        - **`last`** the timeframe to roll up the counts. Examples: 45m, 4h. Supported timeframes: m, h and d. This value should not exceed 48 hours.

        **NOTE** The Event Alert Query is being deprecated and replaced by the Event V2 Alert Query. For more information, see the [Event Migration guide](https://docs.datadoghq.com/events/guides/migrating_to_new_events_features/).

        **Event V2 Alert Query**

        Example: `events(query).rollup(rollup_method[, measure]).last(time_window) operator #`

        - **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
        - **`rollup_method`** The stats roll-up method - supports `count`, `avg` and `cardinality`.
        - **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
        - **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
        - **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
        - **`#`** an integer or decimal number used to set the threshold.

        **Process Alert Query**

        Example: `processes(search).over(tags).rollup('count').last(timeframe) operator #`

        - **`search`** free text search string for querying processes.
        Matching processes match results on the [Live Processes](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows) page.
        - **`tags`** one or more tags (comma-separated)
        - **`timeframe`** the timeframe to roll up the counts. Examples: 10m, 4h. Supported timeframes: s, m, h and d
        - **`operator`** <, <=, >, >=, ==, or !=
        - **`#`** an integer or decimal number used to set the threshold

        **Logs Alert Query**

        Example: `logs(query).index(index_name).rollup(rollup_method[, measure]).last(time_window) operator #`

        - **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
        - **`index_name`** For multi-index organizations, the log index in which the request is performed.
        - **`rollup_method`** The stats roll-up method - supports `count`, `avg` and `cardinality`.
        - **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
        - **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
        - **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
        - **`#`** an integer or decimal number used to set the threshold.

        **Composite Query**

        Example: `12345 && 67890`, where `12345` and `67890` are the IDs of non-composite monitors

        * **`name`** [*required*, *default* = **dynamic, based on query**]: The name of the alert.
        * **`message`** [*required*, *default* = **dynamic, based on query**]: A message to include with notifications for this monitor.
        Email notifications can be sent to specific users by using the same '@username' notation as events.
        * **`tags`** [*optional*, *default* = **empty list**]: A list of tags to associate with your monitor.
        When getting all monitor details via the API, use the `monitor_tags` argument to filter results by these tags.
        It is only available via the API and isn't visible or editable in the Datadog UI.

        **SLO Alert Query**

        Example: `error_budget("slo_id").over("time_window") operator #`

        - **`slo_id`**: The alphanumeric SLO ID of the SLO you are configuring the alert for.
        - **`time_window`**: The time window of the SLO target you wish to alert on. Valid options: `7d`, `30d`, `90d`.
        - **`operator`**: `>=` or `>`

        **Audit Alert Query**

        Example: `audits(query).rollup(rollup_method[, measure]).last(time_window) operator #`

        - **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
        - **`rollup_method`** The stats roll-up method - supports `count`, `avg` and `cardinality`.
        - **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
        - **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
        - **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
        - **`#`** an integer or decimal number used to set the threshold.

        **NOTE** Only available on US1-FED and in closed beta on US1, EU, US3, and US5.

        **CI Pipelines Alert Query**

        Example: `ci-pipelines(query).rollup(rollup_method[, measure]).last(time_window) operator #`

        - **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
        - **`rollup_method`** The stats roll-up method - supports `count`, `avg`, and `cardinality`.
        - **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
        - **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
        - **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
        - **`#`** an integer or decimal number used to set the threshold.

        **NOTE** CI Pipeline monitors are in alpha on US1, EU, US3 and US5.

        **Error Tracking Alert Query**

        Example(RUM): `error-tracking-rum(query).rollup(rollup_method[, measure]).last(time_window) operator #`
        Example(APM Traces): `error-tracking-traces(query).rollup(rollup_method[, measure]).last(time_window) operator #`

        - **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
        - **`rollup_method`** The stats roll-up method - supports `count`, `avg`, and `cardinality`.
        - **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
        - **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
        - **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
        - **`#`** an integer or decimal number used to set the threshold.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_monitor(body, async_req=True)
        >>> result = thread.get()

        :param body: Create a monitor request body.
        :type body: Monitor
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
        :rtype: Monitor
        """
        kwargs = self._create_monitor_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_monitor_endpoint.call_with_http_info(**kwargs)

    def delete_monitor(self, monitor_id, **kwargs):
        """Delete a monitor.

        Delete the specified monitor

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_monitor(monitor_id, async_req=True)
        >>> result = thread.get()

        :param monitor_id: The ID of the monitor.
        :type monitor_id: int
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
        :rtype: DeletedMonitor
        """
        kwargs = self._delete_monitor_endpoint.default_arguments(kwargs)
        kwargs["monitor_id"] = monitor_id

        return self._delete_monitor_endpoint.call_with_http_info(**kwargs)

    def get_monitor(self, monitor_id, **kwargs):
        """Get a monitor's details.

        Get details about the specified monitor from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_monitor(monitor_id, async_req=True)
        >>> result = thread.get()

        :param monitor_id: The ID of the monitor
        :type monitor_id: int
        :param group_states: When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`.
        :type group_states: str, optional
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
        :rtype: Monitor
        """
        kwargs = self._get_monitor_endpoint.default_arguments(kwargs)
        kwargs["monitor_id"] = monitor_id

        return self._get_monitor_endpoint.call_with_http_info(**kwargs)

    def list_monitors(self, **kwargs):
        """Get all monitor details.

        Get details about the specified monitor from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_monitors(async_req=True)
        >>> result = thread.get()

        :param group_states: When specified, shows additional information about the group states.
            Choose one or more from `all`, `alert`, `warn`, and `no data`.
        :type group_states: str, optional
        :param name: A string to filter monitors by name.
        :type name: str, optional
        :param tags: A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope.
            For example, `host:host0`.
        :type tags: str, optional
        :param monitor_tags: A comma separated list indicating what service and/or custom tags, if any, should be used to filter the list of monitors.
            Tags created in the Datadog UI automatically have the service key prepended. For example, `service:my-app`.
        :type monitor_tags: str, optional
        :param with_downtimes: If this argument is set to true, then the returned data includes all current active downtimes for each monitor.
        :type with_downtimes: bool, optional
        :param id_offset: Use this parameter for paginating through large sets of monitors. Start with a value of zero, make a request, set the value to the last ID of result set, and then repeat until the response is empty.
        :type id_offset: int, optional
        :param page: The page to start paginating from. If this argument is not specified, the request returns all monitors without pagination.
        :type page: int, optional
        :param page_size: The number of monitors to return per page. If the page argument is not specified, the default behavior returns all monitors without a `page_size` limit. However, if page is specified and `page_size` is not, the argument defaults to 100.
        :type page_size: int, optional
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
        :rtype: [Monitor]
        """
        kwargs = self._list_monitors_endpoint.default_arguments(kwargs)
        return self._list_monitors_endpoint.call_with_http_info(**kwargs)

    def search_monitor_groups(self, **kwargs):
        """Monitors group search.

        Search and filter your monitor groups details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.search_monitor_groups(async_req=True)
        >>> result = thread.get()

        :param query: After entering a search query in your [Manage Monitor page][1] use the query parameter value in the
            URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2]
            page to learn more.

            The query can contain any number of space-separated monitor attributes, for instance `query="type:metric status:alert"`.

            [1]: https://app.datadoghq.com/monitors/manage
            [2]: /monitors/manage/#find-the-monitors
        :type query: str, optional
        :param page: Page to start paginating from.
        :type page: int, optional
        :param per_page: Number of monitors to return per page.
        :type per_page: int, optional
        :param sort: String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:

            * `name`
            * `status`
            * `tags`
        :type sort: str, optional
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
        :rtype: MonitorGroupSearchResponse
        """
        kwargs = self._search_monitor_groups_endpoint.default_arguments(kwargs)
        return self._search_monitor_groups_endpoint.call_with_http_info(**kwargs)

    def search_monitors(self, **kwargs):
        """Monitors search.

        Search and filter your monitors details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.search_monitors(async_req=True)
        >>> result = thread.get()

        :param query: After entering a search query in your [Manage Monitor page][1] use the query parameter value in the
            URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2]
            page to learn more.

            The query can contain any number of space-separated monitor attributes, for instance `query="type:metric status:alert"`.

            [1]: https://app.datadoghq.com/monitors/manage
            [2]: /monitors/manage/#find-the-monitors
        :type query: str, optional
        :param page: Page to start paginating from.
        :type page: int, optional
        :param per_page: Number of monitors to return per page.
        :type per_page: int, optional
        :param sort: String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:

            * `name`
            * `status`
            * `tags`
        :type sort: str, optional
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
        :rtype: MonitorSearchResponse
        """
        kwargs = self._search_monitors_endpoint.default_arguments(kwargs)
        return self._search_monitors_endpoint.call_with_http_info(**kwargs)

    def update_monitor(self, monitor_id, body, **kwargs):
        """Edit a monitor.

        Edit the specified monitor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_monitor(monitor_id, body, async_req=True)
        >>> result = thread.get()

        :param monitor_id: The ID of the monitor.
        :type monitor_id: int
        :param body: Edit a monitor request body.
        :type body: MonitorUpdateRequest
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
        :rtype: Monitor
        """
        kwargs = self._update_monitor_endpoint.default_arguments(kwargs)
        kwargs["monitor_id"] = monitor_id

        kwargs["body"] = body

        return self._update_monitor_endpoint.call_with_http_info(**kwargs)

    def validate_existing_monitor(self, monitor_id, body, **kwargs):
        """Validate an existing monitor.

        Validate the monitor provided in the request.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.validate_existing_monitor(monitor_id, body, async_req=True)
        >>> result = thread.get()

        :param monitor_id: The ID of the monitor
        :type monitor_id: int
        :param body: Monitor request object
        :type body: Monitor
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
        :rtype: dict
        """
        kwargs = self._validate_existing_monitor_endpoint.default_arguments(kwargs)
        kwargs["monitor_id"] = monitor_id

        kwargs["body"] = body

        return self._validate_existing_monitor_endpoint.call_with_http_info(**kwargs)

    def validate_monitor(self, body, **kwargs):
        """Validate a monitor.

        Validate the monitor provided in the request.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.validate_monitor(body, async_req=True)
        >>> result = thread.get()

        :param body: Monitor request object
        :type body: Monitor
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
        :rtype: dict
        """
        kwargs = self._validate_monitor_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._validate_monitor_endpoint.call_with_http_info(**kwargs)
