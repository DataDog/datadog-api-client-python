# security_monitoring_signal_attributes.SecurityMonitoringSignalAttributes

JSON object containing all signal attributes and their associated values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object of attributes in the security signal. | [optional] 
**message** | **str** | The message the security signal, defined by the rule which which generated the signal. | [optional] 
**tags** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array of tags associated with the security signal. | [optional] 
**timestamp** | **datetime** | Timestamp of the security signal. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


