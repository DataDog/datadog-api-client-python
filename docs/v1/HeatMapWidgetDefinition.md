# HeatMapWidgetDefinition

The heat map visualization shows metrics aggregated across many tags, such as hosts. The more hosts that have a particular value, the darker that square is.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[HeatMapWidgetRequest]**](HeatMapWidgetRequest.md) | List of widget types. | 
**type** | [**HeatMapWidgetDefinitionType**](HeatMapWidgetDefinitionType.md) |  | 
**custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md) | List of custom links. | [optional] 
**events** | [**[WidgetEvent]**](WidgetEvent.md) | List of widget events. | [optional] 
**legend_size** | **str** | Available legend sizes for a widget. Should be one of \&quot;0\&quot;, \&quot;2\&quot;, \&quot;4\&quot;, \&quot;8\&quot;, \&quot;16\&quot;, or \&quot;auto\&quot;. | [optional] 
**show_legend** | **bool** | Whether or not to display the legend on this widget. | [optional] 
**time** | [**WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**yaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


