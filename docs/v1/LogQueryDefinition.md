# LogQueryDefinition

The log query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute** | [**LogsQueryCompute**](LogsQueryCompute.md) |  | [optional] 
**group_by** | [**[LogQueryDefinitionGroupBy]**](LogQueryDefinitionGroupBy.md) | List of tag prefixes to group by in the case of a cluster check. | [optional] 
**index** | **str** | A coma separated-list of index names. Use \&quot;*\&quot; query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) | [optional] 
**multi_compute** | [**[LogsQueryCompute]**](LogsQueryCompute.md) | This field is mutually exclusive with &#x60;compute&#x60;. | [optional] 
**search** | [**LogQueryDefinitionSearch**](LogQueryDefinitionSearch.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


