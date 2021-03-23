# SLOHistoryMetrics

A `metric` based SLO history response.  This is not included in responses for `monitor` based SLOs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominator** | [**SLOHistoryMetricsSeries**](SLOHistoryMetricsSeries.md) |  | 
**interval** | **int** | The aggregated query interval for the series data. It&#39;s implicit based on the query time window. | 
**numerator** | [**SLOHistoryMetricsSeries**](SLOHistoryMetricsSeries.md) |  | 
**query** | **str** | The combined numerator and denominator query CSV. | 
**res_type** | **str** | The series result type. This mimics &#x60;batch_query&#x60; response type. | 
**resp_version** | **int** | The series response version type. This mimics &#x60;batch_query&#x60; response type. | 
**times** | **[float]** | An array of query timestamps in EPOCH milliseconds | 
**message** | **str** | Optional message if there are specific query issues/warnings. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


