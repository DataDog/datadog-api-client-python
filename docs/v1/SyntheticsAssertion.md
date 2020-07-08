# synthetics_assertion.SyntheticsAssertion

Object describing the assertions type, their associated operator, which property they apply, and upon which target.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**synthetics_assertion_json_path_operator.SyntheticsAssertionJSONPathOperator**](SyntheticsAssertionJSONPathOperator.md) |  | defaults to nulltype.Null
**type** | [**synthetics_assertion_type.SyntheticsAssertionType**](SyntheticsAssertionType.md) |  | defaults to nulltype.Null
**_property** | **str** | The associated assertion property. | [optional] 
**target** | [**synthetics_assertion_json_path_target_target.SyntheticsAssertionJSONPathTargetTarget**](SyntheticsAssertionJSONPathTargetTarget.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


