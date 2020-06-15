# logs_status_remapper.LogsStatusRemapper

Use this Processor if you want to assign some attributes as the official status.  Each incoming status value is mapped as follows.    - Integers from 0 to 7 map to the Syslog severity standards   - Strings beginning with `emerg` or f (case-insensitive) map to `emerg` (0)   - Strings beginning with `a` (case-insensitive) map to `alert` (1)   - Strings beginning with `c` (case-insensitive) map to `critical` (2)   - Strings beginning with `err` (case-insensitive) map to `error` (3)   - Strings beginning with `w` (case-insensitive) map to `warning` (4)   - Strings beginning with `n` (case-insensitive) map to `notice` (5)   - Strings beginning with `i` (case-insensitive) map to `info` (6)   - Strings beginning with `d`, `trace` or `verbose` (case-insensitive) map to `debug` (7)   - Strings beginning with `o` or matching `OK` or `Success` (case-insensitive) map to OK   - All others map to `info` (6)    **Note:** If multiple log status remapper processors can be applied to a given log,   only the first one (according to the pipelines order) is taken into account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **[str]** | Array of source attributes. | 
**type** | [**logs_status_remapper_type.LogsStatusRemapperType**](LogsStatusRemapperType.md) |  | 
**is_enabled** | **bool** | Whether or not the processor is enabled. | [optional]  if omitted the server will use the default value of False
**name** | **str** | Name of the processor. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


