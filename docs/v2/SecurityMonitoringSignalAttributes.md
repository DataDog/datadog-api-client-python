# SecurityMonitoringSignalAttributes

The object containing all signal attributes and their associated values.

## Properties

| Name           | Type                                                                      | Description                                                                       | Notes      |
| -------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------- |
| **attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A JSON object of attributes in the security signal.                               | [optional] |
| **message**    | **str**                                                                   | The message in the security signal defined by the rule that generated the signal. | [optional] |
| **tags**       | **[str]**                                                                 | An array of tags associated with the security signal.                             | [optional] |
| **timestamp**  | **datetime**                                                              | The timestamp of the security signal.                                             | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
