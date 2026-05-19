# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseViewResourceType(ModelSimple):
    """
    JSON:API resource type for case views.

    :param value: If omitted defaults to "view". Must be one of ["view"].
    :type value: str
    """

    allowed_values = {
        "view",
    }
    VIEW: ClassVar["CaseViewResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseViewResourceType.VIEW = CaseViewResourceType("view")
