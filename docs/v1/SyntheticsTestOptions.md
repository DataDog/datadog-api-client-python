# synthetics_test_options.SyntheticsTestOptions

Object describing the extra options for a Synthetic test.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_self_signed** | **bool** | For browser test, whether or not the test should allow self signed certificate. | [optional] 
**allow_insecure** | **bool** | Allows loading insecure content for an HTTP request. | [optional] 
**device_ids** | [**[synthetics_device_id.SyntheticsDeviceID]**](SyntheticsDeviceID.md) | Array with the different device IDs used to run the test. | [optional] 
**follow_redirects** | **bool** | For API SSL test, whether or not the test should follow redirects. | [optional] 
**min_failure_duration** | **int** | Minimum amount of time before declaring the test has failed. | [optional] 
**min_location_failed** | **int** | Minimum amount of locations that are allowed to fail for the test. | [optional] 
**retry** | [**synthetics_test_options_retry.SyntheticsTestOptionsRetry**](SyntheticsTestOptionsRetry.md) |  | [optional] 
**tick_every** | [**synthetics_tick_interval.SyntheticsTickInterval**](SyntheticsTickInterval.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


