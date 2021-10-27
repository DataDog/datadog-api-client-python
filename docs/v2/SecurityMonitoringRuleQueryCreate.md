# SecurityMonitoringRuleQueryCreate

Query for matching rule.

## Properties

| Name                | Type                                                                                    | Description                                                                | Notes      |
| ------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------- |
| **query**           | **str**                                                                                 | Query to run on logs.                                                      |
| **agent_rule**      | [**SecurityMonitoringRuntimeAgentRule**](SecurityMonitoringRuntimeAgentRule.md)         |                                                                            | [optional] |
| **aggregation**     | [**SecurityMonitoringRuleQueryAggregation**](SecurityMonitoringRuleQueryAggregation.md) |                                                                            | [optional] |
| **distinct_fields** | **[str]**                                                                               | Field for which the cardinality is measured. Sent as an array.             | [optional] |
| **group_by_fields** | **[str]**                                                                               | Fields to group by.                                                        | [optional] |
| **metric**          | **str**                                                                                 | The target field to aggregate over when using the sum or max aggregations. | [optional] |
| **name**            | **str**                                                                                 | Name of the query.                                                         | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
