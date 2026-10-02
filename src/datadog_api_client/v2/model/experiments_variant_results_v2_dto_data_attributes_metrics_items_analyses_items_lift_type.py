# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType(ModelSimple):
    """
    Whether the reported lift is relative or absolute.

    :param value: Must be one of ["RELATIVE", "ABSOLUTE", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "RELATIVE",
        "ABSOLUTE",
        "UNKNOWN",
    }
    RELATIVE: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType"]
    ABSOLUTE: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType"]
    UNKNOWN: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType.RELATIVE = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType("RELATIVE")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType.ABSOLUTE = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType("ABSOLUTE")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType.UNKNOWN = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType("UNKNOWN")
)
