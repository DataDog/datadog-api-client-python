# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NumberFormatUnitScaleType(ModelSimple):
    """
    The type of unit scale.

    :param value: If omitted defaults to "canonical_unit". Must be one of ["canonical_unit"].
    :type value: str
    """

    allowed_values = {
        "canonical_unit",
    }
    CANONICAL_UNIT: ClassVar["NumberFormatUnitScaleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NumberFormatUnitScaleType.CANONICAL_UNIT = NumberFormatUnitScaleType("canonical_unit")
