# SyntheticsTestConfig

Configuration object for a Synthetic test.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SyntheticsTestRequest**](SyntheticsTestRequest.md) |  | 
**assertions** | [**[SyntheticsAssertion]**](SyntheticsAssertion.md) | Array of assertions used for the test. | defaults to []
**config_variables** | [**[SyntheticsConfigVariable]**](SyntheticsConfigVariable.md) | API tests only - array of variables used for the test. | [optional] 
**variables** | [**[SyntheticsBrowserVariable]**](SyntheticsBrowserVariable.md) | Browser tests only - array of variables used for the test steps. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


