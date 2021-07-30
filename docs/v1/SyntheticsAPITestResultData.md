# SyntheticsAPITestResultData

Object containing results for your Synthetic API test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | [**SyntheticsSSLCertificate**](SyntheticsSSLCertificate.md) |  | [optional] 
**error_code** | [**SyntheticsErrorCode**](SyntheticsErrorCode.md) |  | [optional] 
**error_message** | **str** | The API test error message. | [optional] 
**event_type** | [**SyntheticsTestProcessStatus**](SyntheticsTestProcessStatus.md) |  | [optional] 
**http_status_code** | **int** | The API test HTTP status code. | [optional] 
**request_headers** | **{str: (dict,)}** | Request header object used for the API test. | [optional] 
**response_body** | **str** | Response body returned for the API test. | [optional] 
**response_headers** | **{str: (dict,)}** | Response headers returned for the API test. | [optional] 
**response_size** | **int** | Global size in byte of the API test response. | [optional] 
**timings** | [**SyntheticsTiming**](SyntheticsTiming.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


