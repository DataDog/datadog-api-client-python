# heat_map_widget_definition.HeatMapWidgetDefinition

The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[heat_map_widget_request.HeatMapWidgetRequest]**](HeatMapWidgetRequest.md) | List of widget types. | 
**type** | [**heat_map_widget_definition_type.HeatMapWidgetDefinitionType**](HeatMapWidgetDefinitionType.md) |  | 
**events** | [**[widget_event.WidgetEvent]**](WidgetEvent.md) | List of widget events. | [optional] 
**legend_size** | [**widget_legend_size.WidgetLegendSize**](WidgetLegendSize.md) |  | [optional] 
**show_legend** | **bool** | Whether or not to display the legend on this widget. | [optional] 
**time** | [**widget_time.WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**widget_text_align.WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**yaxis** | [**widget_axis.WidgetAxis**](WidgetAxis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


