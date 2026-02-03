"""
Update investigation feedback returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_metric import (
    SecurityMonitoringSignalInvestigationFeedbackMetric,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_request import (
    SecurityMonitoringSignalInvestigationFeedbackRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_request_attributes import (
    SecurityMonitoringSignalInvestigationFeedbackRequestAttributes,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_request_data import (
    SecurityMonitoringSignalInvestigationFeedbackRequestData,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_section import (
    SecurityMonitoringSignalInvestigationFeedbackSection,
)
from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_type import (
    SecurityMonitoringSignalInvestigationFeedbackType,
)

body = SecurityMonitoringSignalInvestigationFeedbackRequest(
    data=SecurityMonitoringSignalInvestigationFeedbackRequestData(
        attributes=SecurityMonitoringSignalInvestigationFeedbackRequestAttributes(
            feedback="positive",
            feedback_content=[
                SecurityMonitoringSignalInvestigationFeedbackSection(
                    id="section-1",
                    metrics=[
                        SecurityMonitoringSignalInvestigationFeedbackMetric(
                            placeholder="Enter your feedback here",
                            prompt="How helpful was this investigation?",
                            response="Very helpful",
                            type="sentiment",
                        ),
                    ],
                    title="Investigation Quality",
                ),
            ],
            incomplete=False,
            rating="positive",
            signal_id="AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
            type="metrics",
        ),
        type=SecurityMonitoringSignalInvestigationFeedbackType.INVESTIGATION_FEEDBACK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_investigation_feedback"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.update_investigation_feedback(body=body)
