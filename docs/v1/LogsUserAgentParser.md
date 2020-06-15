# logs_user_agent_parser.LogsUserAgentParser

The User-Agent parser takes a User-Agent attribute and extracts the OS, browser, device, and other user data. It recognizes major bots like the Google Bot, Yahoo Slurp, and Bing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**logs_user_agent_parser_type.LogsUserAgentParserType**](LogsUserAgentParserType.md) |  | 
**sources** | **[str]** | Array of source attributes. | defaults to ["http.useragent"]
**target** | **str** | Name of the parent attribute that contains all the extracted details from the &#x60;sources&#x60;. | defaults to 'http.useragent_details'
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**is_encoded** | **bool** | Define if the source attribute is URL encoded or not. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


