# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipFeedbackAction(ModelSimple):
    """
    The feedback action to apply to an inference.

    :param value: Must be one of ["confirm", "reject", "correct", "persist"].
    :type value: str
    """

    allowed_values = {
        "confirm",
        "reject",
        "correct",
        "persist",
    }
    CONFIRM: ClassVar["OwnershipFeedbackAction"]
    REJECT: ClassVar["OwnershipFeedbackAction"]
    CORRECT: ClassVar["OwnershipFeedbackAction"]
    PERSIST: ClassVar["OwnershipFeedbackAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipFeedbackAction.CONFIRM = OwnershipFeedbackAction("confirm")
OwnershipFeedbackAction.REJECT = OwnershipFeedbackAction("reject")
OwnershipFeedbackAction.CORRECT = OwnershipFeedbackAction("correct")
OwnershipFeedbackAction.PERSIST = OwnershipFeedbackAction("persist")
