# FormulaAndFunctionQueryDefinition

A formula and function query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregator** | [**FormulaAndFunctionMetricAggregation**](FormulaAndFunctionMetricAggregation.md) |  | [optional] 
**group_by** | [**[FormulaAndFunctionEventQueryGroupBy]**](FormulaAndFunctionEventQueryGroupBy.md) | Group by options. | [optional] 
**indexes** | **[str]** | An array of index names to query in the stream. Omit or use &#x60;[]&#x60; to query all indexes at once. | [optional] 
**search** | [**FormulaAndFunctionEventQueryDefinitionSearch**](FormulaAndFunctionEventQueryDefinitionSearch.md) |  | [optional] 
**is_normalized_cpu** | **bool** | Whether to normalize the CPU percentages. | [optional] 
**limit** | **int** | Number of hits to return. | [optional] 
**sort** | [**QuerySortOrder**](QuerySortOrder.md) |  | [optional] 
**tag_filters** | **[str]** | An array of tags to filter by. | [optional] 
**text_filter** | **str** | Text to use as filter. | [optional] 
**data_source** | [**FormulaAndFunctionProcessQueryDataSource**](FormulaAndFunctionProcessQueryDataSource.md) |  | [optional] 
**name** | **str** | Name of query for use in formulas. | [optional] 
**query** | **str** | Metrics query definition. | [optional] 
**compute** | [**FormulaAndFunctionEventQueryDefinitionCompute**](FormulaAndFunctionEventQueryDefinitionCompute.md) |  | [optional] 
**metric** | **str** | Process metric name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


