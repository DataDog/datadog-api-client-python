# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AbbreviatedTeamType(ModelSimple):
    """
    The definition of `AbbreviatedTeamType` object.

    :param value: If omitted defaults to "team". Must be one of ["team"].
    :type value: str
    """

    allowed_values = {
        "team",
    }
    TEAM: ClassVar["AbbreviatedTeamType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AbbreviatedTeamType.TEAM = AbbreviatedTeamType("team")
