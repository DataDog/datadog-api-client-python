# SLOHistoryMetricsSeriesMetadata

Query metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggr** | **str** | Query aggregator function. | [optional] 
**expression** | **str** | Query expression. | [optional] 
**metric** | **str** | Query metric used. | [optional] 
**query_index** | **int** | Query index from original combined query. | [optional] 
**scope** | **str** | Query scope. | [optional] 
**unit** | [**[SLOHistoryMetricsSeriesMetadataUnit], none_type**](SLOHistoryMetricsSeriesMetadataUnit.md) | An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


