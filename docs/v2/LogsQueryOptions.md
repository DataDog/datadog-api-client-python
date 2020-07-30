# logs_query_options.LogsQueryOptions

Global query options that are used during the query. Note: You should only supply timezone or time offset but not both otherwise the query will fail.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_offset** | **int** | The time offset (in seconds) to apply to the query. | [optional] 
**timezone** | **str** | The timezone can be specified both as an offset, for example: \&quot;UTC+03:00\&quot;. | [optional]  if omitted the server will use the default value of 'UTC'

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


