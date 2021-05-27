# SyntheticsAPITestConfig

Configuration object for a Synthetic API test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertions** | [**[SyntheticsAssertion]**](SyntheticsAssertion.md) | Array of assertions used for the test. | [optional]  if omitted the server will use the default value of []
**config_variables** | [**[SyntheticsConfigVariable]**](SyntheticsConfigVariable.md) | Array of variables used for the test. | [optional] 
**request** | [**SyntheticsTestRequest**](SyntheticsTestRequest.md) |  | [optional] 
**steps** | [**[SyntheticsAPIStep]**](SyntheticsAPIStep.md) | When the test subtype is &#x60;multi&#x60;, the steps of the test. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


