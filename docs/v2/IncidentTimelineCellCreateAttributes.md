# IncidentTimelineCellCreateAttributes

The timeline cell's attributes for a create request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_type** | [**IncidentTimelineCellMarkdownContentType**](IncidentTimelineCellMarkdownContentType.md) |  | defaults to nulltype.Null
**content** | [**IncidentTimelineCellMarkdownCreateAttributesContent**](IncidentTimelineCellMarkdownCreateAttributesContent.md) |  | defaults to nulltype.Null
**important** | **bool** | A flag indicating whether the timeline cell is important and should be highlighted. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


