# service_summary_widget_definition.ServiceSummaryWidgetDefinition

The service summary displays the graphs of a chosen service in your screenboard. Only available on FREE layout dashboards.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **str** | APM environment. | 
**service** | **str** | APM service. | 
**span_name** | **str** | APM span name. | 
**type** | [**service_summary_widget_definition_type.ServiceSummaryWidgetDefinitionType**](ServiceSummaryWidgetDefinitionType.md) |  | 
**display_format** | [**widget_service_summary_display_format.WidgetServiceSummaryDisplayFormat**](WidgetServiceSummaryDisplayFormat.md) |  | [optional] 
**show_breakdown** | **bool** | Whether to show the latency breakdown or not. | [optional] 
**show_distribution** | **bool** | Whether to show the latency distribution or not. | [optional] 
**show_errors** | **bool** | Whether to show the error metrics or not. | [optional] 
**show_hits** | **bool** | Whether to show the hits metrics or not. | [optional] 
**show_latency** | **bool** | Whether to show the latency metrics or not. | [optional] 
**show_resource_list** | **bool** | Whether to show the resource list or not. | [optional] 
**size_format** | [**widget_size_format.WidgetSizeFormat**](WidgetSizeFormat.md) |  | [optional] 
**time** | [**widget_time.WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**widget_text_align.WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


