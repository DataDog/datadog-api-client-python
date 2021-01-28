# LogsAggregateRequest

The object sent with the request to retrieve a list of logs from your organization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute** | [**[LogsCompute]**](LogsCompute.md) | The list of metrics or timeseries to compute for the retrieved buckets. | [optional] 
**filter** | [**LogsQueryFilter**](LogsQueryFilter.md) |  | [optional] 
**group_by** | [**[LogsGroupBy]**](LogsGroupBy.md) | The rules for the group by | [optional] 
**options** | [**LogsQueryOptions**](LogsQueryOptions.md) |  | [optional] 
**page** | [**LogsAggregateRequestPage**](LogsAggregateRequestPage.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


