# logs_archive_destination.LogsArchiveDestination

An archive's destination.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | The container where the archive will be stored. | defaults to nulltype.Null
**integration** | [**logs_archive_integration_s3.LogsArchiveIntegrationS3**](LogsArchiveIntegrationS3.md) |  | defaults to nulltype.Null
**storage_account** | **str** | The associated storage account. | defaults to nulltype.Null
**type** | [**logs_archive_destination_s3_type.LogsArchiveDestinationS3Type**](LogsArchiveDestinationS3Type.md) |  | defaults to nulltype.Null
**bucket** | **str** | The bucket where the archive will be stored. | defaults to nulltype.Null
**path** | **str** | The archive path. | [optional] 
**region** | **str** | The region where the archive will be stored. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


