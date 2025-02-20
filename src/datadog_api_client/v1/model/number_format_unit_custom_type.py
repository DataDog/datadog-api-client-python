# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NumberFormatUnitCustomType(ModelSimple):
    """
    The type of custom unit.

    :param value: If omitted defaults to "custom_unit_label". Must be one of ["custom_unit_label"].
    :type value: str
    """

    allowed_values = {
        "custom_unit_label",
    }
    CUSTOM_UNIT_LABEL: ClassVar["NumberFormatUnitCustomType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NumberFormatUnitCustomType.CUSTOM_UNIT_LABEL = NumberFormatUnitCustomType("custom_unit_label")
