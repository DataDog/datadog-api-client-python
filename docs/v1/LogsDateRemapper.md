# logs_date_remapper.LogsDateRemapper

As Datadog receives logs, it timestamps them using the value(s) from any of these default attributes.    - `timestamp`   - `date`   - `_timestamp`   - `Timestamp`   - `eventTime`   - `published_date`    If your logs put their dates in an attribute not in this list,   use the log date Remapper Processor to define their date attribute as the official log timestamp.   The recognized date formats are ISO8601, UNIX (the milliseconds EPOCH format), and RFC3164.    **Note:** If your logs don’t contain any of the default attributes   and you haven’t defined your own date attribute, Datadog timestamps   the logs with the date it received them.    If multiple log date remapper processors can be applied to a given log,   only the first one (according to the pipelines order) is taken into account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **[str]** | Array of source attributes. | 
**type** | [**logs_date_remapper_type.LogsDateRemapperType**](LogsDateRemapperType.md) |  | 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


