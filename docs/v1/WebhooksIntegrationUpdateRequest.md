# WebhooksIntegrationUpdateRequest

Update request of a Webhooks integration object.  *All properties are optional.*

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_headers** | **str** | If &#x60;null&#x60;, uses no header. If given a JSON payload, these will be headers attached to your webhook. | [optional] 
**encode_as** | [**WebhooksIntegrationEncoding**](WebhooksIntegrationEncoding.md) |  | [optional] 
**name** | **str** | The name of the webhook. It corresponds with &#x60;&lt;WEBHOOK_NAME&gt;&#x60;. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notifications). | [optional] 
**payload** | **str, none_type** | If &#x60;null&#x60;, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). | [optional] 
**url** | **str** | URL of the webhook. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


