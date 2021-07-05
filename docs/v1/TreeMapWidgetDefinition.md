# TreeMapWidgetDefinition

The treemap visualization found on the Host Dashboards comes from the output of `ps auxww`. This is not continuously run on your hosts. Instead, it’s run once on Agent start/restart. The treemap is only supported for process data on a single host dashboard — this may not be reused in other dashboards or for other metrics.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_by** | [**TreeMapColorBy**](TreeMapColorBy.md) |  | 
**group_by** | [**TreeMapGroupBy**](TreeMapGroupBy.md) |  | 
**requests** | [**[TreeMapWidgetRequest]**](TreeMapWidgetRequest.md) | List of top list widget requests. | 
**size_by** | [**TreeMapSizeBy**](TreeMapSizeBy.md) |  | 
**type** | [**TreeMapWidgetDefinitionType**](TreeMapWidgetDefinitionType.md) |  | 
**title** | **str** | Title of your widget. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


