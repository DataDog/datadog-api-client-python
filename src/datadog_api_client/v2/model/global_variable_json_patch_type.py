# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GlobalVariableJsonPatchType(ModelSimple):
    """
    Global variable JSON Patch type.

    :param value: If omitted defaults to "global_variables_json_patch". Must be one of ["global_variables_json_patch"].
    :type value: str
    """

    allowed_values = {
        "global_variables_json_patch",
    }
    GLOBAL_VARIABLES_JSON_PATCH: ClassVar["GlobalVariableJsonPatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GlobalVariableJsonPatchType.GLOBAL_VARIABLES_JSON_PATCH = GlobalVariableJsonPatchType("global_variables_json_patch")
