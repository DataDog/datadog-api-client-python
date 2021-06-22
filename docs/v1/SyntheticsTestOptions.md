# SyntheticsTestOptions

Object describing the extra options for a Synthetic test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_self_signed** | **bool** | For SSL test, whether or not the test should allow self signed certificates. | [optional] 
**allow_insecure** | **bool** | Allows loading insecure content for an HTTP request. | [optional] 
**device_ids** | [**[SyntheticsDeviceID]**](SyntheticsDeviceID.md) | For browser test, array with the different device IDs used to run the test. | [optional] 
**disable_cors** | **bool** | Whether or not to disable CORS mechanism. | [optional] 
**follow_redirects** | **bool** | For API HTTP test, whether or not the test should follow redirects. | [optional] 
**min_failure_duration** | **int** | Minimum amount of time in failure required to trigger an alert. | [optional] 
**min_location_failed** | **int** | Minimum number of locations in failure required to trigger an alert. | [optional] 
**monitor_name** | **str** | The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs. | [optional] 
**monitor_options** | [**SyntheticsTestOptionsMonitorOptions**](SyntheticsTestOptionsMonitorOptions.md) |  | [optional] 
**monitor_priority** | **int** | Integer from 1 (high) to 5 (low) indicating alert severity. | [optional] 
**no_screenshot** | **bool** | Prevents saving screenshots of the steps. | [optional] 
**retry** | [**SyntheticsTestOptionsRetry**](SyntheticsTestOptionsRetry.md) |  | [optional] 
**tick_every** | **int** | The frequency at which to run the Synthetic test (in seconds). | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


