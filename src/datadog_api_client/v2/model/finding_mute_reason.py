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
    The reason why this finding is muted.

    :param value: Must be one of ["ACCEPTED_RISK", "PENDING_FIX", "FALSE_POSITIVE", "OTHER"].
    :type value: str
    """

    allowed_values = {
        "ACCEPTED_RISK",
        "PENDING_FIX",
        "FALSE_POSITIVE",
        "OTHER",
    }
    ACCEPTED_RISK: ClassVar["FindingMuteReason"]
    PENDING_FIX: ClassVar["FindingMuteReason"]
    FALSE_POSITIVE: ClassVar["FindingMuteReason"]
    OTHER: ClassVar["FindingMuteReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingMuteReason.ACCEPTED_RISK = FindingMuteReason("ACCEPTED_RISK")
FindingMuteReason.PENDING_FIX = FindingMuteReason("PENDING_FIX")
FindingMuteReason.FALSE_POSITIVE = FindingMuteReason("FALSE_POSITIVE")
FindingMuteReason.OTHER = FindingMuteReason("OTHER")
