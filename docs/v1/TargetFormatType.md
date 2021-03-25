# TargetFormatType

If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types. If the `target_type` is `tag`, this parameter may not be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | If the &#x60;target_type&#x60; of the remapper is &#x60;attribute&#x60;, try to cast the value to a new specific type. If the cast is not possible, the original type is kept. &#x60;string&#x60;, &#x60;integer&#x60;, or &#x60;double&#x60; are the possible types. If the &#x60;target_type&#x60; is &#x60;tag&#x60;, this parameter may not be specified. |  must be one of ["auto", "string", "integer", "double", ]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


