# ChangeWidgetRequest

Updated change widget.

## Properties

| Name                      | Type                                                                            | Description                                                                                               | Notes      |
| ------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------- |
| **apm_query**             | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **change_type**           | [**WidgetChangeType**](WidgetChangeType.md)                                     |                                                                                                           | [optional] |
| **compare_to**            | [**WidgetCompareTo**](WidgetCompareTo.md)                                       |                                                                                                           | [optional] |
| **event_query**           | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **formulas**              | [**[WidgetFormula]**](WidgetFormula.md)                                         | List of formulas that operate on queries. **This feature is currently in beta.**                          | [optional] |
| **increase_good**         | **bool**                                                                        | Whether to show increase as good.                                                                         | [optional] |
| **log_query**             | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **network_query**         | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **order_by**              | [**WidgetOrderBy**](WidgetOrderBy.md)                                           |                                                                                                           | [optional] |
| **order_dir**             | [**WidgetSort**](WidgetSort.md)                                                 |                                                                                                           | [optional] |
| **process_query**         | [**ProcessQueryDefinition**](ProcessQueryDefinition.md)                         |                                                                                                           | [optional] |
| **profile_metrics_query** | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **q**                     | **str**                                                                         | Query definition.                                                                                         | [optional] |
| **queries**               | [**[FormulaAndFunctionQueryDefinition]**](FormulaAndFunctionQueryDefinition.md) | List of queries that can be returned directly or used in formulas. **This feature is currently in beta.** | [optional] |
| **response_format**       | [**FormulaAndFunctionResponseFormat**](FormulaAndFunctionResponseFormat.md)     |                                                                                                           | [optional] |
| **rum_query**             | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **security_query**        | [**LogQueryDefinition**](LogQueryDefinition.md)                                 |                                                                                                           | [optional] |
| **show_present**          | **bool**                                                                        | Whether to show the present value.                                                                        | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
