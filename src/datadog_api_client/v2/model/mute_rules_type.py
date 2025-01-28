# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MuteRulesType(ModelSimple):
    """
    The pipeline rule type associated to mute rules

    :param value: If omitted defaults to "mute_rules". Must be one of ["mute_rules"].
    :type value: str
    """

    allowed_values = {
        "mute_rules",
    }
    MUTE_RULES: ClassVar["MuteRulesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MuteRulesType.MUTE_RULES = MuteRulesType("mute_rules")
