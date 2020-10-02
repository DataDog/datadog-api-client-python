# TableWidgetRequest

Updated table widget.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**WidgetAggregator**](WidgetAggregator.md) |  | [optional] 
**alias** | **str** | The column name (defaults to the metric name). | [optional] 
**apm_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**apm_stats_query** | [**ApmStatsQueryDefinition**](ApmStatsQueryDefinition.md) |  | [optional] 
**cell_display_mode** | **[str]** | A list of display modes for each table cell. | [optional] 
**conditional_formats** | [**[WidgetConditionalFormat]**](WidgetConditionalFormat.md) | List of conditional formats. | [optional] 
**event_query** | [**EventQueryDefinition**](EventQueryDefinition.md) |  | [optional] 
**limit** | **int** | For metric queries, the number of lines to show in the table. Only one request should have this property. | [optional] 
**log_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**network_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**order** | [**WidgetSort**](WidgetSort.md) |  | [optional] 
**process_query** | [**ProcessQueryDefinition**](ProcessQueryDefinition.md) |  | [optional] 
**q** | **str** | Query definition. | [optional] 
**rum_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**security_query** | [**LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


