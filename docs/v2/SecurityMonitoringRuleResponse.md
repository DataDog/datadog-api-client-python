# SecurityMonitoringRuleResponse

Rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**[SecurityMonitoringRuleCase]**](SecurityMonitoringRuleCase.md) | Cases for generating signals. | [optional] 
**created_at** | **int** | When the rule was created, timestamp in milliseconds. | [optional] 
**creation_author_id** | **int** | User ID of the user who created the rule. | [optional] 
**filters** | [**[SecurityMonitoringFilter]**](SecurityMonitoringFilter.md) | Additional queries to filter matched events before they are processed. | [optional] 
**has_extended_title** | **bool** | Whether the notifications include the triggering group-by values in their title. | [optional] 
**id** | **str** | The ID of the rule. | [optional] 
**is_default** | **bool** | Whether the rule is included by default. | [optional] 
**is_deleted** | **bool** | Whether the rule has been deleted. | [optional] 
**is_enabled** | **bool** | Whether the rule is enabled. | [optional] 
**message** | **str** | Message for generated signals. | [optional] 
**name** | **str** | The name of the rule. | [optional] 
**options** | [**SecurityMonitoringRuleOptions**](SecurityMonitoringRuleOptions.md) |  | [optional] 
**queries** | [**[SecurityMonitoringRuleQuery]**](SecurityMonitoringRuleQuery.md) | Queries for selecting logs which are part of the rule. | [optional] 
**tags** | **[str]** | Tags for generated signals. | [optional] 
**update_author_id** | **int** | User ID of the user who updated the rule. | [optional] 
**version** | **int** | The version of the rule. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


