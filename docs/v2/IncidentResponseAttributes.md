# IncidentResponseAttributes

The incident's attributes from a response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the incident, which summarizes what happened. | 
**created** | **datetime** | Timestamp when the incident was created. | [optional] [readonly] 
**customer_impact_duration** | **int** | Length of the incident&#39;s customer impact in seconds. Equals the difference between &#x60;customer_impact_start&#x60; and &#x60;customer_impact_end&#x60;. | [optional] [readonly] 
**customer_impact_end** | **datetime, none_type** | Timestamp when customers were no longer impacted by the incident. | [optional] 
**customer_impact_scope** | **str, none_type** | A summary of the impact customers experienced during the incident. | [optional] 
**customer_impact_start** | **datetime, none_type** | Timestamp when customers began being impacted by the incident. | [optional] 
**customer_impacted** | **bool** | A flag indicating whether the incident caused customer impact. | [optional] 
**detected** | **datetime, none_type** | Timestamp when the incident was detected. | [optional] 
**fields** | [**{str: (IncidentFieldAttributes,)}**](IncidentFieldAttributes.md) | A condensed view of the user-defined fields attached to incidents. | [optional] 
**modified** | **datetime** | Timestamp when the incident was last modified. | [optional] [readonly] 
**notification_handles** | [**[IncidentNotificationHandle], none_type**](IncidentNotificationHandle.md) | Notification handles that will be notified of the incident during update. | [optional] 
**postmortem_id** | **str** | The UUID of the postmortem object attached to the incident. | [optional] 
**public_id** | **int** | The monotonically increasing integer ID for the incident. | [optional] 
**resolved** | **datetime, none_type** | Timestamp when the incident&#39;s state was set to resolved. | [optional] 
**time_to_detect** | **int** | The amount of time in seconds to detect the incident. Equals the difference between &#x60;customer_impact_start&#x60; and &#x60;detected&#x60;. | [optional] [readonly] 
**time_to_internal_response** | **int** | The amount of time in seconds to call incident after detection. Equals the difference of &#x60;detected&#x60; and &#x60;created&#x60;. | [optional] [readonly] 
**time_to_repair** | **int** | The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between &#x60;customer_impact_end&#x60; and &#x60;detected&#x60;. | [optional] [readonly] 
**time_to_resolve** | **int** | The amount of time in seconds to resolve the incident after it was created. Equals the difference between &#x60;created&#x60; and &#x60;resolved&#x60;. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


