# SLOHistoryResponseData

An array of service level objective objects.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_ts** | **int** | The &#x60;from&#x60; timestamp in epoch seconds. | [optional] 
**groups** | [**SLOHistorySLIData**](SLOHistorySLIData.md) |  | [optional] 
**overall** | [**SLOHistorySLIData**](SLOHistorySLIData.md) |  | [optional] 
**series** | [**SLOHistoryMetrics**](SLOHistoryMetrics.md) |  | [optional] 
**thresholds** | [**{str: (SLOThreshold,)}**](SLOThreshold.md) | mapping of string timeframe to the SLO threshold. | [optional] 
**to_ts** | **int** | The &#x60;to&#x60; timestamp in epoch seconds. | [optional] 
**type** | [**SLOType**](SLOType.md) |  | [optional] 
**type_id** | [**SLOTypeNumeric**](SLOTypeNumeric.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


