# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DueDateFrom(ModelSimple):
    """
    The reference point from which the due date is calculated. When `fix_available` is selected but not applicable to the finding type, `first_seen` is used instead.

    :param value: Must be one of ["first_seen", "fix_available"].
    :type value: str
    """

    allowed_values = {
        "first_seen",
        "fix_available",
    }
    FIRST_SEEN: ClassVar["DueDateFrom"]
    FIX_AVAILABLE: ClassVar["DueDateFrom"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DueDateFrom.FIRST_SEEN = DueDateFrom("first_seen")
DueDateFrom.FIX_AVAILABLE = DueDateFrom("fix_available")
