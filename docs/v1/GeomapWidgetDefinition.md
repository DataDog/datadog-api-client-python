# GeomapWidgetDefinition

This visualization displays a series of values by country on a world map.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[GeomapWidgetRequest]**](GeomapWidgetRequest.md) | Array of one request object to display in the widget. The request must contain a &#x60;group-by&#x60; tag whose value is a country ISO code.  See the [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) for information about building the &#x60;REQUEST_SCHEMA&#x60;. | 
**style** | [**GeomapWidgetDefinitionStyle**](GeomapWidgetDefinitionStyle.md) |  | 
**type** | [**GeomapWidgetDefinitionType**](GeomapWidgetDefinitionType.md) |  | 
**view** | [**GeomapWidgetDefinitionView**](GeomapWidgetDefinitionView.md) |  | 
**custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md) | A list of custom links. | [optional] 
**time** | [**WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | The title of your widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | The size of the title. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


