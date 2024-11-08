"""
Convert a job result to a signal returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.convert_job_results_to_signals_attributes import ConvertJobResultsToSignalsAttributes
from datadog_api_client.v2.model.convert_job_results_to_signals_data import ConvertJobResultsToSignalsData
from datadog_api_client.v2.model.convert_job_results_to_signals_data_type import ConvertJobResultsToSignalsDataType
from datadog_api_client.v2.model.convert_job_results_to_signals_request import ConvertJobResultsToSignalsRequest
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

body = ConvertJobResultsToSignalsRequest(
    data=ConvertJobResultsToSignalsData(
        attributes=ConvertJobResultsToSignalsAttributes(
            job_result_ids=[
                "",
            ],
            notifications=[
                "",
            ],
            signal_message="A large number of failed login attempts.",
            signal_severity=SecurityMonitoringRuleSeverity.CRITICAL,
        ),
        type=ConvertJobResultsToSignalsDataType.HISTORICALDETECTIONSJOBRESULTSIGNALCONVERSION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["convert_job_result_to_signal"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.convert_job_result_to_signal(body=body)
