# WebhooksIntegrationCustomVariableUpdateRequest

Update request of a custom variable object. _All properties are optional._

## Properties

| Name          | Type     | Description                                                                                                                                                   | Notes      |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **is_secret** | **bool** | Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.                                   | [optional] |
| **name**      | **str**  | The name of the variable. It corresponds with &#x60;&lt;CUSTOM_VARIABLE_NAME&gt;&#x60;. It must only contains upper-case characters, integers or underscores. | [optional] |
| **value**     | **str**  | Value of the custom variable.                                                                                                                                 | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
