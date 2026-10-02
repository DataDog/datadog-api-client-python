# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataAttributesResult(ModelSimple):
    """
    Overall result of the experiment diagnostic checks.

    :param value: Must be one of ["PASS", "FAIL", "WARN", "NO_DATA"].
    :type value: str
    """

    allowed_values = {
        "PASS",
        "FAIL",
        "WARN",
        "NO_DATA",
    }
    PASS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesResult"]
    FAIL: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesResult"]
    WARN: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesResult"]
    NO_DATA: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesResult"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataAttributesResult.PASS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesResult("PASS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesResult.FAIL = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesResult("FAIL")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesResult.WARN = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesResult("WARN")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesResult.NO_DATA = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesResult("NO_DATA")
)
