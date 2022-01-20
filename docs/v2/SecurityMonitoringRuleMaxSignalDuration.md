# SecurityMonitoringRuleMaxSignalDuration

A signal will “close” regardless of the query being matched once the time exceeds the maximum duration. This time is calculated from the first seen timestamp.

## Properties

| Name      | Type    | Description                                                                                                                                                    | Notes                                                                                 |
| --------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **value** | **int** | A signal will “close” regardless of the query being matched once the time exceeds the maximum duration. This time is calculated from the first seen timestamp. | must be one of [0, 60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400, ] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
