# downtime_recurrence.DowntimeRecurrence

An object defining the recurrence of the downtime.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | How often to repeat as an integer. For example, to repeat every 3 days, select a type of &#x60;days&#x60; and a period of &#x60;3&#x60;. | [optional] 
**type** | **str** | The type of recurrence. Choose from &#x60;days&#x60;, &#x60;weeks&#x60;, &#x60;months&#x60;, &#x60;years&#x60;. | [optional] 
**until_date** | **int, none_type** | The date at which the recurrence should end as a POSIX timestamp. &#x60;until_occurences&#x60; and &#x60;until_date&#x60; are mutually exclusive. | [optional] 
**until_occurrences** | **int, none_type** | How many times the downtime is rescheduled. &#x60;until_occurences&#x60; and &#x60;until_date&#x60; are mutually exclusive. | [optional] 
**week_days** | **[str]** | A list of week days to repeat on. Choose from &#x60;Mon&#x60;, &#x60;Tue&#x60;, &#x60;Wed&#x60;, &#x60;Thu&#x60;, &#x60;Fri&#x60;, &#x60;Sat&#x60; or &#x60;Sun&#x60;. Only applicable when type is weeks. First letter must be capitalized. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


