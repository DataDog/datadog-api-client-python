# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmAgentlessHostFacetType(ModelSimple):
    """
    The JSON:API type for agentless host facet resources. The value should always be `agentless_host_facet`.

    :param value: If omitted defaults to "agentless_host_facet". Must be one of ["agentless_host_facet"].
    :type value: str
    """

    allowed_values = {
        "agentless_host_facet",
    }
    AGENTLESS_HOST_FACET: ClassVar["CsmAgentlessHostFacetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmAgentlessHostFacetType.AGENTLESS_HOST_FACET = CsmAgentlessHostFacetType("agentless_host_facet")
