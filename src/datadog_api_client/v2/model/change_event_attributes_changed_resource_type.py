# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeEventAttributesChangedResourceType(ModelSimple):
    """
    The type of the changed resource.

    :param value: Must be one of ["feature_flag", "metric_configuration"].
    :type value: str
    """

    allowed_values = {
        "feature_flag",
        "metric_configuration",
    }
    FEATURE_FLAG: ClassVar["ChangeEventAttributesChangedResourceType"]
    METRIC_CONFIGURATION: ClassVar["ChangeEventAttributesChangedResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeEventAttributesChangedResourceType.FEATURE_FLAG = ChangeEventAttributesChangedResourceType("feature_flag")
ChangeEventAttributesChangedResourceType.METRIC_CONFIGURATION = ChangeEventAttributesChangedResourceType(
    "metric_configuration"
)
