# UsageSummaryDateOrg

Global hourly report of all data billed by Datadog for a given organization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_host_top99p** | **int** | Shows the 99th percentile of all agent hosts over all hours in the current date for the given org. | [optional] 
**apm_host_top99p** | **int** | Shows the 99th percentile of all distinct APM hosts over all hours in the current date for the given org. | [optional] 
**aws_host_top99p** | **int** | Shows the 99th percentile of all AWS hosts over all hours in the current date for the given org. | [optional] 
**aws_lambda_func_count** | **int** | Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org. | [optional] 
**aws_lambda_invocations_sum** | **int** | Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org. | [optional] 
**billable_ingested_bytes_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current date for the given org. | [optional] 
**container_avg** | **int** | Shows the average of all distinct containers over all hours in the current date for the given org. | [optional] 
**container_hwm** | **int** | Shows the high watermark of all distinct containers over all hours in the current date for the given org. | [optional] 
**custom_ts_avg** | **int** | Shows the average number of distinct custom metrics over all hours in the current date for the given org. | [optional] 
**fargate_tasks_count_avg** | **int** | The average task count for Fargate. | [optional] 
**fargate_tasks_count_hwm** | **int** | Shows the high watermark of all Fargate tasks over all hours in the current date for the given org. | [optional] 
**gcp_host_top99p** | **int** | Shows the 99th percentile of all GCP hosts over all hours in the current date for the given org. | [optional] 
**id** | **str** | The organization id. | [optional] 
**indexed_events_count_sum** | **int** | Shows the sum of all log events indexed over all hours in the current date for the given org. | [optional] 
**infra_host_top99p** | **int** | Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for the given org. | [optional] 
**ingested_events_bytes_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current date for the given org. | [optional] 
**mobile_rum_session_count_sum** | **int** | Shows the sum of all mobile RUM Sessions over all hours in the current date for the given org. | [optional] 
**name** | **str** | The organization name. | [optional] 
**netflow_indexed_events_count_sum** | **int** | Shows the sum of all Network flows indexed over all hours in the current date for the given org. | [optional] 
**npm_host_top99p** | **int** | Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for the given org. | [optional] 
**profiling_host_top99p** | **int** | Shows the 99th percentile of all profiled hosts over all hours in the current date for the given org. | [optional] 
**public_id** | **str** | The organization public id. | [optional] 
**rum_session_count_sum** | **int** | Shows the sum of all browser RUM Sessions over all hours in the current date for the given org. | [optional] 
**synthetics_browser_check_calls_count_sum** | **int** | Shows the sum of all Synthetic browser tests over all hours in the current date for the given org. | [optional] 
**synthetics_check_calls_count_sum** | **int** | Shows the sum of all Synthetic API tests over all hours in the current date for the given org. | [optional] 
**trace_search_indexed_events_count_sum** | **int** | Shows the sum of all Indexed Spans indexed over all hours in the current date for the given org. | [optional] 
**twol_ingested_events_bytes_sum** | **int** | Shows the sum of all tracing without limits bytes ingested over all hours in the current date for the given org. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


