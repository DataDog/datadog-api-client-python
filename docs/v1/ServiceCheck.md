# ServiceCheck

An object containing service check and status.

## Properties

| Name          | Type                                            | Description                              | Notes      |
| ------------- | ----------------------------------------------- | ---------------------------------------- | ---------- |
| **check**     | **str**                                         | The check.                               |
| **host_name** | **str**                                         | The host name correlated with the check. |
| **status**    | [**ServiceCheckStatus**](ServiceCheckStatus.md) |                                          |
| **tags**      | **[str]**                                       | Tags related to a check.                 |
| **message**   | **str**                                         | Message containing check status.         | [optional] |
| **timestamp** | **int**                                         | Time of check.                           | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
