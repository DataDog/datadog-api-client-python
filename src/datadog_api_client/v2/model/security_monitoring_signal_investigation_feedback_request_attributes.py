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


class SecurityMonitoringSignalInvestigationFeedbackRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_feedback_section import (
            SecurityMonitoringSignalInvestigationFeedbackSection,
        )

        return {
            "feedback": (str,),
            "feedback_content": ([SecurityMonitoringSignalInvestigationFeedbackSection],),
            "incomplete": (bool,),
            "rating": (str,),
            "signal_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "feedback": "feedback",
        "feedback_content": "feedback_content",
        "incomplete": "incomplete",
        "rating": "rating",
        "signal_id": "signal_id",
        "type": "type",
    }

    def __init__(
        self_,
        feedback: str,
        signal_id: str,
        feedback_content: Union[List[SecurityMonitoringSignalInvestigationFeedbackSection], UnsetType] = unset,
        incomplete: Union[bool, UnsetType] = unset,
        rating: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for investigation feedback.

        :param feedback: The feedback text.
        :type feedback: str

        :param feedback_content: Structured feedback content.
        :type feedback_content: [SecurityMonitoringSignalInvestigationFeedbackSection], optional

        :param incomplete: Whether the feedback is incomplete.
        :type incomplete: bool, optional

        :param rating: The rating value.
        :type rating: str, optional

        :param signal_id: The unique ID of the security signal.
        :type signal_id: str

        :param type: The type of feedback.
        :type type: str, optional
        """
        if feedback_content is not unset:
            kwargs["feedback_content"] = feedback_content
        if incomplete is not unset:
            kwargs["incomplete"] = incomplete
        if rating is not unset:
            kwargs["rating"] = rating
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.feedback = feedback
        self_.signal_id = signal_id
