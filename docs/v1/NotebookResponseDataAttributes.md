# NotebookResponseDataAttributes

The attributes of a notebook.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**[NotebookCellResponse]**](NotebookCellResponse.md) | List of cells to display in the notebook. | 
**name** | **str** | The name of the notebook. | 
**time** | [**NotebookGlobalTime**](NotebookGlobalTime.md) |  | 
**author** | [**NotebookAuthor**](NotebookAuthor.md) |  | [optional] 
**created** | **datetime** | UTC time stamp for when the notebook was created. | [optional] [readonly] 
**metadata** | [**NotebookMetadata**](NotebookMetadata.md) |  | [optional] 
**modified** | **datetime** | UTC time stamp for when the notebook was last modified. | [optional] [readonly] 
**status** | [**NotebookStatus**](NotebookStatus.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


