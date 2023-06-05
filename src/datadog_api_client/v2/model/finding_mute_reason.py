# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FindingMuteReason(ModelSimple):
    """
    The reason why this finding is muted or unmuted.

    :param value: Must be one of ["PENDING_FIX", "FALSE_POSITIVE", "ACCEPTED_RISK", "NO_PENDING_FIX", "HUMAN_ERROR", "NO_LONGER_ACCEPTED_RISK", "OTHER"].
    :type value: str
    """

    allowed_values = {
        "PENDING_FIX",
        "FALSE_POSITIVE",
        "ACCEPTED_RISK",
        "NO_PENDING_FIX",
        "HUMAN_ERROR",
        "NO_LONGER_ACCEPTED_RISK",
        "OTHER",
    }
    PENDING_FIX: ClassVar["FindingMuteReason"]
    FALSE_POSITIVE: ClassVar["FindingMuteReason"]
    ACCEPTED_RISK: ClassVar["FindingMuteReason"]
    NO_PENDING_FIX: ClassVar["FindingMuteReason"]
    HUMAN_ERROR: ClassVar["FindingMuteReason"]
    NO_LONGER_ACCEPTED_RISK: ClassVar["FindingMuteReason"]
    OTHER: ClassVar["FindingMuteReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingMuteReason.PENDING_FIX = FindingMuteReason("PENDING_FIX")
FindingMuteReason.FALSE_POSITIVE = FindingMuteReason("FALSE_POSITIVE")
FindingMuteReason.ACCEPTED_RISK = FindingMuteReason("ACCEPTED_RISK")
FindingMuteReason.NO_PENDING_FIX = FindingMuteReason("NO_PENDING_FIX")
FindingMuteReason.HUMAN_ERROR = FindingMuteReason("HUMAN_ERROR")
FindingMuteReason.NO_LONGER_ACCEPTED_RISK = FindingMuteReason("NO_LONGER_ACCEPTED_RISK")
FindingMuteReason.OTHER = FindingMuteReason("OTHER")
