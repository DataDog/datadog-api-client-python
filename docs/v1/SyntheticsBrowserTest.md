# SyntheticsBrowserTest

Object containing details about a Synthetic browser test.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Notification message associated with the test. Message can either be text or an empty string. | 
**config** | [**SyntheticsBrowserTestConfig**](SyntheticsBrowserTestConfig.md) |  | [optional] 
**locations** | **[str]** | Array of locations used to run the test. | [optional] 
**monitor_id** | **int** | The associated monitor ID. | [optional] 
**name** | **str** | Name of the test. | [optional] 
**options** | [**SyntheticsTestOptions**](SyntheticsTestOptions.md) |  | [optional] 
**public_id** | **str** | The public ID of the test. | [optional] 
**status** | [**SyntheticsTestPauseStatus**](SyntheticsTestPauseStatus.md) |  | [optional] 
**steps** | [**[SyntheticsStep]**](SyntheticsStep.md) | The steps of the test. | [optional] 
**tags** | **[str]** | Array of tags attached to the test. | [optional] 
**type** | [**SyntheticsBrowserTestType**](SyntheticsBrowserTestType.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


