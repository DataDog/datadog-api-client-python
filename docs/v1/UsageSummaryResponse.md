# UsageSummaryResponse

Response with hourly report of all data billed by Datadog all organizations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_host_top99p_sum** | **int** | Shows the 99th percentile of all agent hosts over all hours in the current month(s) for all organizations. | [optional] 
**apm_host_top99p_sum** | **int** | Shows the 99th percentile of all distinct APM hosts over all hours in the current month(s) for all organizations. | [optional] 
**aws_host_top99p_sum** | **int** | Shows the 99th percentile of all AWS hosts over all hours in the current month(s) for all organizations. | [optional] 
**aws_lambda_func_count** | **int** | Shows the average of the number of functions that executed 1 or more times each hour in the current month(s) for all organizations. | [optional] 
**aws_lambda_invocations_sum** | **int** | Shows the sum of all AWS Lambda invocations over all hours in the current month(s) for all organizations. | [optional] 
**azure_app_service_top99p_sum** | **int** | Shows the 99th percentile of all Azure app services over all hours in the current month(s) for all organizations. | [optional] 
**azure_host_top99p_sum** | **int** | Shows the 99th percentile of all Azure hosts over all hours in the current month(s) for all organizations. | [optional] 
**billable_ingested_bytes_agg_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current month(s) for all organizations. | [optional] 
**container_avg_sum** | **int** | Shows the average of all distinct containers over all hours in the current month(s) for all organizations. | [optional] 
**container_hwm_sum** | **int** | Shows the high watermark of all distinct containers over all hours in the current month(s) for all organizations. | [optional] 
**custom_ts_sum** | **int** | Shows the average number of distinct custom metrics over all hours in the current month(s) for all organizations. | [optional] 
**end_date** | **datetime** | Shows the last date of usage in the current month(s) for all organizations. | [optional] 
**fargate_tasks_count_avg_sum** | **int** | Shows the average of all Fargate tasks over all hours in the current month(s) for all organizations. | [optional] 
**fargate_tasks_count_hwm_sum** | **int** | Shows the high watermark of all Fargate tasks over all hours in the current month(s) for all organizations. | [optional] 
**gcp_host_top99p_sum** | **int** | Shows the 99th percentile of all GCP hosts over all hours in the current month(s) for all organizations. | [optional] 
**indexed_events_count_agg_sum** | **int** | Shows the sum of all log events indexed over all hours in the current month(s) for all organizations. | [optional] 
**infra_host_top99p_sum** | **int** | Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current month(s) for all organizations. | [optional] 
**ingested_events_bytes_agg_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current month(s) for all organizations. | [optional] 
**last_updated** | **datetime** | Shows the the most recent hour in the current month(s) for all organizations for which all usages were calculated. | [optional] 
**mobile_rum_session_count_agg_sum** | **int** | Shows the sum of all mobile RUM Sessions over all hours in the current month(s) for all organizations. | [optional] 
**netflow_indexed_events_count_agg_sum** | **int** | Shows the sum of all Network flows indexed over all hours in the current month(s) for all organizations. | [optional] 
**npm_host_top99p_sum** | **int** | Shows the 99th percentile of all distinct Networks hosts over all hours in the current month(s) for all organizations. | [optional] 
**profiling_container_agent_count_avg** | **int** | Shows the average number of profiled containers over all hours in the current month(s) for all organizations. | [optional] 
**profiling_host_count_top99p_sum** | **int** | Shows the 99th percentile of all profiled hosts over all hours in the current month(s) for all organizations. | [optional] 
**rum_session_count_agg_sum** | **int** | Shows the sum of all browser RUM Sessions over all hours in the current month(s) for all organizations. | [optional] 
**start_date** | **datetime** | Shows the first date of usage in the current month(s) for all organizations. | [optional] 
**synthetics_browser_check_calls_count_agg_sum** | **int** | Shows the sum of all Synthetic browser tests over all hours in the current month(s) for all organizations. | [optional] 
**synthetics_check_calls_count_agg_sum** | **int** | Shows the sum of all Synthetic API tests over all hours in the current month(s) for all organizations. | [optional] 
**trace_search_indexed_events_count_agg_sum** | **int** | Shows the sum of all Indexed Spans indexed over all hours in the current month(s) for all organizations. | [optional] 
**twol_ingested_events_bytes_agg_sum** | **int** | Shows the sum of all tracing without limits bytes ingested over all hours in the current month(s) for all organizations. | [optional] 
**usage** | [**[UsageSummaryDate]**](UsageSummaryDate.md) | An array of objects regarding hourly usage. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


