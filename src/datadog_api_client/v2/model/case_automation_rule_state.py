# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseAutomationRuleState(ModelSimple):
    """
    Whether the automation rule is active. Enabled rules trigger on matching case events; disabled rules are inactive but preserve their configuration.

    :param value: Must be one of ["ENABLED", "DISABLED"].
    :type value: str
    """

    allowed_values = {
        "ENABLED",
        "DISABLED",
    }
    ENABLED: ClassVar["CaseAutomationRuleState"]
    DISABLED: ClassVar["CaseAutomationRuleState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseAutomationRuleState.ENABLED = CaseAutomationRuleState("ENABLED")
CaseAutomationRuleState.DISABLED = CaseAutomationRuleState("DISABLED")
