# IncidentUpdateAttributes

The incident's attributes for an update request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_impact_end** | **datetime, none_type** | Timestamp when customers were no longer impacted by the incident. | [optional] 
**customer_impact_scope** | **str** | A summary of the impact customers experienced during the incident. | [optional] 
**customer_impact_start** | **datetime, none_type** | Timestamp when customers began being impacted by the incident. | [optional] 
**customer_impacted** | **bool** | A flag indicating whether the incident caused customer impact. | [optional] 
**detected** | **datetime, none_type** | Timestamp when the incident was detected. | [optional] 
**fields** | [**{str: (IncidentFieldAttributes,)}**](IncidentFieldAttributes.md) | A condensed view of the user-defined fields for which to update selections. | [optional] 
**notification_handles** | **[str]** | Notification handles that will be notified of the incident during update. | [optional] 
**resolved** | **datetime, none_type** | Timestamp when the incident&#39;s state was set to resolved. | [optional] 
**title** | **str** | The title of the incident, which summarizes what happened. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


