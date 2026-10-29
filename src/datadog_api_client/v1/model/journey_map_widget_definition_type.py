# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JourneyMapWidgetDefinitionType(ModelSimple):
    """
    Type of the Journey Paths widget.

    :param value: If omitted defaults to "journey_map". Must be one of ["journey_map"].
    :type value: str
    """

    allowed_values = {
        "journey_map",
    }
    JOURNEY_MAP: ClassVar["JourneyMapWidgetDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JourneyMapWidgetDefinitionType.JOURNEY_MAP = JourneyMapWidgetDefinitionType("journey_map")
