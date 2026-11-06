# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagChangeEventCreationSource(ModelSimple):
    """
    Where the change was made: `UI` for the Datadog app, or `MCP` for a Model Context Protocol (MCP) client.

    :param value: Must be one of ["UI", "MCP"].
    :type value: str
    """

    allowed_values = {
        "UI",
        "MCP",
    }
    UI: ClassVar["FeatureFlagChangeEventCreationSource"]
    MCP: ClassVar["FeatureFlagChangeEventCreationSource"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagChangeEventCreationSource.UI = FeatureFlagChangeEventCreationSource("UI")
FeatureFlagChangeEventCreationSource.MCP = FeatureFlagChangeEventCreationSource("MCP")
