# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["none", "inline", "automatic"].
    :type value: str
    """

    allowed_values = {
        "none",
        "inline",
        "automatic",
    }
    NONE: ClassVar["BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend"]
    INLINE: ClassVar["BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend"]
    AUTOMATIC: ClassVar["BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend.NONE = (
    BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend("none")
)
BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend.INLINE = (
    BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend("inline")
)
BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend.AUTOMATIC = (
    BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend("automatic")
)
