# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateStatusPageRequestDataAttributesVisualizationType(ModelSimple):
    """
    The visualization type of the status page.

    :param value: Must be one of ["bars_and_uptime_percentage", "bars_only", "component_name_only"].
    :type value: str
    """

    allowed_values = {
        "bars_and_uptime_percentage",
        "bars_only",
        "component_name_only",
    }
    BARS_AND_UPTIME_PERCENTAGE: ClassVar["CreateStatusPageRequestDataAttributesVisualizationType"]
    BARS_ONLY: ClassVar["CreateStatusPageRequestDataAttributesVisualizationType"]
    COMPONENT_NAME_ONLY: ClassVar["CreateStatusPageRequestDataAttributesVisualizationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateStatusPageRequestDataAttributesVisualizationType.BARS_AND_UPTIME_PERCENTAGE = (
    CreateStatusPageRequestDataAttributesVisualizationType("bars_and_uptime_percentage")
)
CreateStatusPageRequestDataAttributesVisualizationType.BARS_ONLY = (
    CreateStatusPageRequestDataAttributesVisualizationType("bars_only")
)
CreateStatusPageRequestDataAttributesVisualizationType.COMPONENT_NAME_ONLY = (
    CreateStatusPageRequestDataAttributesVisualizationType("component_name_only")
)
