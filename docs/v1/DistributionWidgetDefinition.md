# DistributionWidgetDefinition

The Distribution visualization is another way of showing metrics aggregated across one or several tags, such as hosts. Unlike the heat map, a distribution graph’s x-axis is quantity rather than time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[DistributionWidgetRequest]**](DistributionWidgetRequest.md) | Array of one request object to display in the widget.  See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json)  to learn how to build the &#x60;REQUEST_SCHEMA&#x60;. | 
**type** | [**DistributionWidgetDefinitionType**](DistributionWidgetDefinitionType.md) |  | 
**legend_size** | **str** | (Deprecated) The widget legend was replaced by a tooltip and sidebar. | [optional] 
**markers** | [**[WidgetMarker]**](WidgetMarker.md) | List of markers. | [optional] 
**show_legend** | **bool** | (Deprecated) The widget legend was replaced by a tooltip and sidebar. | [optional] 
**time** | [**WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**xaxis** | [**DistributionWidgetXAxis**](DistributionWidgetXAxis.md) |  | [optional] 
**yaxis** | [**DistributionWidgetYAxis**](DistributionWidgetYAxis.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


