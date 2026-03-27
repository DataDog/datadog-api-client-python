# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestParentSuiteType(ModelSimple):
    """
    Type of the parent suite resource.

    :param value: If omitted defaults to "parent_suite". Must be one of ["parent_suite"].
    :type value: str
    """

    allowed_values = {
        "parent_suite",
    }
    PARENT_SUITE: ClassVar["SyntheticsTestParentSuiteType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestParentSuiteType.PARENT_SUITE = SyntheticsTestParentSuiteType("parent_suite")
