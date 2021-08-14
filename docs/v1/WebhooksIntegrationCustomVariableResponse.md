# WebhooksIntegrationCustomVariableResponse

Custom variable for Webhook integration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **bool** | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload. | 
**name** | **str** | The name of the variable. It corresponds with &#x60;&lt;CUSTOM_VARIABLE_NAME&gt;&#x60;. It must only contains upper-case characters, integers or underscores. | 
**value** | **str** | Value of the custom variable. It won&#39;t be returned if the variable is secret. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


