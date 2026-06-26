# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceResourceLimitResourceType(ModelSimple):
    """
    Resource limit resource type.

    :param value: If omitted defaults to "resource-limit". Must be one of ["resource-limit"].
    :type value: str
    """

    allowed_values = {
        "resource-limit",
    }
    RESOURCE_LIMIT: ClassVar["GovernanceResourceLimitResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceResourceLimitResourceType.RESOURCE_LIMIT = GovernanceResourceLimitResourceType("resource-limit")
