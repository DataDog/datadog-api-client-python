# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostmapInfrastructureRequestRequestType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "infrastructure_hostmap". Must be one of ["infrastructure_hostmap"].
    :type value: str
    """

    allowed_values = {
        "infrastructure_hostmap",
    }
    INFRASTRUCTURE_HOSTMAP: ClassVar["HostmapInfrastructureRequestRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostmapInfrastructureRequestRequestType.INFRASTRUCTURE_HOSTMAP = HostmapInfrastructureRequestRequestType(
    "infrastructure_hostmap"
)
