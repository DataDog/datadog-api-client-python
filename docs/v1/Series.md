# Series

A metric to submit to Datadog. See [Datadog metrics](https://docs.datadoghq.com/developers/metrics/#custom-metrics-properties).

## Properties

| Name         | Type                    | Description                                                                                                                                                                                                                                        | Notes                                                                  |
| ------------ | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **metric**   | **str**                 | The name of the timeseries.                                                                                                                                                                                                                        |
| **points**   | [**[Point]**](Point.md) | Points relating to a metric. All points must be tuples with timestamp and a scalar value (cannot be a string). Timestamps should be in POSIX time in seconds, and cannot be more than ten minutes in the future or more than one hour in the past. |
| **host**     | **str**                 | The name of the host that produced the metric.                                                                                                                                                                                                     | [optional]                                                             |
| **interval** | **int, none_type**      | If the type of the metric is rate or count, define the corresponding interval.                                                                                                                                                                     | [optional]                                                             |
| **tags**     | **[str]**               | A list of tags associated with the metric.                                                                                                                                                                                                         | [optional]                                                             |
| **type**     | **str**                 | The type of the metric either &#x60;count&#x60;, &#x60;gauge&#x60;, or &#x60;rate&#x60;.                                                                                                                                                           | [optional] if omitted the server will use the default value of "gauge" |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
