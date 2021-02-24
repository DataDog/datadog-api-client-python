# FormulaAndFunctionProcessQueryDefinition

Process query using formulas and functions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**FormulaAndFunctionProcessQueryDataSource**](FormulaAndFunctionProcessQueryDataSource.md) |  | 
**metric** | **str** | Process metric name. | 
**aggregator** | [**FormulaAndFunctionMetricAggregation**](FormulaAndFunctionMetricAggregation.md) |  | [optional] 
**is_normalized_cpu** | **bool** | Whether to normalize the CPU percentages. | [optional] 
**limit** | **int** | Number of hits to return. | [optional] 
**name** | **str** | Name of query for use in formulas. | [optional] 
**sort** | [**QuerySortOrder**](QuerySortOrder.md) |  | [optional] 
**tag_filters** | **[str]** | An array of tags to filter by. | [optional] 
**text_filter** | **str** | Text to use as filter. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


