# UsageBillableSummaryBody

Response with properties for each aggregated usage type.

## Properties

| Name                          | Type         | Description                                             | Notes      |
| ----------------------------- | ------------ | ------------------------------------------------------- | ---------- |
| **account_billable_usage**    | **int**      | The total account usage.                                | [optional] |
| **elapsed_usage_hours**       | **int**      | Elapsed usage hours for some billable product.          | [optional] |
| **first_billable_usage_hour** | **datetime** | The first billable hour for the org.                    | [optional] |
| **last_billable_usage_hour**  | **datetime** | The last billable hour for the org.                     | [optional] |
| **org_billable_usage**        | **int**      | The number of units used within the billable timeframe. | [optional] |
| **percentage_in_account**     | **float**    | The percentage of account usage the org represents.     | [optional] |
| **usage_unit**                | **str**      | Units pertaining to the usage.                          | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
