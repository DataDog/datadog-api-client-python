# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTablePresetColumnPresetType(ModelSimple):
    """


    :param value: If omitted defaults to "previous_period". Must be one of ["previous_period"].
    :type value: str
    """

    allowed_values = {
        "previous_period",
    }
    PREVIOUS_PERIOD: ClassVar["GuidedTablePresetColumnPresetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTablePresetColumnPresetType.PREVIOUS_PERIOD = GuidedTablePresetColumnPresetType("previous_period")
