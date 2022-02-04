# SyntheticsBrowserTestResultData

Object containing results for your Synthetic browser test.

## Properties

| Name                      | Type                                                                            | Description                                                                         | Notes      |
| ------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------- |
| **browser_type**          | **str**                                                                         | Type of browser device used for the browser test.                                   | [optional] |
| **browser_version**       | **str**                                                                         | Browser version used for the browser test.                                          | [optional] |
| **device**                | [**SyntheticsDevice**](SyntheticsDevice.md)                                     |                                                                                     | [optional] |
| **duration**              | **float**                                                                       | Global duration in second of the browser test.                                      | [optional] |
| **error**                 | **str**                                                                         | Error returned for the browser test.                                                | [optional] |
| **failure**               | [**SyntheticsBrowserTestResultFailure**](SyntheticsBrowserTestResultFailure.md) |                                                                                     | [optional] |
| **passed**                | **bool**                                                                        | Whether or not the browser test was conducted.                                      | [optional] |
| **received_email_count**  | **int**                                                                         | The amount of email received during the browser test.                               | [optional] |
| **start_url**             | **str**                                                                         | Starting URL for the browser test.                                                  | [optional] |
| **step_details**          | [**[SyntheticsStepDetail]**](SyntheticsStepDetail.md)                           | Array containing the different browser test steps.                                  | [optional] |
| **thumbnails_bucket_key** | **bool**                                                                        | Whether or not a thumbnail is associated with the browser test.                     | [optional] |
| **time_to_interactive**   | **float**                                                                       | Time in second to wait before the browser test starts after reaching the start URL. | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
