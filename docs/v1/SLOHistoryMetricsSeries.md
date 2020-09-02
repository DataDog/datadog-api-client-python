# SLOHistoryMetricsSeries

A representation of `metric` based SLO time series for the provided queries. This is the same response type from `batch_query` endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of submitted metrics. | 
**metadata** | [**SLOHistoryMetricsSeriesMetadata**](SLOHistoryMetricsSeriesMetadata.md) |  | 
**sum** | **float** | Total sum of the query. | 
**values** | **[float]** | The query values for each metric. | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


