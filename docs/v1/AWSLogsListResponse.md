# aws_logs_list_response.AWSLogsListResponse

A list of all Datadog-AWS logs integrations available in your Datadog organization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Your AWS Account ID without dashes. | [optional] 
**lambdas** | [**[aws_logs_list_response_lambdas.AWSLogsListResponseLambdas]**](AWSLogsListResponseLambdas.md) | List of ARNs configured in your Datadog account. | [optional] 
**services** | **[str]** | Array of services IDs. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


