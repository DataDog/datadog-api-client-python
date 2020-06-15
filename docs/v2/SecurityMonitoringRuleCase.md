# security_monitoring_rule_case.SecurityMonitoringRuleCase

Case when signal is generated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | A rule case contains logical operations (&gt;, &gt;&#x3D;, &amp;&amp;, ||) to determine if a signal should be generated based on the event counts in the previously defined queries. | [optional] 
**name** | **str** | Name of the case. | [optional] 
**notifications** | **[str]** | Notification targets for each rule case | [optional] 
**status** | [**security_monitoring_rule_severity.SecurityMonitoringRuleSeverity**](SecurityMonitoringRuleSeverity.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


