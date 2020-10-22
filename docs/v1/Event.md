# Event

Object representing an event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | [**EventAlertType**](EventAlertType.md) |  | [optional] 
**date_happened** | **int** | POSIX timestamp of the event. Must be sent as an integer (i.e. no quotes). Limited to events no older than 7 days. | [optional] 
**device_name** | **str** | A device name. | [optional] 
**host** | **str** | Host name to associate with the event. Any tags associated with the host are also applied to this event. | [optional] 
**id** | **int** | Integer ID of the event. | [optional] [readonly] 
**payload** | **str** | Payload of the event. | [optional] [readonly] 
**priority** | [**EventPriority**](EventPriority.md) |  | [optional] 
**source_type_name** | **str** | The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). | [optional] 
**tags** | **[str]** | A list of tags to apply to the event. | [optional] 
**text** | **str** | The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with &#x60;%%% \\n&#x60; and end the text block with &#x60;\\n %%%&#x60;. Use &#x60;msg_text&#x60; with the Datadog Ruby library. | [optional] 
**title** | **str** | The event title. Limited to 100 characters. Use &#x60;msg_title&#x60; with the Datadog Ruby library. | [optional] 
**url** | **str** | URL of the event. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


