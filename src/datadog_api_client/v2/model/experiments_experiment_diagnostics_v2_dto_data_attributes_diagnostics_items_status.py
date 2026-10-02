# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus(ModelSimple):
    """
    Outcome of an individual diagnostic check.

    :param value: Must be one of ["PASS", "FAIL", "WARN", "ERROR", "SKIPPED"].
    :type value: str
    """

    allowed_values = {
        "PASS",
        "FAIL",
        "WARN",
        "ERROR",
        "SKIPPED",
    }
    PASS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus"]
    FAIL: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus"]
    WARN: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus"]
    ERROR: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus"]
    SKIPPED: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus.PASS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus("PASS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus.FAIL = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus("FAIL")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus.WARN = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus("WARN")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus.ERROR = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus("ERROR")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus.SKIPPED = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsStatus("SKIPPED")
)
