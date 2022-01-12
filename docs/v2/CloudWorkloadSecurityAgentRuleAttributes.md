# CloudWorkloadSecurityAgentRuleAttributes

A Cloud Workload Security Agent rule returned by the API.

## Properties

| Name              | Type                                                                                                      | Description                                                      | Notes      |
| ----------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------- |
| **category**      | **str**                                                                                                   | The category of the Agent rule.                                  | [optional] |
| **creation_date** | **int**                                                                                                   | When the Agent rule was created, timestamp in milliseconds.      | [optional] |
| **creator**       | [**CloudWorkloadSecurityAgentRuleCreatorAttributes**](CloudWorkloadSecurityAgentRuleCreatorAttributes.md) |                                                                  | [optional] |
| **default_rule**  | **bool**                                                                                                  | Whether the rule is included by default.                         | [optional] |
| **description**   | **str**                                                                                                   | The description of the Agent rule.                               | [optional] |
| **enabled**       | **bool**                                                                                                  | Whether the Agent rule is enabled.                               | [optional] |
| **expression**    | **str**                                                                                                   | The SECL expression of the Agent rule.                           | [optional] |
| **name**          | **str**                                                                                                   | The name of the Agent rule.                                      | [optional] |
| **updated_at**    | **int**                                                                                                   | When the Agent rule was last updated, timestamp in milliseconds. | [optional] |
| **updater**       | [**CloudWorkloadSecurityAgentRuleUpdaterAttributes**](CloudWorkloadSecurityAgentRuleUpdaterAttributes.md) |                                                                  | [optional] |
| **version**       | **int**                                                                                                   | The version of the Agent rule.                                   | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
