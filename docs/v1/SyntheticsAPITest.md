# SyntheticsAPITest

Object containing details about a Synthetic API test.

## Properties

| Name           | Type                                                                | Description                                    | Notes                 |
| -------------- | ------------------------------------------------------------------- | ---------------------------------------------- | --------------------- |
| **config**     | [**SyntheticsAPITestConfig**](SyntheticsAPITestConfig.md)           |                                                |
| **locations**  | **[str]**                                                           | Array of locations used to run the test.       |
| **name**       | **str**                                                             | Name of the test.                              |
| **options**    | [**SyntheticsTestOptions**](SyntheticsTestOptions.md)               |                                                |
| **type**       | [**SyntheticsAPITestType**](SyntheticsAPITestType.md)               |                                                |
| **message**    | **str**                                                             | Notification message associated with the test. | [optional]            |
| **monitor_id** | **int**                                                             | The associated monitor ID.                     | [optional] [readonly] |
| **public_id**  | **str**                                                             | The public ID for the test.                    | [optional] [readonly] |
| **status**     | [**SyntheticsTestPauseStatus**](SyntheticsTestPauseStatus.md)       |                                                | [optional]            |
| **subtype**    | [**SyntheticsTestDetailsSubType**](SyntheticsTestDetailsSubType.md) |                                                | [optional]            |
| **tags**       | **[str]**                                                           | Array of tags attached to the test.            | [optional]            |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
