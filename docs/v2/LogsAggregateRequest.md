# logs_aggregate_request.LogsAggregateRequest

The object sent with the request to retrieve a list of logs from your organization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute** | [**[logs_compute.LogsCompute]**](LogsCompute.md) | The list of metrics or timeseries to compute for the retrieved buckets. | [optional] 
**filter** | [**logs_query_filter.LogsQueryFilter**](LogsQueryFilter.md) |  | [optional] 
**group_by** | [**[logs_group_by.LogsGroupBy]**](LogsGroupBy.md) | The rules for the group by | [optional] 
**options** | [**logs_query_options.LogsQueryOptions**](LogsQueryOptions.md) |  | [optional] 
**paging** | [**logs_aggregate_request_paging.LogsAggregateRequestPaging**](LogsAggregateRequestPaging.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


