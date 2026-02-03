# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_section import (
        SecurityMonitoringSignalInvestigationFeedbackSection,
    )


class SecurityMonitoringSignalInvestigationFeedbackResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_section import (
            SecurityMonitoringSignalInvestigationFeedbackSection,
        )

        return {
            "feedback": (str,),
            "feedback_content": ([SecurityMonitoringSignalInvestigationFeedbackSection],),
            "investigation_id": (str,),
            "rating": (str,),
            "signal_id": (str,),
        }

    attribute_map = {
        "feedback": "feedback",
        "feedback_content": "feedback_content",
        "investigation_id": "investigation_id",
        "rating": "rating",
        "signal_id": "signal_id",
    }

    def __init__(
        self_,
        feedback: str,
        investigation_id: str,
        signal_id: str,
        feedback_content: Union[List[SecurityMonitoringSignalInvestigationFeedbackSection], UnsetType] = unset,
        rating: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of investigation feedback.

        :param feedback: The feedback text.
        :type feedback: str

        :param feedback_content: Structured feedback content.
        :type feedback_content: [SecurityMonitoringSignalInvestigationFeedbackSection], optional

        :param investigation_id: The unique ID of the investigation.
        :type investigation_id: str

        :param rating: The rating value.
        :type rating: str, optional

        :param signal_id: The unique ID of the security signal.
        :type signal_id: str
        """
        if feedback_content is not unset:
            kwargs["feedback_content"] = feedback_content
        if rating is not unset:
            kwargs["rating"] = rating
        super().__init__(kwargs)

        self_.feedback = feedback
        self_.investigation_id = investigation_id
        self_.signal_id = signal_id
