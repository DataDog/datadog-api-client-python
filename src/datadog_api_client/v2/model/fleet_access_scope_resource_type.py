# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAccessScopeResourceType(ModelSimple):
    """
    The JSON:API resource type for a fleet access scope.

    :param value: If omitted defaults to "access_scope". Must be one of ["access_scope"].
    :type value: str
    """

    allowed_values = {
        "access_scope",
    }
    ACCESS_SCOPE: ClassVar["FleetAccessScopeResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAccessScopeResourceType.ACCESS_SCOPE = FleetAccessScopeResourceType("access_scope")
