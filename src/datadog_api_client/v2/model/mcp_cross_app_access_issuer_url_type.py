# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class McpCrossAppAccessIssuerUrlType(ModelSimple):
    """
    Data type of an MCP Cross-App Access issuer URL update.

    :param value: If omitted defaults to "org_config". Must be one of ["org_config"].
    :type value: str
    """

    allowed_values = {
        "org_config",
    }
    ORG_CONFIG: ClassVar["McpCrossAppAccessIssuerUrlType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


McpCrossAppAccessIssuerUrlType.ORG_CONFIG = McpCrossAppAccessIssuerUrlType("org_config")
