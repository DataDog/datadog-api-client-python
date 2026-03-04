# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsDatasetType(ModelSimple):
    """
    Resource type of an LLM Observability dataset.

    :param value: If omitted defaults to "datasets". Must be one of ["datasets"].
    :type value: str
    """

    allowed_values = {
        "datasets",
    }
    DATASETS: ClassVar["LLMObsDatasetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsDatasetType.DATASETS = LLMObsDatasetType("datasets")
