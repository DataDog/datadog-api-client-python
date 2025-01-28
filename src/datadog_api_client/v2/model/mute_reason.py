# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MuteReason(ModelSimple):
    """
    Reason for muting a vulnerability

    :param value: Must be one of ["duplicate", "external_solution", "false_positive", "internal_solution", "no_fix_available", "other", "pending_fix", "risk_accepted"].
    :type value: str
    """

    allowed_values = {
        "duplicate",
        "external_solution",
        "false_positive",
        "internal_solution",
        "no_fix_available",
        "other",
        "pending_fix",
        "risk_accepted",
    }
    DUPLICATE: ClassVar["MuteReason"]
    EXTERNAL_SOLUTION: ClassVar["MuteReason"]
    FALSE_POSITIVE: ClassVar["MuteReason"]
    INTERNAL_SOLUTION: ClassVar["MuteReason"]
    NO_FIX_AVAILABLE: ClassVar["MuteReason"]
    OTHER: ClassVar["MuteReason"]
    PENDING_FIX: ClassVar["MuteReason"]
    RISK_ACCEPTED: ClassVar["MuteReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MuteReason.DUPLICATE = MuteReason("duplicate")
MuteReason.EXTERNAL_SOLUTION = MuteReason("external_solution")
MuteReason.FALSE_POSITIVE = MuteReason("false_positive")
MuteReason.INTERNAL_SOLUTION = MuteReason("internal_solution")
MuteReason.NO_FIX_AVAILABLE = MuteReason("no_fix_available")
MuteReason.OTHER = MuteReason("other")
MuteReason.PENDING_FIX = MuteReason("pending_fix")
MuteReason.RISK_ACCEPTED = MuteReason("risk_accepted")
