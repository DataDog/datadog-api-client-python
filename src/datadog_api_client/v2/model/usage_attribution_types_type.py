# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UsageAttributionTypesType(ModelSimple):
    """
    Type of usage attribution types data.

    :param value: If omitted defaults to "usage_attribution_types". Must be one of ["usage_attribution_types"].
    :type value: str
    """

    allowed_values = {
        "usage_attribution_types",
    }
    USAGE_ATTRIBUTION_TYPES: ClassVar["UsageAttributionTypesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UsageAttributionTypesType.USAGE_ATTRIBUTION_TYPES = UsageAttributionTypesType("usage_attribution_types")
