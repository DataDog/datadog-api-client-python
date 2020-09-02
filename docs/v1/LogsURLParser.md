# LogsURLParser

This processor extracts query parameters and other important parameters from a URL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LogsURLParserType**](LogsURLParserType.md) |  | 
**sources** | **[str]** | Array of source attributes. | defaults to ["http.url"]
**target** | **str** | Name of the parent attribute that contains all the extracted details from the &#x60;sources&#x60;. | defaults to "http.url_details"
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**normalize_ending_slashes** | **bool, none_type** | Normalize the ending slashes or not. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


