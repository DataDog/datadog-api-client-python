# LogsProcessor

Definition of a logs processor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grok** | [**LogsGrokParserRules**](LogsGrokParserRules.md) |  | defaults to nulltype.Null
**source** | **str** | Source attribute used to perform the lookup. | defaults to nulltype.Null
**type** | [**LogsTraceRemapperType**](LogsTraceRemapperType.md) |  | defaults to nulltype.Null
**sources** | **[str]** | Array of source attributes. | defaults to nulltype.Null
**target** | **str** | Name of the attribute that contains the corresponding value in the mapping list or the &#x60;default_lookup&#x60; if not found in the mapping list. | defaults to nulltype.Null
**categories** | [**[LogsCategoryProcessorCategory]**](LogsCategoryProcessorCategory.md) | Array of filters to match or not a log and their corresponding &#x60;name&#x60;to assign a custom value to the log. | defaults to nulltype.Null
**expression** | **str** | Arithmetic operation between one or more log attributes. | defaults to nulltype.Null
**template** | **str** | A formula with one or more attributes and raw text. | defaults to nulltype.Null
**lookup_table** | **[str]** | Mapping table of values for the source attribute and their associated target attribute values, formatted as &#x60;[\&quot;source_key1,target_value1\&quot;, \&quot;source_key2,target_value2\&quot;]&#x60; | defaults to nulltype.Null
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**samples** | **[str]** | List of sample logs to test this grok parser. | [optional] 
**override_on_conflict** | **bool** | Override or not the target element if already set, | [optional]  if omitted the server will use the default value of False
**preserve_source** | **bool** | Remove or preserve the remapped source element. | [optional]  if omitted the server will use the default value of False
**source_type** | **str** | Defines if the sources are from log &#x60;attribute&#x60; or &#x60;tag&#x60;. | [optional]  if omitted the server will use the default value of "attribute"
**target_format** | [**TargetFormatType**](TargetFormatType.md) |  | [optional] 
**target_type** | **str** | Defines if the final attribute or tag name is from log &#x60;attribute&#x60; or &#x60;tag&#x60;. | [optional]  if omitted the server will use the default value of "attribute"
**normalize_ending_slashes** | **bool, none_type** | Normalize the ending slashes or not. | [optional]  if omitted the server will use the default value of False
**is_encoded** | **bool** | Define if the source attribute is URL encoded or not. | [optional]  if omitted the server will use the default value of False
**is_replace_missing** | **bool** | If true, it replaces all missing attributes of &#x60;template&#x60; by an empty string. If &#x60;false&#x60; (default), skips the operation for missing attributes. | [optional]  if omitted the server will use the default value of False
**filter** | [**LogsFilter**](LogsFilter.md) |  | [optional] 
**processors** | [**[LogsProcessor]**](LogsProcessor.md) | Ordered list of processors in this pipeline. | [optional] 
**default_lookup** | **str** | Value to set the target attribute if the source value is not found in the list. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


