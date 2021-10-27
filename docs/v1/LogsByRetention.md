# LogsByRetention

Object containing logs usage data broken down by retention period.

## Properties

| Name               | Type                                                              | Description                                                       | Notes      |
| ------------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ---------- |
| **orgs**           | [**LogsByRetentionOrgs**](LogsByRetentionOrgs.md)                 |                                                                   | [optional] |
| **usage**          | [**[LogsRetentionAggSumUsage]**](LogsRetentionAggSumUsage.md)     | Aggregated index logs usage for each retention period with usage. | [optional] |
| **usage_by_month** | [**LogsByRetentionMonthlyUsage**](LogsByRetentionMonthlyUsage.md) |                                                                   | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
