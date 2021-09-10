# datadog_api_client.v1.MonitorsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_can_delete_monitor**](MonitorsApi.md#check_can_delete_monitor) | **GET** /api/v1/monitor/can_delete | Check if a monitor can be deleted
[**create_monitor**](MonitorsApi.md#create_monitor) | **POST** /api/v1/monitor | Create a monitor
[**delete_monitor**](MonitorsApi.md#delete_monitor) | **DELETE** /api/v1/monitor/{monitor_id} | Delete a monitor
[**get_monitor**](MonitorsApi.md#get_monitor) | **GET** /api/v1/monitor/{monitor_id} | Get a monitor&#39;s details
[**list_monitors**](MonitorsApi.md#list_monitors) | **GET** /api/v1/monitor | Get all monitor details
[**search_monitor_groups**](MonitorsApi.md#search_monitor_groups) | **GET** /api/v1/monitor/groups/search | Monitors group search
[**search_monitors**](MonitorsApi.md#search_monitors) | **GET** /api/v1/monitor/search | Monitors search
[**update_monitor**](MonitorsApi.md#update_monitor) | **PUT** /api/v1/monitor/{monitor_id} | Edit a monitor
[**validate_monitor**](MonitorsApi.md#validate_monitor) | **POST** /api/v1/monitor/validate | Validate a monitor


# **check_can_delete_monitor**
> CheckCanDeleteMonitorResponse check_can_delete_monitor(monitor_ids)

Check if the given monitors can be deleted.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_ids = [
        1,
    ]  # [int] | The IDs of the monitor to check.

    # example passing only required values which don't have defaults set
    try:
        # Check if a monitor can be deleted
        api_response = api_instance.check_can_delete_monitor(monitor_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->check_can_delete_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_ids** | **[int]**| The IDs of the monitor to check. |

### Return type

[**CheckCanDeleteMonitorResponse**](CheckCanDeleteMonitorResponse.md)

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
**403** | Forbidden |  -  |
**409** | Deletion conflict error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_monitor**
> Monitor create_monitor(body)

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
- metric: `metric alert`
- network: `service check`
- outlier: `query alert`
- process: `service check`
- rum: `rum alert`
- SLO: `slo alert`
- watchdog: `event alert`
- event-v2: `event-v2 alert`
- audit: `audit alert`

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
- `time_aggr` avg, sum, max, min [Learn more](https://docs.datadoghq.com/monitors/monitor_types/#define-the-conditions)
- `time_window` last\_#m (between 1 and 2880 depending on the monitor type), last\_#h (between 1 and 48 depending on the monitor type), or last_#d (1 or 2)
- `timeshift` #m_ago (5, 10, 15, or 30), #h_ago (1, 2, or 4), or 1d_ago

Use this to create an outlier monitor using the following query:
`avg(last_30m):outliers(avg:system.cpu.user{role:es-events-data} by {host}, 'dbscan', 7) > 0`

**Service Check Query**

Example: `"check".over(tags).last(count).by(group).count_by_status()`

- **`check`** name of the check, e.g. `datadog.agent.up`
- **`tags`** one or more quoted tags (comma-separated), or "*". e.g.: `.over("env:prod", "role:db")`; **`over`** cannot be blank.
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

**NOTE** Only available on US1 and EU.

**Event V2 Alert Query**

Example: `events(query).rollup(rollup_method[, measure]).last(time_window) operator #`

- **`query`** The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
- **`rollup_method`** The stats roll-up method - supports `count`, `avg` and `cardinality`.
- **`measure`** For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
- **`time_window`** #m (between 1 and 2880), #h (between 1 and 48).
- **`operator`** `<`, `<=`, `>`, `>=`, `==`, or `!=`.
- **`#`** an integer or decimal number used to set the threshold.

**NOTE** Only available on US1-FED, US3, and in closed beta on EU and US1.

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

**NOTE** Only available on US1-FED and in closed beta on EU, US3, and US1.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    body = Monitor(
        message="message_example",
        name="name_example",
        options=MonitorOptions(
            enable_logs_sample=True,
            escalation_message="none",
            evaluation_delay=1,
            groupby_simple_monitor=True,
            include_tags=True,
            locked=True,
            min_failure_duration=0,
            min_location_failed=1,
            new_group_delay=1,
            new_host_delay=300,
            no_data_timeframe=1,
            notify_audit=False,
            notify_no_data=False,
            renotify_interval=1,
            require_full_window=True,
            silenced={
                "key": 1,
            },
            synthetics_check_id="synthetics_check_id_example",
            threshold_windows=MonitorThresholdWindowOptions(
                recovery_window="recovery_window_example",
                trigger_window="trigger_window_example",
            ),
            thresholds=MonitorThresholds(
                critical=3.14,
                critical_recovery=3.14,
                ok=3.14,
                unknown=3.14,
                warning=3.14,
                warning_recovery=3.14,
            ),
            timeout_h=1,
        ),
        priority=1,
        query="avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        restricted_roles=[
            "restricted_roles_example",
        ],
        tags=[
            "tags_example",
        ],
        type=MonitorType("metric alert"),
    )  # Monitor | Create a monitor request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a monitor
        api_response = api_instance.create_monitor(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->create_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Monitor**](Monitor.md)| Create a monitor request body. |

### Return type

[**Monitor**](Monitor.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_monitor**
> DeletedMonitor delete_monitor(monitor_id)

Delete the specified monitor

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_id = 1  # int | The ID of the monitor.
    force = "false"  # str | Delete the monitor even if it's referenced by other resources (e.g. SLO, composite monitor). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a monitor
        api_response = api_instance.delete_monitor(monitor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->delete_monitor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a monitor
        api_response = api_instance.delete_monitor(monitor_id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->delete_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **int**| The ID of the monitor. |
 **force** | **str**| Delete the monitor even if it&#39;s referenced by other resources (e.g. SLO, composite monitor). | [optional]

### Return type

[**DeletedMonitor**](DeletedMonitor.md)

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
**401** | Authentication error |  -  |
**403** | Forbidden |  -  |
**404** | Item not found error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_monitor**
> Monitor get_monitor(monitor_id)

Get details about the specified monitor from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_id = 1  # int | The ID of the monitor
    group_states = "group_states_example"  # str | When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a monitor's details
        api_response = api_instance.get_monitor(monitor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->get_monitor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a monitor's details
        api_response = api_instance.get_monitor(monitor_id, group_states=group_states)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->get_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **int**| The ID of the monitor |
 **group_states** | **str**| When specified, shows additional information about the group states. Choose one or more from &#x60;all&#x60;, &#x60;alert&#x60;, &#x60;warn&#x60;, and &#x60;no data&#x60;. | [optional]

### Return type

[**Monitor**](Monitor.md)

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
**404** | Monitor Not Found error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_monitors**
> [Monitor] list_monitors()

Get details about the specified monitor from your organization.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    group_states = "alert"  # str | When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`. (optional)
    name = "name_example"  # str | A string to filter monitors by name. (optional)
    tags = "host:host0"  # str | A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. For example, `host:host0`. (optional)
    monitor_tags = "service:my-app"  # str | A comma separated list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. Tags created in the Datadog UI automatically have the service key prepended. For example, `service:my-app`. (optional)
    with_downtimes = True  # bool | If this argument is set to true, then the returned data includes all current downtimes for each monitor. (optional)
    id_offset = 1  # int | Monitor ID offset. (optional)
    page = 0  # int | The page to start paginating from. If this argument is not specified, the request returns all monitors without pagination. (optional)
    page_size = 20  # int | The number of monitors to return per page. If the page argument is not specified, the default behavior returns all monitors without a `page_size` limit. However, if page is specified and `page_size` is not, the argument defaults to 100. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all monitor details
        api_response = api_instance.list_monitors(group_states=group_states, name=name, tags=tags, monitor_tags=monitor_tags, with_downtimes=with_downtimes, id_offset=id_offset, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->list_monitors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_states** | **str**| When specified, shows additional information about the group states. Choose one or more from &#x60;all&#x60;, &#x60;alert&#x60;, &#x60;warn&#x60;, and &#x60;no data&#x60;. | [optional]
 **name** | **str**| A string to filter monitors by name. | [optional]
 **tags** | **str**| A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. For example, &#x60;host:host0&#x60;. | [optional]
 **monitor_tags** | **str**| A comma separated list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. Tags created in the Datadog UI automatically have the service key prepended. For example, &#x60;service:my-app&#x60;. | [optional]
 **with_downtimes** | **bool**| If this argument is set to true, then the returned data includes all current downtimes for each monitor. | [optional]
 **id_offset** | **int**| Monitor ID offset. | [optional]
 **page** | **int**| The page to start paginating from. If this argument is not specified, the request returns all monitors without pagination. | [optional]
 **page_size** | **int**| The number of monitors to return per page. If the page argument is not specified, the default behavior returns all monitors without a &#x60;page_size&#x60; limit. However, if page is specified and &#x60;page_size&#x60; is not, the argument defaults to 100. | [optional]

### Return type

[**[Monitor]**](Monitor.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_monitor_groups**
> MonitorGroupSearchResponse search_monitor_groups()

Search and filter your monitor groups details.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    query = "query_example"  # str | After entering a search query in your [Manage Monitor page][1] use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2] page to learn more.  The query can contain any number of space-separated monitor attributes, for instance `query=\"type:metric status:alert\"`.  [1]: https://app.datadoghq.com/monitors/manage [2]: /monitors/manage_monitor/#find-the-monitors (optional)
    page = 0  # int | Page to start paginating from. (optional) if omitted the server will use the default value of 0
    per_page = 30  # int | Number of monitors to return per page. (optional) if omitted the server will use the default value of 30
    sort = "sort_example"  # str | String for sort order, composed of field and sort order separate by a comma, e.g. `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:  * `name` * `status` * `tags` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Monitors group search
        api_response = api_instance.search_monitor_groups(query=query, page=page, per_page=per_page, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->search_monitor_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| After entering a search query in your [Manage Monitor page][1] use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2] page to learn more.  The query can contain any number of space-separated monitor attributes, for instance &#x60;query&#x3D;\&quot;type:metric status:alert\&quot;&#x60;.  [1]: https://app.datadoghq.com/monitors/manage [2]: /monitors/manage_monitor/#find-the-monitors | [optional]
 **page** | **int**| Page to start paginating from. | [optional] if omitted the server will use the default value of 0
 **per_page** | **int**| Number of monitors to return per page. | [optional] if omitted the server will use the default value of 30
 **sort** | **str**| String for sort order, composed of field and sort order separate by a comma, e.g. &#x60;name,asc&#x60;. Supported sort directions: &#x60;asc&#x60;, &#x60;desc&#x60;. Supported fields:  * &#x60;name&#x60; * &#x60;status&#x60; * &#x60;tags&#x60; | [optional]

### Return type

[**MonitorGroupSearchResponse**](MonitorGroupSearchResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_monitors**
> MonitorSearchResponse search_monitors()

Search and filter your monitors details.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    query = "query_example"  # str | After entering a search query in your [Manage Monitor page][1] use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2] page to learn more.  The query can contain any number of space-separated monitor attributes, for instance `query=\"type:metric status:alert\"`.  [1]: https://app.datadoghq.com/monitors/manage [2]: /monitors/manage_monitor/#find-the-monitors (optional)
    page = 0  # int | Page to start paginating from. (optional) if omitted the server will use the default value of 0
    per_page = 30  # int | Number of monitors to return per page. (optional) if omitted the server will use the default value of 30
    sort = "sort_example"  # str | String for sort order, composed of field and sort order separate by a comma, e.g. `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:  * `name` * `status` * `tags` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Monitors search
        api_response = api_instance.search_monitors(query=query, page=page, per_page=per_page, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->search_monitors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| After entering a search query in your [Manage Monitor page][1] use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2] page to learn more.  The query can contain any number of space-separated monitor attributes, for instance &#x60;query&#x3D;\&quot;type:metric status:alert\&quot;&#x60;.  [1]: https://app.datadoghq.com/monitors/manage [2]: /monitors/manage_monitor/#find-the-monitors | [optional]
 **page** | **int**| Page to start paginating from. | [optional] if omitted the server will use the default value of 0
 **per_page** | **int**| Number of monitors to return per page. | [optional] if omitted the server will use the default value of 30
 **sort** | **str**| String for sort order, composed of field and sort order separate by a comma, e.g. &#x60;name,asc&#x60;. Supported sort directions: &#x60;asc&#x60;, &#x60;desc&#x60;. Supported fields:  * &#x60;name&#x60; * &#x60;status&#x60; * &#x60;tags&#x60; | [optional]

### Return type

[**MonitorSearchResponse**](MonitorSearchResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_monitor**
> Monitor update_monitor(monitor_id, body)

Edit the specified monitor.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_id = 1  # int | The ID of the monitor.
    body = MonitorUpdateRequest(
        message="message_example",
        name="name_example",
        options=MonitorOptions(
            enable_logs_sample=True,
            escalation_message="none",
            evaluation_delay=1,
            groupby_simple_monitor=True,
            include_tags=True,
            locked=True,
            min_failure_duration=0,
            min_location_failed=1,
            new_group_delay=1,
            new_host_delay=300,
            no_data_timeframe=1,
            notify_audit=False,
            notify_no_data=False,
            renotify_interval=1,
            require_full_window=True,
            silenced={
                "key": 1,
            },
            synthetics_check_id="synthetics_check_id_example",
            threshold_windows=MonitorThresholdWindowOptions(
                recovery_window="recovery_window_example",
                trigger_window="trigger_window_example",
            ),
            thresholds=MonitorThresholds(
                critical=3.14,
                critical_recovery=3.14,
                ok=3.14,
                unknown=3.14,
                warning=3.14,
                warning_recovery=3.14,
            ),
            timeout_h=1,
        ),
        priority=1,
        query="query_example",
        restricted_roles=[
            "restricted_roles_example",
        ],
        tags=[
            "tags_example",
        ],
        type=MonitorType("metric alert"),
    )  # MonitorUpdateRequest | Edit a monitor request body.

    # example passing only required values which don't have defaults set
    try:
        # Edit a monitor
        api_response = api_instance.update_monitor(monitor_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->update_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **int**| The ID of the monitor. |
 **body** | [**MonitorUpdateRequest**](MonitorUpdateRequest.md)| Edit a monitor request body. |

### Return type

[**Monitor**](Monitor.md)

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
**401** | Authentication error |  -  |
**403** | Forbidden |  -  |
**404** | Monitor Not Found error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **validate_monitor**
> dict validate_monitor(body)

Validate the monitor provided in the request.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    body = Monitor(
        message="message_example",
        name="name_example",
        options=MonitorOptions(
            enable_logs_sample=True,
            escalation_message="none",
            evaluation_delay=1,
            groupby_simple_monitor=True,
            include_tags=True,
            locked=True,
            min_failure_duration=0,
            min_location_failed=1,
            new_group_delay=1,
            new_host_delay=300,
            no_data_timeframe=1,
            notify_audit=False,
            notify_no_data=False,
            renotify_interval=1,
            require_full_window=True,
            silenced={
                "key": 1,
            },
            synthetics_check_id="synthetics_check_id_example",
            threshold_windows=MonitorThresholdWindowOptions(
                recovery_window="recovery_window_example",
                trigger_window="trigger_window_example",
            ),
            thresholds=MonitorThresholds(
                critical=3.14,
                critical_recovery=3.14,
                ok=3.14,
                unknown=3.14,
                warning=3.14,
                warning_recovery=3.14,
            ),
            timeout_h=1,
        ),
        priority=1,
        query="avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        restricted_roles=[
            "restricted_roles_example",
        ],
        tags=[
            "tags_example",
        ],
        type=MonitorType("metric alert"),
    )  # Monitor | Monitor request object

    # example passing only required values which don't have defaults set
    try:
        # Validate a monitor
        api_response = api_instance.validate_monitor(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->validate_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Monitor**](Monitor.md)| Monitor request object |

### Return type

**dict**

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid JSON |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

