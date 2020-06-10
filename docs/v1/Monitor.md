# monitor.Monitor

Object describing a monitor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp of the monitor creation. | [optional] [readonly] 
**creator** | [**creator.Creator**](Creator.md) |  | [optional] 
**deleted** | **datetime, none_type** | Whether or not the monitor is deleted. (Always &#x60;null&#x60;) | [optional] [readonly] 
**id** | **int** | ID of this monitor. | [optional] [readonly] 
**message** | **str** | A message to include with notifications for this monitor. | [optional] 
**modified** | **datetime** | Last timestamp when the monitor was edited. | [optional] [readonly] 
**multi** | **bool** | Whether or not the monitor is broken down on different groups. | [optional] [readonly] 
**name** | **str** | The monitor name. | [optional] 
**options** | [**monitor_options.MonitorOptions**](MonitorOptions.md) |  | [optional] 
**overall_state** | [**monitor_overall_states.MonitorOverallStates**](MonitorOverallStates.md) |  | [optional] 
**query** | **str** | The monitor query. | [optional] 
**state** | [**monitor_state.MonitorState**](MonitorState.md) |  | [optional] 
**tags** | **[str]** | Tags associated to your monitor. | [optional] 
**type** | [**monitor_type.MonitorType**](MonitorType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


