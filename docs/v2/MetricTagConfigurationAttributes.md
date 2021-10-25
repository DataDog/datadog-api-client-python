# MetricTagConfigurationAttributes

Object containing the definition of a metric tag configuration attributes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**MetricCustomAggregations**](MetricCustomAggregations.md) |  | [optional] 
**created_at** | **datetime** | Timestamp when the tag configuration was created. | [optional] 
**include_percentiles** | **bool** | Toggle to turn on/off percentile aggregations for distribution metrics. Only present when the &#x60;metric_type&#x60; is &#x60;distribution&#x60;. | [optional] 
**metric_type** | [**MetricTagConfigurationMetricTypes**](MetricTagConfigurationMetricTypes.md) |  | [optional] 
**modified_at** | **datetime** | Timestamp when the tag configuration was last modified. | [optional] 
**tags** | **[str]** | List of tag keys on which to group. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


