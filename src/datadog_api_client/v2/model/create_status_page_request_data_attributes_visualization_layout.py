# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateStatusPageRequestDataAttributesVisualizationLayout(ModelSimple):
    """
    The layout of components on the status page. Defaults to `list`. `grid` requires `visualization_type` to be `component_name_only`; changing `visualization_type` to any other value resets the layout to `list`.

    :param value: Must be one of ["list", "grid"].
    :type value: str
    """

    allowed_values = {
        "list",
        "grid",
    }
    LIST: ClassVar["CreateStatusPageRequestDataAttributesVisualizationLayout"]
    GRID: ClassVar["CreateStatusPageRequestDataAttributesVisualizationLayout"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateStatusPageRequestDataAttributesVisualizationLayout.LIST = (
    CreateStatusPageRequestDataAttributesVisualizationLayout("list")
)
CreateStatusPageRequestDataAttributesVisualizationLayout.GRID = (
    CreateStatusPageRequestDataAttributesVisualizationLayout("grid")
)
