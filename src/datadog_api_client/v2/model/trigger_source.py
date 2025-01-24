# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TriggerSource(ModelSimple):
    """
    The type of security issues on which the rule applies. Notification rules based on security signals need to use the trigger source "security_signals",
        while notification rules based on security vulnerabilities need to use the trigger source "security_findings".

    :param value: Must be one of ["security_findings", "security_signals"].
    :type value: str
    """

    allowed_values = {
        "security_findings",
        "security_signals",
    }
    SECURITY_FINDINGS: ClassVar["TriggerSource"]
    SECURITY_SIGNALS: ClassVar["TriggerSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TriggerSource.SECURITY_FINDINGS = TriggerSource("security_findings")
TriggerSource.SECURITY_SIGNALS = TriggerSource("security_signals")
