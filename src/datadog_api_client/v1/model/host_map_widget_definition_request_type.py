# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostMapWidgetDefinitionRequestType(ModelSimple):
    """
    Identifies which host map request format the sibling fields on `HostMapWidgetDefinitionRequests` describe: an infrastructure-backed request or a DDSQL published-dataset request.

    :param value: Must be one of ["infrastructure_hostmap", "data_projection"].
    :type value: str
    """

    allowed_values = {
        "infrastructure_hostmap",
        "data_projection",
    }
    INFRASTRUCTURE_HOSTMAP: ClassVar["HostMapWidgetDefinitionRequestType"]
    DATA_PROJECTION: ClassVar["HostMapWidgetDefinitionRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostMapWidgetDefinitionRequestType.INFRASTRUCTURE_HOSTMAP = HostMapWidgetDefinitionRequestType("infrastructure_hostmap")
HostMapWidgetDefinitionRequestType.DATA_PROJECTION = HostMapWidgetDefinitionRequestType("data_projection")
