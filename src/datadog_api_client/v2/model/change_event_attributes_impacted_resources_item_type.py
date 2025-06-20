# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeEventAttributesImpactedResourcesItemType(ModelSimple):
    """
    The type of the impacted resource.

    :param value: If omitted defaults to "service". Must be one of ["service"].
    :type value: str
    """

    allowed_values = {
        "service",
    }
    SERVICE: ClassVar["ChangeEventAttributesImpactedResourcesItemType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeEventAttributesImpactedResourcesItemType.SERVICE = ChangeEventAttributesImpactedResourcesItemType("service")
