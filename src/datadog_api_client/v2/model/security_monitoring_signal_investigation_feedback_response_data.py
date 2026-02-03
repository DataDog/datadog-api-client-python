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
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_response_attributes import (
        SecurityMonitoringSignalInvestigationFeedbackResponseAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_type import (
        SecurityMonitoringSignalInvestigationFeedbackType,
    )


class SecurityMonitoringSignalInvestigationFeedbackResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_response_attributes import (
            SecurityMonitoringSignalInvestigationFeedbackResponseAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_type import (
            SecurityMonitoringSignalInvestigationFeedbackType,
        )

        return {
            "attributes": (SecurityMonitoringSignalInvestigationFeedbackResponseAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSignalInvestigationFeedbackType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalInvestigationFeedbackResponseAttributes,
        id: str,
        type: SecurityMonitoringSignalInvestigationFeedbackType,
        **kwargs,
    ):
        """
        Data containing investigation feedback.

        :param attributes: Attributes of investigation feedback.
        :type attributes: SecurityMonitoringSignalInvestigationFeedbackResponseAttributes

        :param id: The unique ID of the investigation.
        :type id: str

        :param type: The type of feedback.
        :type type: SecurityMonitoringSignalInvestigationFeedbackType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
