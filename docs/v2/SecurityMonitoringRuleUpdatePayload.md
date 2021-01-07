# SecurityMonitoringRuleUpdatePayload

Update an existing rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[SecurityMonitoringRuleCase]**](SecurityMonitoringRuleCase.md) | Cases for generating signals. | [optional] 
**filters** | [**[SecurityMonitoringFilter]**](SecurityMonitoringFilter.md) | Additional queries to filter matched events before they are processed. | [optional] 
**is_enabled** | **bool** | Whether the rule is enabled. | [optional] 
**message** | **str** | Message for generated signals. | [optional] 
**name** | **str** | Name of the rule. | [optional] 
**options** | [**SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | [optional] 
**queries** | [**[SecurityMonitoringRuleQuery]**](SecurityMonitoringRuleQuery.md) | Queries for selecting logs which are part of the rule. | [optional] 
**tags** | **[str]** | Tags for generated signals. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


