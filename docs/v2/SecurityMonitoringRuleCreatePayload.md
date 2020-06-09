# security_monitoring_rule_create_payload.SecurityMonitoringRuleCreatePayload

Create a new rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[security_monitoring_rule_case.SecurityMonitoringRuleCase]**](SecurityMonitoringRuleCase.md) | Cases for generating signals. | 
**enabled** | **bool** | Whether the rule is enabled. | 
**message** | **str** | Message for generated signals. | 
**name** | **str** | The name of the rule | 
**options** | [**security_monitoring_rule_options.SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | 
**queries** | [**[security_monitoring_rule_query.SecurityMonitoringRuleQuery]**](SecurityMonitoringRuleQuery.md) | Queries for selecting logs which are part of the rule. | 
**tags** | **[str]** | Tags for generated signals. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


