# TimeseriesWidgetDefinition

The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[TimeseriesWidgetRequest]**](TimeseriesWidgetRequest.md) | List of timeseries widget requests. | 
**type** | [**TimeseriesWidgetDefinitionType**](TimeseriesWidgetDefinitionType.md) |  | 
**custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md) | List of custom links. | [optional] 
**events** | [**[WidgetEvent]**](WidgetEvent.md) | List of widget events. | [optional] 
**legend_size** | **str** | Available legend sizes for a widget. Should be one of \&quot;0\&quot;, \&quot;2\&quot;, \&quot;4\&quot;, \&quot;8\&quot;, \&quot;16\&quot;, or \&quot;auto\&quot;. | [optional] 
**markers** | [**[WidgetMarker]**](WidgetMarker.md) | List of markers. | [optional] 
**right_yaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 
**show_legend** | **bool** | (screenboard only) Show the legend for this widget. | [optional] 
**time** | [**WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of your widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**yaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


