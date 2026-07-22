# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PupBumpTestType(ModelSimple):
    """
    Pup bump test resource type.

    :param value: If omitted defaults to "pup_bump_test". Must be one of ["pup_bump_test"].
    :type value: str
    """

    allowed_values = {
        "pup_bump_test",
    }
    PUP_BUMP_TEST: ClassVar["PupBumpTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PupBumpTestType.PUP_BUMP_TEST = PupBumpTestType("pup_bump_test")
