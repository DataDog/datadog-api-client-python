# synthetics_step_detail.SyntheticsStepDetail

Object describing a step for a Synthetic test.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_errors** | [**[synthetics_browser_error.SyntheticsBrowserError]**](SyntheticsBrowserError.md) | Array of errors collected for a browser test. | [optional] 
**check_type** | [**synthetics_check_type.SyntheticsCheckType**](SyntheticsCheckType.md) |  | [optional] 
**description** | **str** | Description of the test. | [optional] 
**duration** | **float** | Total duration in millisecond of the test. | [optional] 
**error** | **str** | Error returned by the test. | [optional] 
**playing_tab** | [**synthetics_playing_tab.SyntheticsPlayingTab**](SyntheticsPlayingTab.md) |  | [optional] 
**resources** | [**[synthetics_resource.SyntheticsResource]**](SyntheticsResource.md) | Array of resources collected by the test. | [optional] 
**screenshot_bucket_key** | **bool** | Whether or not screenshots where collected by the test. | [optional] 
**skipped** | **bool** | Whether or not to skip this step. | [optional] 
**snapshot_bucket_key** | **bool** | Whether or not snapshots where collected by the test. | [optional] 
**step_id** | **int** | The step ID. | [optional] 
**sub_test_step_details** | [**[SyntheticsStepDetail]**](SyntheticsStepDetail.md) | If this steps include a sub-test. [Subtests documentation](https://docs.datadoghq.com/synthetics/browser_tests/advanced_options/#subtests). | [optional] 
**time_to_interactive** | **float** | Time before starting the step. | [optional] 
**type** | [**synthetics_step_type.SyntheticsStepType**](SyntheticsStepType.md) |  | [optional] 
**url** | **str** | URL to perform the step against. | [optional] 
**value** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Value for the step. | [optional] 
**warnings** | [**[synthetics_step_detail_warnings.SyntheticsStepDetailWarnings]**](SyntheticsStepDetailWarnings.md) | Warning collected that didn&#39;t failed the step. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


