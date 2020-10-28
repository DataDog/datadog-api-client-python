# MonitorOptions

List of options associated with your monitor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**MonitorOptionsAggregation**](MonitorOptionsAggregation.md) |  | [optional] 
**device_ids** | [**[MonitorDeviceID]**](MonitorDeviceID.md) | IDs of the device the Synthetics monitor is running on. | [optional] [readonly] 
**enable_logs_sample** | **bool** | Whether or not to send a log sample when the log monitor triggers. | [optional] 
**escalation_message** | **str** | A message to include with a re-notification. Supports the &#x60;@username&#x60; notification we allow elsewhere. Not applicable if &#x60;renotify_interval&#x60; is &#x60;None&#x60;. | [optional]  if omitted the server will use the default value of "none"
**evaluation_delay** | **int, none_type** | Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to &#x60;300&#x60; (5min), the timeframe is set to &#x60;last_5m&#x60; and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation. | [optional] 
**include_tags** | **bool** | A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.  **Examples** - If &#x60;True&#x60;, &#x60;[Triggered on {host:h1}] Monitor Title&#x60; - If &#x60;False&#x60;, &#x60;[Triggered] Monitor Title&#x60; | [optional]  if omitted the server will use the default value of True
**locked** | **bool** | Whether or not the monitor is locked (only editable by creator and admins). | [optional] 
**min_failure_duration** | **int, none_type** | How long the test should be in failure before alerting (integer, number of seconds, max 7200). | [optional]  if omitted the server will use the default value of 0
**min_location_failed** | **int, none_type** | The minimum number of locations in failure at the same time during at least one moment in the &#x60;min_failure_duration&#x60; period (&#x60;min_location_failed&#x60; and &#x60;min_failure_duration&#x60; are part of the advanced alerting rules - integer, &gt;&#x3D; 1). | [optional]  if omitted the server will use the default value of 1
**new_host_delay** | **int, none_type** | Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer. | [optional]  if omitted the server will use the default value of 300
**no_data_timeframe** | **int, none_type** | The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for metric alerts, and 24 hours is used for service checks. | [optional] 
**notify_audit** | **bool** | A Boolean indicating whether tagged users is notified on changes to this monitor. | [optional]  if omitted the server will use the default value of False
**notify_no_data** | **bool** | A Boolean indicating whether this monitor notifies when data stops reporting. | [optional]  if omitted the server will use the default value of False
**renotify_interval** | **int, none_type** | The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved. | [optional] 
**require_full_window** | **bool** | A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to &#x60;false&#x60; for sparse metrics, otherwise some evaluations are skipped. Default is false. | [optional] 
**silenced** | **{str: (int, none_type)}** | Information about the downtime applied to the monitor. | [optional] 
**synthetics_check_id** | **str, none_type** | ID of the corresponding Synthetic check. | [optional] 
**threshold_windows** | [**MonitorThresholdWindowOptions**](MonitorThresholdWindowOptions.md) |  | [optional] 
**thresholds** | [**MonitorThresholds**](MonitorThresholds.md) |  | [optional] 
**timeout_h** | **int, none_type** | The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


