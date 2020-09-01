# MonitorStateGroup

Monitor state for a single group.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_nodata_ts** | **int** | Latest timestamp the monitor was in NO_DATA state. | [optional] 
**last_notified_ts** | **int** | Latest timestamp of the notification sent for this monitor group. | [optional] 
**last_resolved_ts** | **int** | Latest timestamp the monitor group was resolved. | [optional] 
**last_triggered_ts** | **int** | Latest timestamp the monitor group triggered. | [optional] 
**name** | **str** | The name of the monitor. | [optional] 
**status** | [**MonitorOverallStates**](MonitorOverallStates.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


