# synthetics_test_request.SyntheticsTestRequest

Object describing the Synthetic test request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**synthetics_test_request_basic_auth.SyntheticsTestRequestBasicAuth**](SyntheticsTestRequestBasicAuth.md) |  | [optional] 
**body** | **str** | Body to include in the test. | [optional] 
**headers** | **{str: (str,)}** | Headers to include when performing the test. | [optional] 
**host** | **str** | Host name to perform the test with. | [optional] 
**method** | [**http_method.HTTPMethod**](HTTPMethod.md) |  | [optional] 
**port** | **int** | Port to use when performing the test. | [optional] 
**query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Query to use for the test. | [optional] 
**timeout** | **float** | Timeout in millisecond for the test. | [optional] 
**url** | **str** | URL to perform the test with. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


