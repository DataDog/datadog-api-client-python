# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudcraftWidgetDefinitionProjection(ModelSimple):
    """
    Projection used to render the Cloudcraft topology.

    :param value: Must be one of ["isometric", "2d"].
    :type value: str
    """

    allowed_values = {
        "isometric",
        "2d",
    }
    ISOMETRIC: ClassVar["CloudcraftWidgetDefinitionProjection"]
    TWO_D: ClassVar["CloudcraftWidgetDefinitionProjection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudcraftWidgetDefinitionProjection.ISOMETRIC = CloudcraftWidgetDefinitionProjection("isometric")
CloudcraftWidgetDefinitionProjection.TWO_D = CloudcraftWidgetDefinitionProjection("2d")
