# logs_response_metadata.LogsResponseMetadata

The metadata associated with a request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | The time elapsed in milliseconds | [optional] 
**page** | [**logs_response_metadata_page.LogsResponseMetadataPage**](LogsResponseMetadataPage.md) |  | [optional] 
**request_id** | **str** | The identifier of the request | [optional] 
**status** | [**logs_aggregate_response_status.LogsAggregateResponseStatus**](LogsAggregateResponseStatus.md) |  | [optional] 
**warnings** | [**[logs_warning.LogsWarning]**](LogsWarning.md) | A list of warnings (non fatal errors) encountered, partial results might be returned if warnings are present in the response. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


