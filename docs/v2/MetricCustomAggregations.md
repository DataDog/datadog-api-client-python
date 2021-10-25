# MetricCustomAggregations

A list of queryable aggregation combinations for a count, rate, or gauge metric. By default, count and rate metrics require the (time: sum, space: sum) aggregation and Gauge metrics require the (time: avg, space: avg) aggregation. Additional time & space combinations are also available:  - time: avg, space: avg - time: avg, space: max - time: avg, space: min - time: avg, space: sum - time: count, space: sum - time: max, space: max - time: min, space: min - time: sum, space: avg - time: sum, space: sum  Can only be applied to metrics that have a `metric_type` of `count`, `rate`, or `gauge`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**[MetricCustomAggregation]**](MetricCustomAggregation.md) | A list of queryable aggregation combinations for a count, rate, or gauge metric. By default, count and rate metrics require the (time: sum, space: sum) aggregation and Gauge metrics require the (time: avg, space: avg) aggregation. Additional time &amp; space combinations are also available:  - time: avg, space: avg - time: avg, space: max - time: avg, space: min - time: avg, space: sum - time: count, space: sum - time: max, space: max - time: min, space: min - time: sum, space: avg - time: sum, space: sum  Can only be applied to metrics that have a &#x60;metric_type&#x60; of &#x60;count&#x60;, &#x60;rate&#x60;, or &#x60;gauge&#x60;. | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


