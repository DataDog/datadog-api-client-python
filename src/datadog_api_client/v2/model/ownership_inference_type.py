# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipInferenceType(ModelSimple):
    """
    The type of the ownership inference resource. The value should always be `ownership_inference`.

    :param value: If omitted defaults to "ownership_inference". Must be one of ["ownership_inference"].
    :type value: str
    """

    allowed_values = {
        "ownership_inference",
    }
    OWNERSHIP_INFERENCE: ClassVar["OwnershipInferenceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipInferenceType.OWNERSHIP_INFERENCE = OwnershipInferenceType("ownership_inference")
