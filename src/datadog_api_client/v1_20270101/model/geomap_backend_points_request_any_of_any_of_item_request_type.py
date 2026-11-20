# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeomapBackendPointsRequestAnyOfAnyOfItemRequestType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "network_devices_geomap". Must be one of ["network_devices_geomap"].
    :type value: str
    """

    allowed_values = {
        "network_devices_geomap",
    }
    NETWORK_DEVICES_GEOMAP: ClassVar["GeomapBackendPointsRequestAnyOfAnyOfItemRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeomapBackendPointsRequestAnyOfAnyOfItemRequestType.NETWORK_DEVICES_GEOMAP = (
    GeomapBackendPointsRequestAnyOfAnyOfItemRequestType("network_devices_geomap")
)
