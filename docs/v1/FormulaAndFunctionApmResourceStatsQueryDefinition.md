# FormulaAndFunctionApmResourceStatsQueryDefinition

APM resource stats query using formulas and functions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**FormulaAndFunctionApmResourceStatsDataSource**](FormulaAndFunctionApmResourceStatsDataSource.md) |  | 
**env** | **str** | APM environment. | 
**name** | **str** | Name of this query to use in formulas. | 
**service** | **str** | APM service name. | 
**stat** | [**FormulaAndFunctionApmResourceStatName**](FormulaAndFunctionApmResourceStatName.md) |  | 
**group_by** | **[str]** | Array of fields to group results by. | [optional] 
**operation_name** | **str** | Name of operation on service. | [optional] 
**primary_tag_name** | **str** | Name of the second primary tag used within APM. Required when &#x60;primary_tag_value&#x60; is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog | [optional] 
**primary_tag_value** | **str** | Value of the second primary tag by which to filter APM data. &#x60;primary_tag_name&#x60; must also be specified. | [optional] 
**resource_name** | **str** | APM resource name. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


