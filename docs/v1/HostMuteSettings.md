# host_mute_settings.HostMuteSettings

Combination of settings to mute a host.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** | POSIX timestamp in seconds when the host is unmuted. If omitted, the host remains muted until explicitly unmuted. | [optional] 
**message** | **str** | Message to associate with the muting of this host. | [optional] 
**override** | **bool** | If true and the host is already muted, replaces existing host mute settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


