# GraphSnapshot

Object representing a graph snapshot.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_def** | **str** | A JSON document defining the graph. &#x60;graph_def&#x60; can be used instead of &#x60;metric_query&#x60;. The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar) and should be formatted to a single line then URL encoded. | [optional] 
**metric_query** | **str** | The metric query. One of &#x60;metric_query&#x60; or &#x60;graph_def&#x60; is required. | [optional] 
**snapshot_url** | **str** | URL of your [graph snapshot](https://docs.datadoghq.com/metrics/explorer/#snapshot). | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


