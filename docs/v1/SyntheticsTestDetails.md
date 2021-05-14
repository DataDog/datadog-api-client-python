# SyntheticsTestDetails

Object containing details about your Synthetic test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**SyntheticsTestConfig**](SyntheticsTestConfig.md) |  | [optional] 
**locations** | **[str]** | Array of locations used to run the test. | [optional] 
**message** | **str** | Notification message associated with the test. | [optional] 
**monitor_id** | **int** | The associated monitor ID. | [optional] [readonly] 
**name** | **str** | Name of the test. | [optional] 
**options** | [**SyntheticsTestOptions**](SyntheticsTestOptions.md) |  | [optional] 
**public_id** | **str** | The test public ID. | [optional] [readonly] 
**status** | [**SyntheticsTestPauseStatus**](SyntheticsTestPauseStatus.md) |  | [optional] 
**steps** | [**[SyntheticsStep]**](SyntheticsStep.md) | For browser test, the steps of the test. | [optional] 
**subtype** | [**SyntheticsTestDetailsSubType**](SyntheticsTestDetailsSubType.md) |  | [optional] 
**tags** | **[str]** | Array of tags attached to the test. | [optional] 
**type** | [**SyntheticsTestDetailsType**](SyntheticsTestDetailsType.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


