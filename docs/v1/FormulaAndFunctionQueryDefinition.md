# FormulaAndFunctionQueryDefinition

A formula and function query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**FormulaAndFunctionProcessQueryDataSource**](FormulaAndFunctionProcessQueryDataSource.md) |  | defaults to nulltype.Null
**query** | **str** | Metrics query definition. | defaults to nulltype.Null
**compute** | [**TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute**](TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute.md) |  | defaults to nulltype.Null
**metric** | **str** | Process metric name. | defaults to nulltype.Null
**aggregator** | [**FormulaAndFunctionMetricAggregation**](FormulaAndFunctionMetricAggregation.md) |  | [optional] 
**name** | **str** | Name of query for use in formulas. | [optional] 
**group_by** | [**[TimeSeriesFormulaAndFunctionEventQueryGroupBy]**](TimeSeriesFormulaAndFunctionEventQueryGroupBy.md) | Group by options. | [optional] 
**indexes** | **[str]** | An array of index names to query in the stream. Omit or use &#x60;[]&#x60; to query all indexes at once. | [optional] 
**search** | [**TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch**](TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch.md) |  | [optional] 
**is_normalized_cpu** | **bool** | Whether to normalize the CPU percentages. | [optional] 
**limit** | **int** | Number of hits to return. | [optional] 
**sort** | [**QuerySortOrder**](QuerySortOrder.md) |  | [optional] 
**tag_filters** | **[str]** | An array of tags to filter by. | [optional] 
**text_filter** | **str** | Text to use as filter. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


