# synthetics_api_test_result_full.SyntheticsAPITestResultFull

Object returned describing a API test result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check** | [**synthetics_api_test_result_full_check.SyntheticsAPITestResultFullCheck**](SyntheticsAPITestResultFullCheck.md) |  | [optional] 
**check_time** | **float** | When the API test was conducted. | [optional] 
**check_version** | **int** | Version of the API test used. | [optional] 
**probe_dc** | **str** | Locations for which to query the API test results. | [optional] 
**result** | [**synthetics_api_test_result_data.SyntheticsAPITestResultData**](SyntheticsAPITestResultData.md) |  | [optional] 
**result_id** | **str** | ID of the API test result. | [optional] 
**status** | [**synthetics_test_monitor_status.SyntheticsTestMonitorStatus**](SyntheticsTestMonitorStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


