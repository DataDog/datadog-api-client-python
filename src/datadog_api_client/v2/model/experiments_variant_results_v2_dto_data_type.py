# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsVariantResultsV2DTODataType(ModelSimple):
    """
    Experiment variant results resource type.

    :param value: If omitted defaults to "experiment-variant-results". Must be one of ["experiment-variant-results"].
    :type value: str
    """

    allowed_values = {
        "experiment-variant-results",
    }
    EXPERIMENT_VARIANT_RESULTS: ClassVar["ExperimentsVariantResultsV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsVariantResultsV2DTODataType.EXPERIMENT_VARIANT_RESULTS = ExperimentsVariantResultsV2DTODataType(
    "experiment-variant-results"
)
