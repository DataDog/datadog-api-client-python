# SyntheticsResource

Object describing a resource which is the combination of requests (fetch, XHR) and Assets (HTML, CSS, JS, images).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** | Number of time the resource was collected. | [optional] 
**method** | **str** | HTTP method associated to the resource. | [optional] 
**size** | **int** | Size of the resource in bytes. | [optional] 
**status** | **int** | Status Code of the resource. | [optional] 
**timestamp** | **float** | Timestamp of the resource collection. | [optional] 
**trace_id** | **str** | Trace ID associated with the resource if any. | [optional] 
**type** | [**SyntheticsResourceType**](SyntheticsResourceType.md) |  | [optional] 
**url** | **str** | URL of the resource. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


