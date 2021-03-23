# SLOWidgetDefinition

Use the SLO and uptime widget to track your SLOs (Service Level Objectives) and uptime on screenboards and timeboards.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SLOWidgetDefinitionType**](SLOWidgetDefinitionType.md) |  | 
**view_type** | **str** | Type of view displayed by the widget. | defaults to "detail"
**show_error_budget** | **bool** | Defined error budget. | [optional] 
**slo_id** | **str** | ID of the SLO displayed. | [optional] 
**time_windows** | [**[WidgetTimeWindows]**](WidgetTimeWindows.md) | Times being monitored. | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**view_mode** | [**WidgetViewMode**](WidgetViewMode.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


