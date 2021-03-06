# QueryValueWidgetRequest

Updated query value widget.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**WidgetAggregator**](WidgetAggregator.md) |  | [optional] 
**apm_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**conditional_formats** | [**[WidgetConditionalFormat]**](WidgetConditionalFormat.md) | List of conditional formats. | [optional] 
**event_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**formulas** | [**[WidgetFormula]**](WidgetFormula.md) | List of formulas that operate on queries. **This feature is currently in beta.** | [optional] 
**log_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**network_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**process_query** | [**ProcessQueryDefinition**](ProcessQueryDefinition.md) |  | [optional] 
**profile_metrics_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**q** | **str** | TODO. | [optional] 
**queries** | [**[FormulaAndFunctionQueryDefinition]**](FormulaAndFunctionQueryDefinition.md) | List of queries that can be returned directly or used in formulas. **This feature is currently in beta.** | [optional] 
**response_format** | [**FormulaAndFunctionResponseFormat**](FormulaAndFunctionResponseFormat.md) |  | [optional] 
**rum_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**security_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


