# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataType(ModelSimple):
    """
    Experiment diagnostics resource type.

    :param value: If omitted defaults to "experiment-diagnostics". Must be one of ["experiment-diagnostics"].
    :type value: str
    """

    allowed_values = {
        "experiment-diagnostics",
    }
    EXPERIMENT_DIAGNOSTICS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataType.EXPERIMENT_DIAGNOSTICS = ExperimentsExperimentDiagnosticsV2DTODataType(
    "experiment-diagnostics"
)
