# SecurityMonitoringRuleThirdPartyOptions

Options for third-party rules.

## Properties

| Name                      | Type                                                                    | Description                                                                                      | Notes      |
| ------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------- |
| **default_notifications** | **[str]**                                                               | Notification targets for the root query.                                                         | [optional] |
| **default_status**        | [**SecurityMonitoringRuleSeverity**](SecurityMonitoringRuleSeverity.md) |                                                                                                  | [optional] |
| **first_seen_override**   | **str**                                                                 | (Optional): the name of an attribute to override the first seen value of the third party signal. | [optional] |
| **last_seen_override**    | **str**                                                                 | (Optional): the name of an attribute to override the last seen value of the third party signal.  | [optional] |
| **root_query**            | **str**                                                                 | Root query of the rule.                                                                          | [optional] |
| **signal_id**             | **str**                                                                 | Optional mapping of the third-party signal ID.                                                   | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
