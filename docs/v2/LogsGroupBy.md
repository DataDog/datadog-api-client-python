# logs_group_by.LogsGroupBy

A group by rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet** | **str** | The name of the facet to use (required) | 
**histogram** | [**logs_group_by_histogram.LogsGroupByHistogram**](LogsGroupByHistogram.md) |  | [optional] 
**limit** | **int** | The maximum buckets to return for this group by | [optional]  if omitted the server will use the default value of 10
**missing** | [**logs_group_by_missing.LogsGroupByMissing**](LogsGroupByMissing.md) |  | [optional] 
**sort** | [**logs_aggregate_sort.LogsAggregateSort**](LogsAggregateSort.md) |  | [optional] 
**total** | [**logs_group_by_total.LogsGroupByTotal**](LogsGroupByTotal.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


