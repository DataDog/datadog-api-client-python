# MetricsQueryMetadata

Object containing all metric names returned and their associated metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggr** | **str** | Aggregation type. | [optional] [readonly] 
**display_name** | **str** | Display name of the metric. | [optional] [readonly] 
**end** | **int** | End of the time window, milliseconds since Unix epoch. | [optional] [readonly] 
**expression** | **str** | Metric expression. | [optional] [readonly] 
**interval** | **int** | Number of seconds between data samples. | [optional] [readonly] 
**length** | **int** | Number of data samples. | [optional] [readonly] 
**metric** | **str** | Metric name. | [optional] [readonly] 
**pointlist** | [**[Point]**](Point.md) | List of points of the time series. | [optional] [readonly] 
**query_index** | **int** | The index of the series&#39; query within the request. | [optional] [readonly] 
**scope** | **str** | Metric scope, comma separated list of tags. | [optional] [readonly] 
**start** | **int** | Start of the time window, milliseconds since Unix epoch. | [optional] [readonly] 
**tag_set** | **[str]** | Unique tags identifying this series. | [optional] [readonly] 
**unit** | [**[MetricsQueryUnit]**](MetricsQueryUnit.md) | Detailed information about the metric unit. First element describes the \&quot;primary unit\&quot; (for example, &#x60;bytes&#x60; in &#x60;bytes per second&#x60;), second describes the \&quot;per unit\&quot; (for example, &#x60;second&#x60; in &#x60;bytes per second&#x60;). | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


