# MetricTagConfigurationCreateAttributes

Object containing the definition of a metric tag configuration to be created.

## Properties

| Name                    | Type                                                                          | Description                                                                                                                                                                         | Notes                                                                |
| ----------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **metric_type**         | [**MetricTagConfigurationMetricTypes**](MetricTagConfigurationMetricTypes.md) |                                                                                                                                                                                     |
| **tags**                | **[str]**                                                                     | A list of tag keys that will be queryable for your metric.                                                                                                                          | defaults to []                                                       |
| **aggregations**        | [**MetricCustomAggregations**](MetricCustomAggregations.md)                   |                                                                                                                                                                                     | [optional]                                                           |
| **include_percentiles** | **bool**                                                                      | Toggle to include/exclude percentiles for a distribution metric. Defaults to false. Can only be applied to metrics that have a &#x60;metric_type&#x60; of &#x60;distribution&#x60;. | [optional] if omitted the server will use the default value of False |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
