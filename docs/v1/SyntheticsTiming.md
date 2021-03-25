# SyntheticsTiming

Object containing all metrics and their values collected for a Synthetic API test. Learn more about those metrics in [Synthetics documentation](https://docs.datadoghq.com/synthetics/#metrics).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **float** | The duration in millisecond of the DNS lookup. | [optional] 
**download** | **float** | The time in millisecond to download the response. | [optional] 
**first_byte** | **float** | The time in millisecond to first byte. | [optional] 
**handshake** | **float** | The duration in millisecond of the TLS handshake. | [optional] 
**redirect** | **float** | The time in millisecond spent during redirections. | [optional] 
**ssl** | **float** | The duration in millisecond of the TLS handshake. | [optional] 
**tcp** | **float** | Time in millisecond to establish the TCP connection. | [optional] 
**total** | **float** | The overall time in millisecond the request took to be processed. | [optional] 
**wait** | **float** | Time spent in millisecond waiting for a response. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


