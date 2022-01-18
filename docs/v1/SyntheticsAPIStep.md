# SyntheticsAPIStep

The steps used in a Synthetics multistep API test.

## Properties

| Name                 | Type                                                            | Description                                                                                                                                           | Notes          |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **name**             | **str**                                                         | The name of the step.                                                                                                                                 |
| **request**          | [**SyntheticsTestRequest**](SyntheticsTestRequest.md)           |                                                                                                                                                       |
| **subtype**          | [**SyntheticsAPIStepSubtype**](SyntheticsAPIStepSubtype.md)     |                                                                                                                                                       |
| **assertions**       | [**[SyntheticsAssertion]**](SyntheticsAssertion.md)             | Array of assertions used for the test.                                                                                                                | defaults to [] |
| **allow_failure**    | **bool**                                                        | Determines whether or not to continue with test if this step fails.                                                                                   | [optional]     |
| **extracted_values** | [**[SyntheticsParsingOptions]**](SyntheticsParsingOptions.md)   | Array of values to parse and save as variables from the response.                                                                                     | [optional]     |
| **is_critical**      | **bool**                                                        | Determines whether or not to consider the entire test as failed if this step fails. Can be used only if &#x60;allowFailure&#x60; is &#x60;true&#x60;. | [optional]     |
| **retry**            | [**SyntheticsTestOptionsRetry**](SyntheticsTestOptionsRetry.md) |                                                                                                                                                       | [optional]     |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
