# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestVersionType(ModelSimple):
    """
    Type of the version resource.

    :param value: If omitted defaults to "version". Must be one of ["version"].
    :type value: str
    """

    allowed_values = {
        "version",
    }
    VERSION: ClassVar["SyntheticsTestVersionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestVersionType.VERSION = SyntheticsTestVersionType("version")
