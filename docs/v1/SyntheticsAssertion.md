# synthetics_assertion.SyntheticsAssertion

Object describing the assertions type, their associated operator, which property they apply , and upon which target.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**synthetics_assertion_operator.SyntheticsAssertionOperator**](SyntheticsAssertionOperator.md) |  | 
**type** | [**synthetics_assertion_type.SyntheticsAssertionType**](SyntheticsAssertionType.md) |  | 
**_property** | **str** | The associated assertion property. | [optional] 
**target** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Target to apply the assertion to. It can be a string, a number, or a Date. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


