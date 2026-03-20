# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpdateFeatureFlagDataType(ModelSimple):
    """
    The resource type.

    :param value: If omitted defaults to "feature-flags". Must be one of ["feature-flags"].
    :type value: str
    """

    allowed_values = {
        "feature-flags",
    }
    FEATURE_FLAGS: ClassVar["UpdateFeatureFlagDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpdateFeatureFlagDataType.FEATURE_FLAGS = UpdateFeatureFlagDataType("feature-flags")
