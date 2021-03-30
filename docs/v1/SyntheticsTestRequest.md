# SyntheticsTestRequest

Object describing the Synthetic test request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**SyntheticsBasicAuth**](SyntheticsBasicAuth.md) |  | [optional] 
**body** | **str** | Body to include in the test. | [optional] 
**certificate** | [**SyntheticsTestRequestCertificate**](SyntheticsTestRequestCertificate.md) |  | [optional] 
**dns_server** | **str** | DNS server to use for DNS tests. | [optional] 
**headers** | [**SyntheticsTestHeaders**](SyntheticsTestHeaders.md) |  | [optional] 
**host** | **str** | Host name to perform the test with. | [optional] 
**method** | [**HTTPMethod**](HTTPMethod.md) |  | [optional] 
**no_saving_response_body** | **bool** | Determines whether or not to save the response body. | [optional] 
**port** | **int** | Port to use when performing the test. | [optional] 
**query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Query to use for the test. | [optional] 
**timeout** | **float** | Timeout in seconds for the test. | [optional] 
**url** | **str** | URL to perform the test with. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


