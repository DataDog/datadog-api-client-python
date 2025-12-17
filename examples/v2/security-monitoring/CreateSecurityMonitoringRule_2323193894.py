"""
Create a detection rule with detection method 'anomaly_detection' returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options import (
    SecurityMonitoringRuleAnomalyDetectionOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_bucket_duration import (
    SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_detection_tolerance import (
    SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance,
)
from datadog_api_client.v2.model.security_monitoring_rule_anomaly_detection_options_learning_duration import (
    SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
    SecurityMonitoringRuleEvaluationWindow,
)
from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
    SecurityMonitoringRuleMaxSignalDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_standard_data_source import SecurityMonitoringStandardDataSource
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

body = SecurityMonitoringStandardRuleCreatePayload(
    name="Example-Security-Monitoring",
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
    is_enabled=True,
    queries=[
        SecurityMonitoringStandardRuleQuery(
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            data_source=SecurityMonitoringStandardDataSource.LOGS,
            distinct_fields=[],
            group_by_fields=[
                "@usr.email",
                "@network.client.ip",
            ],
            has_optional_group_by_fields=False,
            name="",
            query="service:app status:error",
        ),
    ],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
            condition="a > 0.995",
        ),
    ],
    message="An anomaly detection rule",
    options=SecurityMonitoringRuleOptions(
        detection_method=SecurityMonitoringRuleDetectionMethod.ANOMALY_DETECTION,
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
        anomaly_detection_options=SecurityMonitoringRuleAnomalyDetectionOptions(
            bucket_duration=SecurityMonitoringRuleAnomalyDetectionOptionsBucketDuration.FIVE_MINUTES,
            learning_duration=SecurityMonitoringRuleAnomalyDetectionOptionsLearningDuration.ONE_DAY,
            detection_tolerance=SecurityMonitoringRuleAnomalyDetectionOptionsDetectionTolerance.THREE,
            learning_period_baseline=10,
        ),
    ),
    tags=[],
    filters=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
