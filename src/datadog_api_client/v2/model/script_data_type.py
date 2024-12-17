# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScriptDataType(ModelSimple):
    """
    The definition of `ScriptDataType` object.

    :param value: If omitted defaults to "scripts". Must be one of ["scripts"].
    :type value: str
    """

    allowed_values = {
        "scripts",
    }
    SCRIPTS: ClassVar["ScriptDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScriptDataType.SCRIPTS = ScriptDataType("scripts")
