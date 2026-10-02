# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsRefreshExperimentResultsV2DTODataType(ModelSimple):
    """
    Experiment results refresh resource type.

    :param value: If omitted defaults to "experiment-results-refresh". Must be one of ["experiment-results-refresh"].
    :type value: str
    """

    allowed_values = {
        "experiment-results-refresh",
    }
    EXPERIMENT_RESULTS_REFRESH: ClassVar["ExperimentsRefreshExperimentResultsV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsRefreshExperimentResultsV2DTODataType.EXPERIMENT_RESULTS_REFRESH = (
    ExperimentsRefreshExperimentResultsV2DTODataType("experiment-results-refresh")
)
