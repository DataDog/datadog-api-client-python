# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsDatasetVersionType(ModelSimple):
    """
    Resource type of an LLM Observability dataset version.

    :param value: If omitted defaults to "dataset_version". Must be one of ["dataset_version"].
    :type value: str
    """

    allowed_values = {
        "dataset_version",
    }
    DATASET_VERSION: ClassVar["LLMObsDatasetVersionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsDatasetVersionType.DATASET_VERSION = LLMObsDatasetVersionType("dataset_version")
