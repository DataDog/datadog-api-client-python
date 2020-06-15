# security_monitoring_rule_response.SecurityMonitoringRuleResponse

Detection rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[security_monitoring_rule_case.SecurityMonitoringRuleCase]**](SecurityMonitoringRuleCase.md) | Cases for generating signals. | [optional] 
**created_at** | **int** | When the rule was created, timestamp in milliseconds. | [optional] 
**creation_author_id** | **int** | User ID of the user who created the rule. | [optional] 
**id** | **str** | The ID of the rule. | [optional] 
**is_default** | **bool** | Whether the rule is included by default. | [optional] 
**is_deleted** | **bool** | Whether the rule has been deleted. | [optional] 
**is_enabled** | **bool** | Whether the rule is enabled. | [optional] 
**message** | **str** | Message for generated signals. | [optional] 
**name** | **str** | The name of the rule. | [optional] 
**options** | [**security_monitoring_rule_options.SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | [optional] 
**queries** | [**[security_monitoring_rule_query.SecurityMonitoringRuleQuery]**](SecurityMonitoringRuleQuery.md) | Queries for selecting logs which are part of the rule. | [optional] 
**tags** | **[str]** | Tags for generated signals. | [optional] 
**version** | **int** | The version of the rule. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


