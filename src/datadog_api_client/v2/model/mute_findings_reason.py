# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MuteFindingsReason(ModelSimple):
    """
    The reason why the findings are muted or unmuted.

    :param value: Must be one of ["PENDING_FIX", "FALSE_POSITIVE", "OTHER", "NO_FIX", "DUPLICATE", "RISK_ACCEPTED", "NO_PENDING_FIX", "HUMAN_ERROR", "NO_LONGER_ACCEPTED_RISK"].
    :type value: str
    """

    allowed_values = {
        "PENDING_FIX",
        "FALSE_POSITIVE",
        "OTHER",
        "NO_FIX",
        "DUPLICATE",
        "RISK_ACCEPTED",
        "NO_PENDING_FIX",
        "HUMAN_ERROR",
        "NO_LONGER_ACCEPTED_RISK",
    }
    PENDING_FIX: ClassVar["MuteFindingsReason"]
    FALSE_POSITIVE: ClassVar["MuteFindingsReason"]
    OTHER: ClassVar["MuteFindingsReason"]
    NO_FIX: ClassVar["MuteFindingsReason"]
    DUPLICATE: ClassVar["MuteFindingsReason"]
    RISK_ACCEPTED: ClassVar["MuteFindingsReason"]
    NO_PENDING_FIX: ClassVar["MuteFindingsReason"]
    HUMAN_ERROR: ClassVar["MuteFindingsReason"]
    NO_LONGER_ACCEPTED_RISK: ClassVar["MuteFindingsReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MuteFindingsReason.PENDING_FIX = MuteFindingsReason("PENDING_FIX")
MuteFindingsReason.FALSE_POSITIVE = MuteFindingsReason("FALSE_POSITIVE")
MuteFindingsReason.OTHER = MuteFindingsReason("OTHER")
MuteFindingsReason.NO_FIX = MuteFindingsReason("NO_FIX")
MuteFindingsReason.DUPLICATE = MuteFindingsReason("DUPLICATE")
MuteFindingsReason.RISK_ACCEPTED = MuteFindingsReason("RISK_ACCEPTED")
MuteFindingsReason.NO_PENDING_FIX = MuteFindingsReason("NO_PENDING_FIX")
MuteFindingsReason.HUMAN_ERROR = MuteFindingsReason("HUMAN_ERROR")
MuteFindingsReason.NO_LONGER_ACCEPTED_RISK = MuteFindingsReason("NO_LONGER_ACCEPTED_RISK")
