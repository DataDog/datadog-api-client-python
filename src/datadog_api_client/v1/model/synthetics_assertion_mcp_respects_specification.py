# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_mcp_respects_specification_type import (
        SyntheticsAssertionMCPRespectsSpecificationType,
    )


class SyntheticsAssertionMCPRespectsSpecification(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_mcp_respects_specification_type import (
            SyntheticsAssertionMCPRespectsSpecificationType,
        )

        return {
            "type": (SyntheticsAssertionMCPRespectsSpecificationType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: SyntheticsAssertionMCPRespectsSpecificationType, **kwargs):
        """
        An assertion that verifies the MCP server response respects the MCP specification.

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionMCPRespectsSpecificationType
        """
        super().__init__(kwargs)

        self_.type = type
