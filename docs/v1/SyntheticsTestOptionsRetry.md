# SyntheticsTestOptionsRetry

Object describing the retry strategy to apply to a Synthetic test.

## Properties

| Name         | Type      | Description                                                                                    | Notes      |
| ------------ | --------- | ---------------------------------------------------------------------------------------------- | ---------- |
| **count**    | **int**   | Number of times a test needs to be retried before marking a location as failed. Defaults to 0. | [optional] |
| **interval** | **float** | Time interval between retries (in milliseconds). Defaults to 300ms.                            | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
