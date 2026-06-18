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
    The reason for muting a security finding.

    :param value: Must be one of ["duplicate", "false_positive", "no_fix", "other", "pending_fix", "risk_accepted"].
    :type value: str
    """

    allowed_values = {
        "duplicate",
        "false_positive",
        "no_fix",
        "other",
        "pending_fix",
        "risk_accepted",
    }
    DUPLICATE: ClassVar["MuteReason"]
    FALSE_POSITIVE: ClassVar["MuteReason"]
    NO_FIX: ClassVar["MuteReason"]
    OTHER: ClassVar["MuteReason"]
    PENDING_FIX: ClassVar["MuteReason"]
    RISK_ACCEPTED: ClassVar["MuteReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MuteReason.DUPLICATE = MuteReason("duplicate")
MuteReason.FALSE_POSITIVE = MuteReason("false_positive")
MuteReason.NO_FIX = MuteReason("no_fix")
MuteReason.OTHER = MuteReason("other")
MuteReason.PENDING_FIX = MuteReason("pending_fix")
MuteReason.RISK_ACCEPTED = MuteReason("risk_accepted")
