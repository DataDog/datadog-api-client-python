# WebhooksIntegration

Datadog-Webhooks integration.

## Properties

| Name               | Type                                                              | Description                                                                                                                                                                                                                 | Notes      |
| ------------------ | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **name**           | **str**                                                           | The name of the webhook. It corresponds with &#x60;&lt;WEBHOOK_NAME&gt;&#x60;. Learn more on how to use it in [monitor notifications](https://docs.datadoghq.com/monitors/notify).                                          |
| **url**            | **str**                                                           | URL of the webhook.                                                                                                                                                                                                         |
| **custom_headers** | **str, none_type**                                                | If &#x60;null&#x60;, uses no header. If given a JSON payload, these will be headers attached to your webhook.                                                                                                               | [optional] |
| **encode_as**      | [**WebhooksIntegrationEncoding**](WebhooksIntegrationEncoding.md) |                                                                                                                                                                                                                             | [optional] |
| **payload**        | **str, none_type**                                                | If &#x60;null&#x60;, uses the default payload. If given a JSON payload, the webhook returns the payload specified by the given payload. [Webhooks variable usage](https://docs.datadoghq.com/integrations/webhooks/#usage). | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
