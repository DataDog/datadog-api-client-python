# logs_string_builder_processor.LogsStringBuilderProcessor

Use the string builder processor to add a new attribute (without spaces or special characters) to a log with the result of the provided template. This enables aggregation of different attributes or raw strings into a single attribute.  The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.  **Notes**:  - The processor only accepts attributes with values or an array of values in the blocks. - If an attribute cannot be used (object or array of object),   it is replaced by an empty string or the entire operation is skipped depending on your selection. - If the target attribute already exists, it is overwritten by the result of the template. - Results of the template cannot exceed 256 characters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The name of the attribute that contains the result of the template. | 
**template** | **str** | A formula with one or more attributes and raw text. | 
**type** | [**logs_string_builder_processor_type.LogsStringBuilderProcessorType**](LogsStringBuilderProcessorType.md) |  | 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**is_replace_missing** | **bool** | If true, it replaces all missing attributes of &#x60;template&#x60; by an empty string. If &#x60;false&#x60; (default), skips the operation for missing attributes. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


