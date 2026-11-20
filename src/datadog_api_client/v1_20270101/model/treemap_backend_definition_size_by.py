# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TreemapBackendDefinitionSizeBy(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["pct_cpu", "pct_mem"].
    :type value: str
    """

    allowed_values = {
        "pct_cpu",
        "pct_mem",
    }
    PCT_CPU: ClassVar["TreemapBackendDefinitionSizeBy"]
    PCT_MEM: ClassVar["TreemapBackendDefinitionSizeBy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TreemapBackendDefinitionSizeBy.PCT_CPU = TreemapBackendDefinitionSizeBy("pct_cpu")
TreemapBackendDefinitionSizeBy.PCT_MEM = TreemapBackendDefinitionSizeBy("pct_mem")
