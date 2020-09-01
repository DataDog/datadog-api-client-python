# LogsPipeline

Pipelines and processors operate on incoming logs, parsing and transforming them into structured attributes for easier querying.  **Note**: These endpoints are only available for admin users. Make sure to use an application key created by an admin.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the pipeline. | 
**filter** | [**LogsFilter**](LogsFilter.md) |  | [optional] 
**id** | **str** | ID of the pipeline. | [optional] [readonly] 
**is_enabled** | **bool** | Whether or not the pipeline is enabled. | [optional] 
**is_read_only** | **bool** | Whether or not the pipeline can be edited. | [optional] [readonly] 
**processors** | [**[LogsProcessor]**](LogsProcessor.md) | Ordered list of processors in this pipeline. | [optional] 
**type** | **str** | Type of pipeline. | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


