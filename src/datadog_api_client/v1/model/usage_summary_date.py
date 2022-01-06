# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_summary_date_org import UsageSummaryDateOrg

    globals()["UsageSummaryDateOrg"] = UsageSummaryDateOrg


class UsageSummaryDate(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "agent_host_top99p": (int,),
            "apm_azure_app_service_host_top99p": (int,),
            "apm_host_top99p": (int,),
            "audit_logs_lines_indexed_sum": (int,),
            "avg_profiled_fargate_tasks": (int,),
            "aws_host_top99p": (int,),
            "aws_lambda_func_count": (int,),
            "aws_lambda_invocations_sum": (int,),
            "azure_app_service_top99p": (int,),
            "billable_ingested_bytes_sum": (int,),
            "browser_rum_lite_session_count_sum": (int,),
            "browser_rum_replay_session_count_sum": (int,),
            "browser_rum_units_sum": (int,),
            "container_avg": (int,),
            "container_hwm": (int,),
            "cspm_container_avg": (int,),
            "cspm_container_hwm": (int,),
            "cspm_host_top99p": (int,),
            "custom_ts_avg": (int,),
            "cws_container_count_avg": (int,),
            "cws_host_top99p": (int,),
            "date": (datetime,),
            "dbm_host_top99p": (int,),
            "dbm_queries_count_avg": (int,),
            "fargate_tasks_count_avg": (int,),
            "fargate_tasks_count_hwm": (int,),
            "gcp_host_top99p": (int,),
            "heroku_host_top99p": (int,),
            "incident_management_monthly_active_users_hwm": (int,),
            "indexed_events_count_sum": (int,),
            "infra_host_top99p": (int,),
            "ingested_events_bytes_sum": (int,),
            "iot_device_sum": (int,),
            "iot_device_top99p": (int,),
            "mobile_rum_lite_session_count_sum": (int,),
            "mobile_rum_session_count_android_sum": (int,),
            "mobile_rum_session_count_ios_sum": (int,),
            "mobile_rum_session_count_sum": (int,),
            "mobile_rum_units_sum": (int,),
            "netflow_indexed_events_count_sum": (int,),
            "npm_host_top99p": (int,),
            "opentelemetry_host_top99p": (int,),
            "orgs": ([UsageSummaryDateOrg],),
            "profiling_host_top99p": (int,),
            "rum_browser_and_mobile_session_count": (int,),
            "rum_session_count_sum": (int,),
            "rum_total_session_count_sum": (int,),
            "rum_units_sum": (int,),
            "sds_logs_scanned_bytes_sum": (int,),
            "sds_total_scanned_bytes_sum": (int,),
            "synthetics_browser_check_calls_count_sum": (int,),
            "synthetics_check_calls_count_sum": (int,),
            "trace_search_indexed_events_count_sum": (int,),
            "twol_ingested_events_bytes_sum": (int,),
            "vsphere_host_top99p": (int,),
        }

    attribute_map = {
        "agent_host_top99p": "agent_host_top99p",
        "apm_azure_app_service_host_top99p": "apm_azure_app_service_host_top99p",
        "apm_host_top99p": "apm_host_top99p",
        "audit_logs_lines_indexed_sum": "audit_logs_lines_indexed_sum",
        "avg_profiled_fargate_tasks": "avg_profiled_fargate_tasks",
        "aws_host_top99p": "aws_host_top99p",
        "aws_lambda_func_count": "aws_lambda_func_count",
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",
        "azure_app_service_top99p": "azure_app_service_top99p",
        "billable_ingested_bytes_sum": "billable_ingested_bytes_sum",
        "browser_rum_lite_session_count_sum": "browser_rum_lite_session_count_sum",
        "browser_rum_replay_session_count_sum": "browser_rum_replay_session_count_sum",
        "browser_rum_units_sum": "browser_rum_units_sum",
        "container_avg": "container_avg",
        "container_hwm": "container_hwm",
        "cspm_container_avg": "cspm_container_avg",
        "cspm_container_hwm": "cspm_container_hwm",
        "cspm_host_top99p": "cspm_host_top99p",
        "custom_ts_avg": "custom_ts_avg",
        "cws_container_count_avg": "cws_container_count_avg",
        "cws_host_top99p": "cws_host_top99p",
        "date": "date",
        "dbm_host_top99p": "dbm_host_top99p",
        "dbm_queries_count_avg": "dbm_queries_count_avg",
        "fargate_tasks_count_avg": "fargate_tasks_count_avg",
        "fargate_tasks_count_hwm": "fargate_tasks_count_hwm",
        "gcp_host_top99p": "gcp_host_top99p",
        "heroku_host_top99p": "heroku_host_top99p",
        "incident_management_monthly_active_users_hwm": "incident_management_monthly_active_users_hwm",
        "indexed_events_count_sum": "indexed_events_count_sum",
        "infra_host_top99p": "infra_host_top99p",
        "ingested_events_bytes_sum": "ingested_events_bytes_sum",
        "iot_device_sum": "iot_device_sum",
        "iot_device_top99p": "iot_device_top99p",
        "mobile_rum_lite_session_count_sum": "mobile_rum_lite_session_count_sum",
        "mobile_rum_session_count_android_sum": "mobile_rum_session_count_android_sum",
        "mobile_rum_session_count_ios_sum": "mobile_rum_session_count_ios_sum",
        "mobile_rum_session_count_sum": "mobile_rum_session_count_sum",
        "mobile_rum_units_sum": "mobile_rum_units_sum",
        "netflow_indexed_events_count_sum": "netflow_indexed_events_count_sum",
        "npm_host_top99p": "npm_host_top99p",
        "opentelemetry_host_top99p": "opentelemetry_host_top99p",
        "orgs": "orgs",
        "profiling_host_top99p": "profiling_host_top99p",
        "rum_browser_and_mobile_session_count": "rum_browser_and_mobile_session_count",
        "rum_session_count_sum": "rum_session_count_sum",
        "rum_total_session_count_sum": "rum_total_session_count_sum",
        "rum_units_sum": "rum_units_sum",
        "sds_logs_scanned_bytes_sum": "sds_logs_scanned_bytes_sum",
        "sds_total_scanned_bytes_sum": "sds_total_scanned_bytes_sum",
        "synthetics_browser_check_calls_count_sum": "synthetics_browser_check_calls_count_sum",
        "synthetics_check_calls_count_sum": "synthetics_check_calls_count_sum",
        "trace_search_indexed_events_count_sum": "trace_search_indexed_events_count_sum",
        "twol_ingested_events_bytes_sum": "twol_ingested_events_bytes_sum",
        "vsphere_host_top99p": "vsphere_host_top99p",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageSummaryDate - a model defined in OpenAPI

        Keyword Args:
            agent_host_top99p (int): [optional] Shows the 99th percentile of all agent hosts over all hours in the current date for all organizations.
            apm_azure_app_service_host_top99p (int): [optional] Shows the 99th percentile of all Azure app services using APM over all hours in the current date all organizations.
            apm_host_top99p (int): [optional] Shows the 99th percentile of all distinct APM hosts over all hours in the current date for all organizations.
            audit_logs_lines_indexed_sum (int): [optional] Shows the sum of audit logs lines indexed over all hours in the current date for all organizations.
            avg_profiled_fargate_tasks (int): [optional] The average profiled task count for Fargate Profiling.
            aws_host_top99p (int): [optional] Shows the 99th percentile of all AWS hosts over all hours in the current date for all organizations.
            aws_lambda_func_count (int): [optional] Shows the average of the number of functions that executed 1 or more times each hour in the current date for all organizations.
            aws_lambda_invocations_sum (int): [optional] Shows the sum of all AWS Lambda invocations over all hours in the current date for all organizations.
            azure_app_service_top99p (int): [optional] Shows the 99th percentile of all Azure app services over all hours in the current date for all organizations.
            billable_ingested_bytes_sum (int): [optional] Shows the sum of all log bytes ingested over all hours in the current date for all organizations.
            browser_rum_lite_session_count_sum (int): [optional] Shows the sum of all browser lite sessions over all hours in the current date for all organizations.
            browser_rum_replay_session_count_sum (int): [optional] Shows the sum of all browser replay sessions over all hours in the current date for all organizations.
            browser_rum_units_sum (int): [optional] Shows the sum of all browser RUM units over all hours in the current date for all organizations.
            container_avg (int): [optional] Shows the average of all distinct containers over all hours in the current date for all organizations.
            container_hwm (int): [optional] Shows the high-water mark of all distinct containers over all hours in the current date for all organizations.
            cspm_container_avg (int): [optional] Shows the average number of Cloud Security Posture Management containers over all hours in the current date for all organizations.
            cspm_container_hwm (int): [optional] Shows the high-water mark of Cloud Security Posture Management containers over all hours in the current date for all organizations.
            cspm_host_top99p (int): [optional] Shows the 99th percentile of all Cloud Security Posture Management hosts over all hours in the current date for all organizations.
            custom_ts_avg (int): [optional] Shows the average number of distinct custom metrics over all hours in the current date for all organizations.
            cws_container_count_avg (int): [optional] Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for all organizations.
            cws_host_top99p (int): [optional] Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for all organizations.
            date (datetime): [optional] The date for the usage.
            dbm_host_top99p (int): [optional] Shows the 99th percentile of all Database Monitoring hosts over all hours in the current date for all organizations.
            dbm_queries_count_avg (int): [optional] Shows the average of all normalized Database Monitoring queries over all hours in the current date for all organizations.
            fargate_tasks_count_avg (int): [optional] Shows the high-watermark of all Fargate tasks over all hours in the current date for all organizations.
            fargate_tasks_count_hwm (int): [optional] Shows the average of all Fargate tasks over all hours in the current date for all organizations.
            gcp_host_top99p (int): [optional] Shows the 99th percentile of all GCP hosts over all hours in the current date for all organizations.
            heroku_host_top99p (int): [optional] Shows the 99th percentile of all Heroku dynos over all hours in the current date for all organizations.
            incident_management_monthly_active_users_hwm (int): [optional] Shows the high-water mark of incident management monthly active users over all hours in the current date for all organizations.
            indexed_events_count_sum (int): [optional] Shows the sum of all log events indexed over all hours in the current date for all organizations.
            infra_host_top99p (int): [optional] Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for all organizations.
            ingested_events_bytes_sum (int): [optional] Shows the sum of all log bytes ingested over all hours in the current date for all organizations.
            iot_device_sum (int): [optional] Shows the sum of all IoT devices over all hours in the current date for all organizations.
            iot_device_top99p (int): [optional] Shows the 99th percentile of all IoT devices over all hours in the current date all organizations.
            mobile_rum_lite_session_count_sum (int): [optional] Shows the sum of all mobile lite sessions over all hours in the current date for all organizations.
            mobile_rum_session_count_android_sum (int): [optional] Shows the sum of all mobile RUM Sessions on Android over all hours in the current date for all organizations.
            mobile_rum_session_count_ios_sum (int): [optional] Shows the sum of all mobile RUM Sessions on iOS over all hours in the current date for all organizations.
            mobile_rum_session_count_sum (int): [optional] Shows the sum of all mobile RUM Sessions over all hours in the current date for all organizations
            mobile_rum_units_sum (int): [optional] Shows the sum of all mobile RUM units over all hours in the current date for all organizations.
            netflow_indexed_events_count_sum (int): [optional] Shows the sum of all Network flows indexed over all hours in the current date for all organizations.
            npm_host_top99p (int): [optional] Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for all organizations.
            opentelemetry_host_top99p (int): [optional] Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for all organizations.
            orgs ([UsageSummaryDateOrg]): [optional] Organizations associated with a user.
            profiling_host_top99p (int): [optional] Shows the 99th percentile of all profiled hosts over all hours in the current date for all organizations.
            rum_browser_and_mobile_session_count (int): [optional] Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current month for all organizations.
            rum_session_count_sum (int): [optional] Shows the sum of all browser RUM Sessions over all hours in the current date for all organizations
            rum_total_session_count_sum (int): [optional] Shows the sum of RUM Sessions (browser and mobile) over all hours in the current date for all organizations.
            rum_units_sum (int): [optional] Shows the sum of all browser and mobile RUM units over all hours in the current date for all organizations.
            sds_logs_scanned_bytes_sum (int): [optional] Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for all organizations.
            sds_total_scanned_bytes_sum (int): [optional] Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for all organizations.
            synthetics_browser_check_calls_count_sum (int): [optional] Shows the sum of all Synthetic browser tests over all hours in the current date for all organizations.
            synthetics_check_calls_count_sum (int): [optional] Shows the sum of all Synthetic API tests over all hours in the current date for all organizations.
            trace_search_indexed_events_count_sum (int): [optional] Shows the sum of all Indexed Spans indexed over all hours in the current date for all organizations.
            twol_ingested_events_bytes_sum (int): [optional] Shows the sum of all tracing without limits bytes ingested over all hours in the current date for all organizations.
            vsphere_host_top99p (int): [optional] Shows the 99th percentile of all vSphere hosts over all hours in the current date for all organizations.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSummaryDate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
