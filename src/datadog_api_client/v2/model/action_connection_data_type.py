# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ActionConnectionDataType(ModelSimple):
    """
    The definition of `ActionConnectionDataType` object.

    :param value: If omitted defaults to "action_connection". Must be one of ["action_connection"].
    :type value: str
    """

    allowed_values = {
        "action_connection",
    }
    ACTION_CONNECTION: ClassVar["ActionConnectionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ActionConnectionDataType.ACTION_CONNECTION = ActionConnectionDataType("action_connection")
