# SLOHistorySLIData

An object that holds an SLI value and its associated data. It can represent an SLO's overall SLI value. This can also represent the SLI value for a specific monitor in multi-monitor SLOs, or a group in grouped SLOs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_budget_remaining** | [**SLOErrorBudgetRemainingData**](SLOErrorBudgetRemainingData.md) |  | [optional] 
**errors** | [**[SLOHistoryResponseError]**](SLOHistoryResponseError.md) | A list of errors while querying the history data for the service level objective. | [optional] 
**group** | **str** | For groups in a grouped SLO, this is the group name. | [optional] 
**history** | **[[float]]** | For &#x60;monitor&#x60; based SLOs, this includes the aggregated history uptime time series. | [optional] 
**monitor_modified** | **int** | For &#x60;monitor&#x60; based SLOs, this is the last modified timestamp in epoch seconds of the monitor. | [optional] 
**monitor_type** | **str** | For &#x60;monitor&#x60; based SLOs, this describes the type of monitor. | [optional] 
**name** | **str** | For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name. | [optional] 
**precision** | **{str: (float,)}** | A mapping of threshold &#x60;timeframe&#x60; to number of accurate decimals, regardless of the from &amp;&amp; to timestamp. | [optional] 
**preview** | **bool** | For &#x60;monitor&#x60; based SLOs, when &#x60;true&#x60; this indicates that a replay is in progress to give an accurate uptime calculation. | [optional] 
**sli_value** | **float** | The current SLI value of the SLO over the history window. | [optional] 
**span_precision** | **float** | The amount of decimal places the SLI value is accurate to for the given from &#x60;&amp;&amp;&#x60; to timestamp. | [optional] 
**uptime** | **float** | Use &#x60;sli_value&#x60; instead. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


