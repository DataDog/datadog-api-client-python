# timeseries_widget_definition.TimeseriesWidgetDefinition

The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Analyzed Spans over time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[timeseries_widget_request.TimeseriesWidgetRequest]**](TimeseriesWidgetRequest.md) | List of timeseries widget requests. | 
**type** | [**timeseries_widget_definition_type.TimeseriesWidgetDefinitionType**](TimeseriesWidgetDefinitionType.md) |  | 
**events** | [**[widget_event.WidgetEvent]**](WidgetEvent.md) | List of widget events. | [optional] 
**legend_size** | [**widget_legend_size.WidgetLegendSize**](WidgetLegendSize.md) |  | [optional] 
**markers** | [**[widget_marker.WidgetMarker]**](WidgetMarker.md) | List of markers. | [optional] 
**show_legend** | **bool** | (screenboard only) Show the legend for this widget. | [optional] 
**time** | [**widget_time.WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of your widget. | [optional] 
**title_align** | [**widget_text_align.WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**yaxis** | [**widget_axis.WidgetAxis**](WidgetAxis.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


