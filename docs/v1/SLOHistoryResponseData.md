# SLOHistoryResponseData

An array of service level objective objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_ts** | **int** | The &#x60;from&#x60; timestamp in epoch seconds. | [optional] 
**group_by** | **[str]** | For &#x60;metric&#x60; based SLOs where the query includes a group-by clause, this represents the list of grouping parameters.  This is not included in responses for &#x60;monitor&#x60; based SLOs. | [optional] 
**groups** | [**[SLOHistoryMonitor]**](SLOHistoryMonitor.md) | For grouped SLOs, this represents SLI data for specific groups.  This is not included in the responses for &#x60;metric&#x60; based SLOs. | [optional] 
**monitors** | [**[SLOHistoryMonitor]**](SLOHistoryMonitor.md) | For multi-monitor SLOs, this represents SLI data for specific monitors.  This is not included in the responses for &#x60;metric&#x60; based SLOs. | [optional] 
**overall** | [**SLOHistorySLIData**](SLOHistorySLIData.md) |  | [optional] 
**series** | [**SLOHistoryMetrics**](SLOHistoryMetrics.md) |  | [optional] 
**thresholds** | [**{str: (SLOThreshold,)}**](SLOThreshold.md) | mapping of string timeframe to the SLO threshold. | [optional] 
**to_ts** | **int** | The &#x60;to&#x60; timestamp in epoch seconds. | [optional] 
**type** | [**SLOType**](SLOType.md) |  | [optional] 
**type_id** | [**SLOTypeNumeric**](SLOTypeNumeric.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


