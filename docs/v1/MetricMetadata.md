# MetricMetadata

Object with all metric related metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Metric description. | [optional] 
**integration** | **str** | Name of the integration that sent the metric if applicable. | [optional] [readonly] 
**per_unit** | **str** | Per unit of the metric such as &#x60;second&#x60; in &#x60;bytes per second&#x60;. | [optional] 
**short_name** | **str** | A more human-readable and abbreviated version of the metric name. | [optional] 
**statsd_interval** | **int** | StatsD flush interval of the metric in seconds if applicable. | [optional] 
**type** | **str** | Metric type such as &#x60;gauge&#x60; or &#x60;rate&#x60;. | [optional] 
**unit** | **str** | Primary unit of the metric such as &#x60;byte&#x60; or &#x60;operation&#x60;. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


