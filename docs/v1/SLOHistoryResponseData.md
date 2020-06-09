# slo_history_response_data.SLOHistoryResponseData

An array of service level objective objects.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_ts** | **int** | The &#x60;from&#x60; timestamp in epoch seconds. | [optional] 
**groups** | [**slo_history_sli_data.SLOHistorySLIData**](SLOHistorySLIData.md) |  | [optional] 
**overall** | [**slo_history_sli_data.SLOHistorySLIData**](SLOHistorySLIData.md) |  | [optional] 
**series** | [**slo_history_metrics.SLOHistoryMetrics**](SLOHistoryMetrics.md) |  | [optional] 
**thresholds** | [**{str: (slo_threshold.SLOThreshold,)}**](SLOThreshold.md) | mapping of string timeframe to the SLO threshold. | [optional] 
**to_ts** | **int** | The &#x60;to&#x60; timestamp in epoch seconds. | [optional] 
**type** | [**slo_type.SLOType**](SLOType.md) |  | [optional] 
**type_id** | [**slo_type_numeric.SLOTypeNumeric**](SLOTypeNumeric.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


