# MetricTagConfigurationUpdateAttributes

Object containing the definition of a metric tag configuration to be updated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**MetricCustomAggregations**](MetricCustomAggregations.md) |  | [optional] 
**include_percentiles** | **bool** | Toggle to include/exclude percentiles for a distribution metric. Defaults to false. Can only be applied to metrics that have a &#x60;metric_type&#x60; of &#x60;distribution&#x60;. | [optional]  if omitted the server will use the default value of False
**tags** | **[str]** | A list of tag keys that will be queryable for your metric. | [optional]  if omitted the server will use the default value of []

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


