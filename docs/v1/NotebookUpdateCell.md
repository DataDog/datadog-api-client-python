# NotebookUpdateCell

Updating a notebook can either insert new cell(s) or update existing cell(s) by including the cell `id`. To delete existing cell(s), simply omit it from the list of cells.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**NotebookCellUpdateRequestAttributes**](NotebookCellUpdateRequestAttributes.md) |  | [optional] 
**type** | [**NotebookCellResourceType**](NotebookCellResourceType.md) |  | [optional] 
**id** | **str** | Notebook cell ID. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


