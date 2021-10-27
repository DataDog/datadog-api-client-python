# LogsMessageRemapper

The message is a key attribute in Datadog. It is displayed in the message column of the Log Explorer and you can do full string search on it. Use this Processor to define one or more attributes as the official log message. **Note:** If multiple log message remapper processors can be applied to a given log, only the first one (according to the pipeline order) is taken into account.

## Properties

| Name           | Type                                                      | Description                              | Notes                                                                |
| -------------- | --------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| **type**       | [**LogsMessageRemapperType**](LogsMessageRemapperType.md) |                                          |
| **sources**    | **[str]**                                                 | Array of source attributes.              | defaults to ["msg"]                                                  |
| **is_enabled** | **bool**                                                  | Whether or not the processor is enabled. | [optional] if omitted the server will use the default value of False |
| **name**       | **str**                                                   | Name of the processor.                   | [optional]                                                           |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
