# logs_pipeline_processor.LogsPipelineProcessor

Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps. For example, first use a high-level filtering such as team and then a second level of filtering based on the integration, service, or any other tag or attribute.  A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**logs_pipeline_processor_type.LogsPipelineProcessorType**](LogsPipelineProcessorType.md) |  | 
**filter** | [**logs_filter.LogsFilter**](LogsFilter.md) |  | [optional] 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 
**processors** | [**[logs_processor.LogsProcessor]**](LogsProcessor.md) | Ordered list of processors in this pipeline. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


