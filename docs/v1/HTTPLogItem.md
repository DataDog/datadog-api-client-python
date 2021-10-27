# HTTPLogItem

Logs that are sent over HTTP.

## Properties

| Name         | Type    | Description                                                                                                                                                                                                                                                                                                              | Notes      |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **ddsource** | **str** | The integration name associated with your log: the technology from which the log originated. When it matches an integration name, Datadog automatically installs the corresponding parsers and facets. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                   | [optional] |
| **ddtags**   | **str** | Tags associated with your logs.                                                                                                                                                                                                                                                                                          | [optional] |
| **hostname** | **str** | The name of the originating host of the log.                                                                                                                                                                                                                                                                             | [optional] |
| **message**  | **str** | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. | [optional] |
| **service**  | **str** | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products. See [reserved attributes](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes).                                              | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
