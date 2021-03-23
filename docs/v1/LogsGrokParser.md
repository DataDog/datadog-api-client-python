# LogsGrokParser

Create custom grok rules to parse the full message or [a specific attribute of your raw event](https://docs.datadoghq.com/logs/processing/parsing/#advanced-settings). For more information, see the [parsing section](https://docs.datadoghq.com/logs/processing/parsing).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grok** | [**LogsGrokParserRules**](LogsGrokParserRules.md) |  | 
**type** | [**LogsGrokParserType**](LogsGrokParserType.md) |  | 
**source** | **str** | Name of the log attribute to parse. | defaults to "message"
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**samples** | **[str]** | List of sample logs to test this grok parser. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


