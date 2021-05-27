# MonitorGroupSearchResult

A single monitor group search result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The name of the group. | [optional] [readonly] 
**group_tags** | **[str]** | The list of tags of the monitor group. | [optional] [readonly] 
**last_nodata_ts** | **int** | Latest timestamp the monitor group was in NO_DATA state. | [optional] [readonly] 
**last_triggered_ts** | **int, none_type** | Latest timestamp the monitor group triggered. | [optional] [readonly] 
**monitor_id** | **int** | The ID of the monitor. | [optional] [readonly] 
**monitor_name** | **str** | The name of the monitor. | [optional] [readonly] 
**status** | [**MonitorOverallStates**](MonitorOverallStates.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


