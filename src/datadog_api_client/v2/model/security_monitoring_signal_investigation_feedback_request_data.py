# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_request_attributes import (
        SecurityMonitoringSignalInvestigationFeedbackRequestAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_type import (
        SecurityMonitoringSignalInvestigationFeedbackType,
    )


class SecurityMonitoringSignalInvestigationFeedbackRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_request_attributes import (
            SecurityMonitoringSignalInvestigationFeedbackRequestAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_type import (
            SecurityMonitoringSignalInvestigationFeedbackType,
        )

        return {
            "attributes": (SecurityMonitoringSignalInvestigationFeedbackRequestAttributes,),
            "type": (SecurityMonitoringSignalInvestigationFeedbackType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalInvestigationFeedbackRequestAttributes,
        type: SecurityMonitoringSignalInvestigationFeedbackType,
        **kwargs,
    ):
        """
        Data for submitting investigation feedback.

        :param attributes: Attributes for investigation feedback.
        :type attributes: SecurityMonitoringSignalInvestigationFeedbackRequestAttributes

        :param type: The type of feedback.
        :type type: SecurityMonitoringSignalInvestigationFeedbackType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
