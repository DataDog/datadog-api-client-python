# NotebookCellUpdateRequestAttributes

The attributes of a notebook cell in update cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`, `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_size** | [**NotebookGraphSize**](NotebookGraphSize.md) |  | [optional] 
**split_by** | [**NotebookSplitBy**](NotebookSplitBy.md) |  | [optional] 
**time** | [**NotebookCellTime**](NotebookCellTime.md) |  | [optional] 
**definition** | [**LogStreamWidgetDefinition**](LogStreamWidgetDefinition.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


