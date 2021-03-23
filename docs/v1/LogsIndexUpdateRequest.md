# LogsIndexUpdateRequest

Object for updating a Datadog Log index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**LogsFilter**](LogsFilter.md) |  | 
**daily_limit** | **int** | The number of log events you can send in this index per day before you are rate-limited. | [optional] 
**disable_daily_limit** | **bool** | If true, sets the &#x60;daily_limit&#x60; value to null and the index is not limited on a daily basis (any specified &#x60;daily_limit&#x60; value in the request is ignored). If false or omitted, the index&#39;s current &#x60;daily_limit&#x60; is maintained. | [optional] 
**exclusion_filters** | [**[LogsExclusion]**](LogsExclusion.md) | An array of exclusion objects. The logs are tested against the query of each filter, following the order of the array. Only the first matching active exclusion matters, others (if any) are ignored. | [optional] 
**num_retention_days** | **int** | The number of days before logs are deleted from this index. Available values depend on retention plans specified in your organization&#39;s contract/subscriptions.  **Note:** Changing the retention for an index adjusts the length of retention for all logs already in this index. It may also affect billing. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


