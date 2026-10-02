# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsMetricV2DTODataAttributesMetricType(ModelSimple):
    """
    Type of metric calculation.

    :param value: Must be one of ["SIMPLE", "RATIO", "PERCENTILE", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "SIMPLE",
        "RATIO",
        "PERCENTILE",
        "UNKNOWN",
    }
    SIMPLE: ClassVar["ExperimentsMetricV2DTODataAttributesMetricType"]
    RATIO: ClassVar["ExperimentsMetricV2DTODataAttributesMetricType"]
    PERCENTILE: ClassVar["ExperimentsMetricV2DTODataAttributesMetricType"]
    UNKNOWN: ClassVar["ExperimentsMetricV2DTODataAttributesMetricType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsMetricV2DTODataAttributesMetricType.SIMPLE = ExperimentsMetricV2DTODataAttributesMetricType("SIMPLE")
ExperimentsMetricV2DTODataAttributesMetricType.RATIO = ExperimentsMetricV2DTODataAttributesMetricType("RATIO")
ExperimentsMetricV2DTODataAttributesMetricType.PERCENTILE = ExperimentsMetricV2DTODataAttributesMetricType("PERCENTILE")
ExperimentsMetricV2DTODataAttributesMetricType.UNKNOWN = ExperimentsMetricV2DTODataAttributesMetricType("UNKNOWN")
