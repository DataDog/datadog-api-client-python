# NotebooksResponseDataAttributes

The attributes of a notebook in get all response.

## Properties

| Name         | Type                                                  | Description                                             | Notes                 |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------- | --------------------- |
| **name**     | **str**                                               | The name of the notebook.                               |
| **author**   | [**NotebookAuthor**](NotebookAuthor.md)               |                                                         | [optional]            |
| **cells**    | [**[NotebookCellResponse]**](NotebookCellResponse.md) | List of cells to display in the notebook.               | [optional]            |
| **created**  | **datetime**                                          | UTC time stamp for when the notebook was created.       | [optional] [readonly] |
| **metadata** | [**NotebookMetadata**](NotebookMetadata.md)           |                                                         | [optional]            |
| **modified** | **datetime**                                          | UTC time stamp for when the notebook was last modified. | [optional] [readonly] |
| **status**   | [**NotebookStatus**](NotebookStatus.md)               |                                                         | [optional]            |
| **time**     | [**NotebookGlobalTime**](NotebookGlobalTime.md)       |                                                         | [optional]            |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
