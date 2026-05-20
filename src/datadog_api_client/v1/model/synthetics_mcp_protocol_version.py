# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMCPProtocolVersion(ModelSimple):
    """
    The MCP protocol version used by the step. See https://modelcontextprotocol.io/specification.

    :param value: If omitted defaults to "2025-06-18". Must be one of ["2025-06-18"].
    :type value: str
    """

    allowed_values = {
        "2025-06-18",
    }
    VERSION_2025_06_18: ClassVar["SyntheticsMCPProtocolVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMCPProtocolVersion.VERSION_2025_06_18 = SyntheticsMCPProtocolVersion("2025-06-18")
