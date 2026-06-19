# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PatchDegradationUpdateRequestDataType(ModelSimple):
    """
    Degradation updates resource type.

    :param value: If omitted defaults to "degradation_updates". Must be one of ["degradation_updates"].
    :type value: str
    """

    allowed_values = {
        "degradation_updates",
    }
    DEGRADATION_UPDATES: ClassVar["PatchDegradationUpdateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PatchDegradationUpdateRequestDataType.DEGRADATION_UPDATES = PatchDegradationUpdateRequestDataType("degradation_updates")
