# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SuiteJsonPatchType(ModelSimple):
    """
    Type for a JSON Patch request on a Synthetic test suite, `suites_json_patch`.

    :param value: If omitted defaults to "suites_json_patch". Must be one of ["suites_json_patch"].
    :type value: str
    """

    allowed_values = {
        "suites_json_patch",
    }
    SUITES_JSON_PATCH: ClassVar["SuiteJsonPatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SuiteJsonPatchType.SUITES_JSON_PATCH = SuiteJsonPatchType("suites_json_patch")
