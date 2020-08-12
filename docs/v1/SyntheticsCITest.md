# synthetics_ci_test.SyntheticsCITest

Test configuration for Synthetics CI
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** | The public ID of the Synthetics test to trigger. | 
**allow_insecure_certificates** | **bool** | Disable certificate checks in API tests. | [optional] 
**basic_auth** | [**synthetics_basic_auth.SyntheticsBasicAuth**](SyntheticsBasicAuth.md) |  | [optional] 
**body** | **str** | Body to include in the test. | [optional] 
**body_type** | **str** | Type of the data sent in a synthetics API test. | [optional] 
**cookies** | **str** | Cookies for the request. | [optional] 
**device_ids** | [**[synthetics_device_id.SyntheticsDeviceID]**](SyntheticsDeviceID.md) | For browser test, array with the different device IDs used to run the test. | [optional] 
**follow_redirects** | **bool** | For API HTTP test, whether or not the test should follow redirects. | [optional] 
**headers** | [**synthetics_test_headers.SyntheticsTestHeaders**](SyntheticsTestHeaders.md) |  | [optional] 
**locations** | **[str]** | Array of locations used to run the test. | [optional] 
**metadata** | [**synthetics_ci_test_metadata.SyntheticsCITestMetadata**](SyntheticsCITestMetadata.md) |  | [optional] 
**retry** | [**synthetics_test_options_retry.SyntheticsTestOptionsRetry**](SyntheticsTestOptionsRetry.md) |  | [optional] 
**start_url** | **str** | Starting URL for the browser test. | [optional] 
**variables** | **{str: (str,)}** | Variables to replace in the test. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


