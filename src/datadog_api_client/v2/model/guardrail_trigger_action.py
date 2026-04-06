# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuardrailTriggerAction(ModelSimple):
    """
    Action to perform when a guardrail threshold is triggered.

    :param value: Must be one of ["PAUSE", "ABORT"].
    :type value: str
    """

    allowed_values = {
        "PAUSE",
        "ABORT",
    }
    PAUSE: ClassVar["GuardrailTriggerAction"]
    ABORT: ClassVar["GuardrailTriggerAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuardrailTriggerAction.PAUSE = GuardrailTriggerAction("PAUSE")
GuardrailTriggerAction.ABORT = GuardrailTriggerAction("ABORT")
