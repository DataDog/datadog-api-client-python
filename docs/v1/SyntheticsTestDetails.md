# synthetics_test_details.SyntheticsTestDetails

Object containing details about your Synthetic test.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**synthetics_test_config.SyntheticsTestConfig**](SyntheticsTestConfig.md) |  | [optional] 
**locations** | **[str]** | Array of locations used to run the test. | [optional] 
**message** | **str** | Notification message associated with the test. | [optional] 
**monitor_id** | **int** | The associated monitor ID. | [optional] 
**name** | **str** | Name of the test. | [optional] 
**options** | [**synthetics_test_options.SyntheticsTestOptions**](SyntheticsTestOptions.md) |  | [optional] 
**public_id** | **str** | The test public ID. | [optional] 
**status** | [**synthetics_test_pause_status.SyntheticsTestPauseStatus**](SyntheticsTestPauseStatus.md) |  | [optional] 
**steps** | [**[synthetics_step.SyntheticsStep]**](SyntheticsStep.md) | The steps of the test (only for browser tests). | [optional] 
**subtype** | [**synthetics_test_details_sub_type.SyntheticsTestDetailsSubType**](SyntheticsTestDetailsSubType.md) |  | [optional] 
**tags** | **[str]** | Array of tags attached to the test. | [optional] 
**type** | [**synthetics_test_details_type.SyntheticsTestDetailsType**](SyntheticsTestDetailsType.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


