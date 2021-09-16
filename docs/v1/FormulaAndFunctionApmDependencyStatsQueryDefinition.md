# FormulaAndFunctionApmDependencyStatsQueryDefinition

A formula and functions APM dependency stats query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**FormulaAndFunctionApmDependencyStatsDataSource**](FormulaAndFunctionApmDependencyStatsDataSource.md) |  | 
**env** | **str** | APM environment. | 
**name** | **str** | Name of query to use in formulas. | 
**operation_name** | **str** | Name of operation on service. | 
**resource_name** | **str** | APM resource. | 
**service** | **str** | APM service. | 
**stat** | [**FormulaAndFunctionApmDependencyStatName**](FormulaAndFunctionApmDependencyStatName.md) |  | 
**is_upstream** | **bool** | Determines whether stats for upstream or downstream dependencies should be queried. | [optional] 
**primary_tag_name** | **str** | The name of the second primary tag used within APM; required when &#x60;primary_tag_value&#x60; is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog. | [optional] 
**primary_tag_value** | **str** | Filter APM data by the second primary tag. &#x60;primary_tag_name&#x60; must also be specified. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


