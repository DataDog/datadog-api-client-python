# table_widget_request.TableWidgetRequest

Updated table widget.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**widget_aggregator.WidgetAggregator**](WidgetAggregator.md) |  | [optional] 
**alias** | **str** | The column name (defaults to the metric name). | [optional] 
**apm_query** | [**log_query_definition.LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**apm_resources_query** | [**apm_resources_query_definition.ApmResourcesQueryDefinition**](ApmResourcesQueryDefinition.md) |  | [optional] 
**conditional_formats** | [**[widget_conditional_format.WidgetConditionalFormat]**](WidgetConditionalFormat.md) | List of conditional formats. | [optional] 
**event_query** | [**event_query_definition.EventQueryDefinition**](EventQueryDefinition.md) |  | [optional] 
**limit** | **int** | For metric queries, the number of lines to show in the table. Only one request should have this property. | [optional] 
**log_query** | [**log_query_definition.LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**network_query** | [**log_query_definition.LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**order** | [**widget_sort.WidgetSort**](WidgetSort.md) |  | [optional] 
**process_query** | [**process_query_definition.ProcessQueryDefinition**](ProcessQueryDefinition.md) |  | [optional] 
**q** | **str** | Query definition. | [optional] 
**rum_query** | [**log_query_definition.LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 
**security_query** | [**log_query_definition.LogQueryDefinition**](LogQueryDefinition.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


