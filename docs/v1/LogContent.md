# log_content.LogContent

JSON object containing all log attributes and their associated values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object of attributes from your log. | [optional] 
**host** | **str** | Name of the machine from where the logs are being sent. | [optional] 
**message** | **str** | The message [reserved attribute](https://docs.datadoghq.com/logs/log_collection/#reserved-attributes) of your log. By default, Datadog ingests the value of the message attribute as the body of the log entry. That value is then highlighted and displayed in the Logstream, where it is indexed for full text search. | [optional] 
**service** | **str** | The name of the application or service generating the log events. It is used to switch from Logs to APM, so make sure you define the same value when you use both products. | [optional] 
**tags** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array of tags associated with your log. | [optional] 
**timestamp** | **datetime** | Timestamp of your log. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


