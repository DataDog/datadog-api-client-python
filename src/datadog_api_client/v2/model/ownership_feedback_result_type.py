# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipFeedbackResultType(ModelSimple):
    """
    The type of the ownership feedback result resource. The value should always be `ownership_feedback_result`.

    :param value: If omitted defaults to "ownership_feedback_result". Must be one of ["ownership_feedback_result"].
    :type value: str
    """

    allowed_values = {
        "ownership_feedback_result",
    }
    OWNERSHIP_FEEDBACK_RESULT: ClassVar["OwnershipFeedbackResultType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipFeedbackResultType.OWNERSHIP_FEEDBACK_RESULT = OwnershipFeedbackResultType("ownership_feedback_result")
