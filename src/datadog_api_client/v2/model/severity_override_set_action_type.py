# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityOverrideSetActionType(ModelSimple):
    """
    The action that applies a manual severity override.

    :param value: If omitted defaults to "set". Must be one of ["set"].
    :type value: str
    """

    allowed_values = {
        "set",
    }
    SET: ClassVar["SeverityOverrideSetActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityOverrideSetActionType.SET = SeverityOverrideSetActionType("set")
