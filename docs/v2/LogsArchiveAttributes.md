# LogsArchiveAttributes

The attributes associated with the archive.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**LogsArchiveDestination**](LogsArchiveDestination.md) |  | 
**name** | **str** | The archive name. | 
**query** | **str** | The archive query/filter. Logs matching this query are included in the archive. | 
**include_tags** | **bool** | To store the tags in the archive, set the value \&quot;true\&quot;. If it is set to \&quot;false\&quot;, the tags will be deleted when the logs are sent to the archive. | [optional]  if omitted the server will use the default value of False
**rehydration_tags** | **[str]** | An array of tags to add to rehydrated logs from an archive. | [optional] 
**state** | [**LogsArchiveState**](LogsArchiveState.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


