# logs_attribute_remapper.LogsAttributeRemapper

The remapper processor remaps any source attribute(s) or tag to another target attribute or tag. Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice). Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **[str]** | Array of source attributes. | 
**target** | **str** | Final attribute or tag name to remap the sources to. | 
**type** | [**logs_attribute_remapper_type.LogsAttributeRemapperType**](LogsAttributeRemapperType.md) |  | 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**override_on_conflict** | **bool** | Override or not the target element if already set, | [optional]  if omitted the server will use the default value of False
**preserve_source** | **bool** | Remove or preserve the remapped source element. | [optional]  if omitted the server will use the default value of False
**source_type** | **str** | Defines if the sources are from log &#x60;attribute&#x60; or &#x60;tag&#x60;. | [optional]  if omitted the server will use the default value of 'attribute'
**target_type** | **str** | Defines if the sources are from log &#x60;attribute&#x60; or &#x60;tag&#x60;. | [optional]  if omitted the server will use the default value of 'attribute'

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


