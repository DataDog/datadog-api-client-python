# SecurityMonitoringRuleCreatePayload

Create a new rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[SecurityMonitoringRuleCaseCreate]**](SecurityMonitoringRuleCaseCreate.md) | Cases for generating signals. | 
**is_enabled** | **bool** | Whether the rule is enabled. | 
**message** | **str** | Message for generated signals. | 
**name** | **str** | The name of the rule. | 
**options** | [**SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | 
**queries** | [**[SecurityMonitoringRuleQueryCreate]**](SecurityMonitoringRuleQueryCreate.md) | Queries for selecting logs which are part of the rule. | 
**tags** | **[str]** | Tags for generated signals. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


