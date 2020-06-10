# logs_trace_remapper.LogsTraceRemapper

There are two ways to improve correlation between application traces and logs.    1. Follow the documentation on [how to inject a trace ID in the application logs](https://docs.datadoghq.com/tracing/connect_logs_and_traces)   and by default log integrations take care of all the rest of the setup.    2. Use the Trace remapper processor to define a log attribute as its associated trace ID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**logs_trace_remapper_type.LogsTraceRemapperType**](LogsTraceRemapperType.md) |  | 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**sources** | **[str]** | Array of source attributes. | [optional]  if omitted the server will use the default value of ["dd.trace_id"]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


