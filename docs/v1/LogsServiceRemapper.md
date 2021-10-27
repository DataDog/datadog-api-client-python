# LogsServiceRemapper

Use this processor if you want to assign one or more attributes as the official service. **Note:** If multiple service remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.

## Properties

| Name           | Type                                                      | Description                              | Notes                                                                |
| -------------- | --------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| **sources**    | **[str]**                                                 | Array of source attributes.              |
| **type**       | [**LogsServiceRemapperType**](LogsServiceRemapperType.md) |                                          |
| **is_enabled** | **bool**                                                  | Whether or not the processor is enabled. | [optional] if omitted the server will use the default value of False |
| **name**       | **str**                                                   | Name of the processor.                   | [optional]                                                           |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
