# ServiceLevelObjectiveQuery

A metric SLI query. **Required if type is `metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.

## Properties

| Name            | Type    | Description                                      | Notes |
| --------------- | ------- | ------------------------------------------------ | ----- |
| **denominator** | **str** | A Datadog metric query for total (valid) events. |
| **numerator**   | **str** | A Datadog metric query for good events.          |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
