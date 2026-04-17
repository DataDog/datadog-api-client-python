"""
Run a historical job returns "Status created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.historical_job_options import HistoricalJobOptions
from datadog_api_client.v2.model.historical_job_query import HistoricalJobQuery
from datadog_api_client.v2.model.job_definition import JobDefinition
from datadog_api_client.v2.model.run_historical_job_request import RunHistoricalJobRequest
from datadog_api_client.v2.model.run_historical_job_request_attributes import RunHistoricalJobRequestAttributes
from datadog_api_client.v2.model.run_historical_job_request_data import RunHistoricalJobRequestData
from datadog_api_client.v2.model.run_historical_job_request_data_type import RunHistoricalJobRequestDataType
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
    SecurityMonitoringRuleEvaluationWindow,
)
from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
    SecurityMonitoringRuleMaxSignalDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

body = RunHistoricalJobRequest(
    data=RunHistoricalJobRequestData(
        type=RunHistoricalJobRequestDataType.HISTORICALDETECTIONSJOBCREATE,
        attributes=RunHistoricalJobRequestAttributes(
            job_definition=JobDefinition(
                type="log_detection",
                name="Excessive number of failed attempts.",
                queries=[
                    HistoricalJobQuery(
                        query="source:non_existing_src_weekend",
                        aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
                        group_by_fields=[],
                        distinct_fields=[],
                    ),
                ],
                cases=[
                    SecurityMonitoringRuleCaseCreate(
                        name="Condition 1",
                        status=SecurityMonitoringRuleSeverity.INFO,
                        notifications=[],
                        condition="a > 1",
                    ),
                ],
                options=HistoricalJobOptions(
                    keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
                    max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
                    evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
                ),
                message="A large number of failed login attempts.",
                tags=[],
                _from=1730387522611,
                to=1730387532611,
                index="main",
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["run_historical_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.run_historical_job(body=body)

    print(response)
