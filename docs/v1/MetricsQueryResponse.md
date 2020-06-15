# metrics_query_response.MetricsQueryResponse

Response Object that includes your query and the list of metrics retrieved.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Message indicating the errors if status is not &#x60;ok&#x60;. | [optional] [readonly] 
**from_date** | **int** | Start of requested time window, milliseconds since Unix epoch. | [optional] [readonly] 
**group_by** | **[str]** | List of tag keys on which to group. | [optional] [readonly] 
**message** | **str** | Message indicating &#x60;success&#x60; if status is &#x60;ok&#x60;. | [optional] [readonly] 
**query** | **str** | Query string | [optional] [readonly] 
**res_type** | **str** | Type of response. | [optional] [readonly] 
**series** | [**[metrics_query_response_series.MetricsQueryResponseSeries]**](MetricsQueryResponseSeries.md) | List of timeseries queried. | [optional] [readonly] 
**status** | **str** | Status of the query. | [optional] [readonly] 
**to_date** | **int** | End of requested time window, milliseconds since Unix epoch. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


