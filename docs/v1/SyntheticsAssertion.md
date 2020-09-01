# SyntheticsAssertion

Object describing the assertions type, their associated operator, which property they apply, and upon which target.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**SyntheticsAssertionJSONPathOperator**](SyntheticsAssertionJSONPathOperator.md) |  | defaults to nulltype.Null
**type** | [**SyntheticsAssertionType**](SyntheticsAssertionType.md) |  | defaults to nulltype.Null
**_property** | **str** | The associated assertion property. | [optional] 
**target** | [**SyntheticsAssertionJSONPathTargetTarget**](SyntheticsAssertionJSONPathTargetTarget.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


