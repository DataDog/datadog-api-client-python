# IncidentCreateAttributes

The incident's attributes for a create request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_impacted** | **bool** | A flag indicating whether the incident caused customer impact. | 
**title** | **str** | The title of the incident, which summarizes what happened. | 
**fields** | [**{str: (IncidentFieldAttributes,)}**](IncidentFieldAttributes.md) | A condensed view of the user-defined fields for which to create initial selections. | [optional] 
**initial_cells** | [**[IncidentTimelineCellCreateAttributes]**](IncidentTimelineCellCreateAttributes.md) | An array of initial timeline cells to be placed at the beginning of the incident timeline. | [optional] 
**notification_handles** | [**[IncidentNotificationHandle]**](IncidentNotificationHandle.md) | Notification handles that will be notified of the incident at creation. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


