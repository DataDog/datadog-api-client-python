# MonitorSummaryWidgetDefinition

The monitor summary widget displays a summary view of all your Datadog monitors, or a subset based on a query. Only available on FREE layout dashboards.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Query to filter the monitors with. | 
**type** | [**MonitorSummaryWidgetDefinitionType**](MonitorSummaryWidgetDefinitionType.md) |  | 
**color_preference** | [**WidgetColorPreference**](WidgetColorPreference.md) |  | [optional] 
**count** | **int** | The number of monitors to display. | [optional] 
**display_format** | [**WidgetMonitorSummaryDisplayFormat**](WidgetMonitorSummaryDisplayFormat.md) |  | [optional] 
**hide_zero_counts** | **bool** | Whether to show counts of 0 or not. | [optional] 
**show_last_triggered** | **bool** | Whether to show the time that has elapsed since the monitor/group triggered. | [optional] 
**sort** | [**WidgetMonitorSummarySort**](WidgetMonitorSummarySort.md) |  | [optional] 
**start** | **int** | The start of the list. Typically 0. | [optional] 
**summary_type** | [**WidgetSummaryType**](WidgetSummaryType.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


