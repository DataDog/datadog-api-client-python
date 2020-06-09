# service_level_objective_request.ServiceLevelObjectiveRequest

A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, `tags`, etc.).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service level objective object. | 
**thresholds** | [**[slo_threshold.SLOThreshold]**](SLOThreshold.md) | The thresholds (timeframes and associated targets) for this service level objective object. | 
**type** | [**slo_type.SLOType**](SLOType.md) |  | 
**created_at** | **int** | Creation timestamp (UNIX time in seconds)  Always included in service level objective responses. | [optional] [readonly] 
**creator** | [**creator.Creator**](Creator.md) |  | [optional] 
**description** | **str, none_type** | A user-defined description of the service level objective.  Always included in service level objective responses (but may be &#x60;null&#x60;). Optional in create/update requests. | [optional] 
**groups** | **[str]** | A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.  Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the &#x60;monitor_ids&#x60; field is one. | [optional] 
**id** | **str** | A unique identifier for the service level objective object.  Always included in service level objective responses. | [optional] [readonly] 
**modified_at** | **int** | Modification timestamp (UNIX time in seconds)  Always included in service level objective responses. | [optional] [readonly] 
**monitor_ids** | **[int]** | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is &#x60;monitor&#x60;**. | [optional] 
**query** | [**service_level_objective_query.ServiceLevelObjectiveQuery**](ServiceLevelObjectiveQuery.md) |  | [optional] 
**tags** | **[str]** | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


