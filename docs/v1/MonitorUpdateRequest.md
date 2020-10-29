# MonitorUpdateRequest

Object describing a monitor update request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp of the monitor creation. | [optional] [readonly] 
**creator** | [**Creator**](Creator.md) |  | [optional] 
**deleted** | **datetime, none_type** | Whether or not the monitor is deleted. (Always &#x60;null&#x60;) | [optional] [readonly] 
**id** | **int** | ID of this monitor. | [optional] [readonly] 
**message** | **str** | A message to include with notifications for this monitor. | [optional] 
**modified** | **datetime** | Last timestamp when the monitor was edited. | [optional] [readonly] 
**multi** | **bool** | Whether or not the monitor is broken down on different groups. | [optional] [readonly] 
**name** | **str** | The monitor name. | [optional] 
**options** | [**MonitorOptions**](MonitorOptions.md) |  | [optional] 
**overall_state** | [**MonitorOverallStates**](MonitorOverallStates.md) |  | [optional] 
**priority** | **int** | Integer from 1 (high) to 5 (low) indicating alert severity. | [optional] 
**query** | **str** | The monitor query. | [optional] 
**state** | [**MonitorState**](MonitorState.md) |  | [optional] 
**tags** | **[str]** | Tags associated to your monitor. | [optional] 
**type** | [**MonitorType**](MonitorType.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


