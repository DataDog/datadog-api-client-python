# SyntheticsBrowserTestConfig

Configuration object for a Synthetic browser test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SyntheticsTestRequest**](SyntheticsTestRequest.md) |  | 
**assertions** | [**[SyntheticsAssertion]**](SyntheticsAssertion.md) | Array of assertions used for the test. | defaults to []
**set_cookie** | **str** | Cookies to be used for the request, using the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) syntax. | [optional] 
**variables** | [**[SyntheticsBrowserVariable]**](SyntheticsBrowserVariable.md) | Array of variables used for the test steps. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


