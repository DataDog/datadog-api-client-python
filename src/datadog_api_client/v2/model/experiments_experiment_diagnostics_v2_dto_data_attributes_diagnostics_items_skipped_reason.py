# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason(ModelSimple):
    """
    Reason the diagnostic check could not be evaluated.

    :param value: Must be one of ["NO_ASSIGNMENTS", "NO_DIMENSIONAL_DATA", "NO_METRIC_DATA", "ZERO_VARIANCE"].
    :type value: str
    """

    allowed_values = {
        "NO_ASSIGNMENTS",
        "NO_DIMENSIONAL_DATA",
        "NO_METRIC_DATA",
        "ZERO_VARIANCE",
    }
    NO_ASSIGNMENTS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason"]
    NO_DIMENSIONAL_DATA: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason"]
    NO_METRIC_DATA: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason"]
    ZERO_VARIANCE: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason.NO_ASSIGNMENTS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason("NO_ASSIGNMENTS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason.NO_DIMENSIONAL_DATA = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason("NO_DIMENSIONAL_DATA")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason.NO_METRIC_DATA = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason("NO_METRIC_DATA")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason.ZERO_VARIANCE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsSkippedReason("ZERO_VARIANCE")
)
