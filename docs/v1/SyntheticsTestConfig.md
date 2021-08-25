# SyntheticsTestConfig

Configuration object for a Synthetic test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertions** | [**[SyntheticsAssertion]**](SyntheticsAssertion.md) | Array of assertions used for the test. | [optional]  if omitted the server will use the default value of []
**config_variables** | [**[SyntheticsConfigVariable]**](SyntheticsConfigVariable.md) | Array of variables used for the test. | [optional] 
**request** | [**SyntheticsTestRequest**](SyntheticsTestRequest.md) |  | [optional] 
**variables** | [**[SyntheticsBrowserVariable]**](SyntheticsBrowserVariable.md) | Browser tests only - array of variables used for the test steps. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


