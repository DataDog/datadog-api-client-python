# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSignalInvestigationFeedbackType(ModelSimple):
    """
    The type of feedback.

    :param value: If omitted defaults to "investigation_feedback". Must be one of ["investigation_feedback"].
    :type value: str
    """

    allowed_values = {
        "investigation_feedback",
    }
    INVESTIGATION_FEEDBACK: ClassVar["SecurityMonitoringSignalInvestigationFeedbackType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalInvestigationFeedbackType.INVESTIGATION_FEEDBACK = (
    SecurityMonitoringSignalInvestigationFeedbackType("investigation_feedback")
)
