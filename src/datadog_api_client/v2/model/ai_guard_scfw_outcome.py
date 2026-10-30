# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIGuardScfwOutcome(ModelSimple):
    """
    The Supply Chain Firewall outcome for a package, a matched rule, or the whole request.

    :param value: Must be one of ["ALLOW", "WARN", "BLOCK"].
    :type value: str
    """

    allowed_values = {
        "ALLOW",
        "WARN",
        "BLOCK",
    }
    ALLOW: ClassVar["AIGuardScfwOutcome"]
    WARN: ClassVar["AIGuardScfwOutcome"]
    BLOCK: ClassVar["AIGuardScfwOutcome"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIGuardScfwOutcome.ALLOW = AIGuardScfwOutcome("ALLOW")
AIGuardScfwOutcome.WARN = AIGuardScfwOutcome("WARN")
AIGuardScfwOutcome.BLOCK = AIGuardScfwOutcome("BLOCK")
