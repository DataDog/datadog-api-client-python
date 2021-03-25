# LogsListResponse

Response object with all logs matching the request and pagination information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**[Log]**](Log.md) | Array of logs matching the request and the &#x60;nextLogId&#x60; if sent. | [optional] 
**next_log_id** | **str** | Hash identifier of the next log to return in the list. This parameter is used for the pagination feature. | [optional] 
**status** | **str** | Status of the response. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


