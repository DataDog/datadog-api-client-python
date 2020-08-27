# change_widget_definition.ChangeWidgetDefinition

The Change graph shows you the change in a value over the time period chosen.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[change_widget_request.ChangeWidgetRequest]**](ChangeWidgetRequest.md) | Array of one request object to display in the widget.  See the dedicated [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json)  to learn how to build the &#x60;REQUEST_SCHEMA&#x60;. | 
**type** | [**change_widget_definition_type.ChangeWidgetDefinitionType**](ChangeWidgetDefinitionType.md) |  | 
**custom_links** | [**[widget_custom_link.WidgetCustomLink]**](WidgetCustomLink.md) | List of custom links. | [optional] 
**time** | [**widget_time.WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**widget_text_align.WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


