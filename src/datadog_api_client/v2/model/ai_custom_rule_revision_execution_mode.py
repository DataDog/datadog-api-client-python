# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiCustomRuleRevisionExecutionMode(ModelSimple):
    """
    The execution mode for an AI rule revision.

    :param value: Must be one of ["auto", "manual", "always"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "manual",
        "always",
    }
    AUTO: ClassVar["AiCustomRuleRevisionExecutionMode"]
    MANUAL: ClassVar["AiCustomRuleRevisionExecutionMode"]
    ALWAYS: ClassVar["AiCustomRuleRevisionExecutionMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiCustomRuleRevisionExecutionMode.AUTO = AiCustomRuleRevisionExecutionMode("auto")
AiCustomRuleRevisionExecutionMode.MANUAL = AiCustomRuleRevisionExecutionMode("manual")
AiCustomRuleRevisionExecutionMode.ALWAYS = AiCustomRuleRevisionExecutionMode("always")
