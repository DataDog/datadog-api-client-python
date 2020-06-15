# logs_index.LogsIndex

Object describing a Datadog Log index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**logs_filter.LogsFilter**](LogsFilter.md) |  | 
**daily_limit** | **int** | The number of log events you can send in this index per day before you are rate-limited. | [optional] [readonly] 
**exclusion_filters** | [**[logs_exclusion.LogsExclusion]**](LogsExclusion.md) | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored. | [optional] 
**is_rate_limited** | **bool** | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. Rate limit is reset every-day at 2pm UTC. | [optional] [readonly] 
**name** | **str** | The name of the index. | [optional] [readonly] 
**num_retention_days** | **int** | The number of days before logs are deleted from this index. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


