# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeomapPointsProjectionType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "geomap_points". Must be one of ["geomap_points"].
    :type value: str
    """

    allowed_values = {
        "geomap_points",
    }
    GEOMAP_POINTS: ClassVar["GeomapPointsProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeomapPointsProjectionType.GEOMAP_POINTS = GeomapPointsProjectionType("geomap_points")
