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
**filters** | [**[SecurityMonitoringFilter]**](SecurityMonitoringFilter.md) | Additional queries to filter matched events before they are processed. | [optional] 
**has_extended_title** | **bool** | Whether the notifications include the triggering group-by values in their title. | [optional] 
**tags** | **[str]** | Tags for generated signals. | [optional] 
**type** | [**SecurityMonitoringRuleTypeCreate**](SecurityMonitoringRuleTypeCreate.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


