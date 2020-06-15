# host_map_widget_definition.HostMapWidgetDefinition

The host map widget graphs any metric across your hosts using the same visualization available from the main Host Map page.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**host_map_widget_definition_requests.HostMapWidgetDefinitionRequests**](HostMapWidgetDefinitionRequests.md) |  | 
**type** | [**host_map_widget_definition_type.HostMapWidgetDefinitionType**](HostMapWidgetDefinitionType.md) |  | 
**group** | **[str]** | List of tag prefixes to group by. | [optional] 
**no_group_hosts** | **bool** | Whether to show the hosts that don’t fit in a group. | [optional] 
**no_metric_hosts** | **bool** | Whether to show the hosts with no metrics. | [optional] 
**node_type** | [**widget_node_type.WidgetNodeType**](WidgetNodeType.md) |  | [optional] 
**notes** | **str** | Notes on the title. | [optional] 
**scope** | **[str]** | List of tags used to filter the map. | [optional] 
**style** | [**host_map_widget_definition_style.HostMapWidgetDefinitionStyle**](HostMapWidgetDefinitionStyle.md) |  | [optional] 
**title** | **str** | Title of the widget. | [optional] 
**title_align** | [**widget_text_align.WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


