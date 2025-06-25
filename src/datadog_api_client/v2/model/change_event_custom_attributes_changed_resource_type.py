# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeEventCustomAttributesChangedResourceType(ModelSimple):
    """
    The type of the resource that was changed.

    :param value: Must be one of ["feature_flag", "configuration"].
    :type value: str
    """

    allowed_values = {
        "feature_flag",
        "configuration",
    }
    FEATURE_FLAG: ClassVar["ChangeEventCustomAttributesChangedResourceType"]
    CONFIGURATION: ClassVar["ChangeEventCustomAttributesChangedResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeEventCustomAttributesChangedResourceType.FEATURE_FLAG = ChangeEventCustomAttributesChangedResourceType(
    "feature_flag"
)
ChangeEventCustomAttributesChangedResourceType.CONFIGURATION = ChangeEventCustomAttributesChangedResourceType(
    "configuration"
)
