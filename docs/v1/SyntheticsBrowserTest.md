# SyntheticsBrowserTest

Object containing details about a Synthetic browser test.

## Properties

| Name           | Type                                                              | Description                                                                                   | Notes                 |
| -------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------- |
| **config**     | [**SyntheticsBrowserTestConfig**](SyntheticsBrowserTestConfig.md) |                                                                                               |
| **locations**  | **[str]**                                                         | Array of locations used to run the test.                                                      |
| **name**       | **str**                                                           | Name of the test.                                                                             |
| **options**    | [**SyntheticsTestOptions**](SyntheticsTestOptions.md)             |                                                                                               |
| **type**       | [**SyntheticsBrowserTestType**](SyntheticsBrowserTestType.md)     |                                                                                               |
| **message**    | **str**                                                           | Notification message associated with the test. Message can either be text or an empty string. | [optional]            |
| **monitor_id** | **int**                                                           | The associated monitor ID.                                                                    | [optional] [readonly] |
| **public_id**  | **str**                                                           | The public ID of the test.                                                                    | [optional] [readonly] |
| **status**     | [**SyntheticsTestPauseStatus**](SyntheticsTestPauseStatus.md)     |                                                                                               | [optional]            |
| **steps**      | [**[SyntheticsStep]**](SyntheticsStep.md)                         | The steps of the test.                                                                        | [optional]            |
| **tags**       | **[str]**                                                         | Array of tags attached to the test.                                                           | [optional]            |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
