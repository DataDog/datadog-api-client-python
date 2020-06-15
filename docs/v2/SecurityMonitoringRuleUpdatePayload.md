# security_monitoring_rule_update_payload.SecurityMonitoringRuleUpdatePayload

Update an existing rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[security_monitoring_rule_case.SecurityMonitoringRuleCase]**](SecurityMonitoringRuleCase.md) | Cases for generating signals. | [optional] 
**enabled** | **bool** | Whether the rule is enabled. | [optional] 
**message** | **str** | Message for generated signals. | [optional] 
**name** | **str** | Name of the rule. | [optional] 
**options** | [**security_monitoring_rule_options.SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | [optional] 
**queries** | [**[security_monitoring_rule_query.SecurityMonitoringRuleQuery]**](SecurityMonitoringRuleQuery.md) | Queries for selecting logs which are part of the rule. | [optional] 
**tags** | **[str]** | Tags for generated signals. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


