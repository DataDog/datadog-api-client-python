# slo_bulk_delete_response.SLOBulkDeleteResponse

The bulk partial delete service level objective object endpoint response.  This endpoint operates on multiple service level objective objects, so it may be partially successful. In such cases, the \"data\" and \"error\" fields in this response indicate which deletions succeeded and failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**slo_bulk_delete_response_data.SLOBulkDeleteResponseData**](SLOBulkDeleteResponseData.md) |  | [optional] 
**errors** | [**[slo_bulk_delete_response_errors.SLOBulkDeleteResponseErrors]**](SLOBulkDeleteResponseErrors.md) | Array of errors object returned. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


