# host.Host

Object representing a host.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **[str]** | Host aliases collected by Datadog. | [optional] 
**apps** | **[str]** | The Datadog integrations reporting metrics for the host. | [optional] 
**aws_name** | **str** | AWS name of your host. | [optional] 
**host_name** | **str** | The host name. | [optional] 
**id** | **int** | The host ID. | [optional] 
**is_muted** | **bool** | If a host is muted or unmuted. | [optional] 
**last_reported_time** | **int** | Last time the host reported a metric data point. | [optional] 
**meta** | [**host_meta.HostMeta**](HostMeta.md) |  | [optional] 
**metrics** | [**host_metrics.HostMetrics**](HostMetrics.md) |  | [optional] 
**mute_timeout** | **int** | Timeout of the mute applied to your host. | [optional] 
**name** | **str** | The host name. | [optional] 
**sources** | **[str]** | Source or cloud provider associated with your host. | [optional] 
**tags_by_source** | **{str: ([str],)}** | List of tags for each source (AWS, Datadog Agent, Chef..). | [optional] 
**up** | **bool** | Displays UP when the expected metrics are received and displays &#x60;???&#x60; if no metrics are received. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


