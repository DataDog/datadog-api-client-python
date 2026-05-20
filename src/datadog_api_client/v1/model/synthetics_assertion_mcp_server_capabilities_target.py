# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
    from datadog_api_client.v1.model.synthetics_mcp_server_capability import SyntheticsMCPServerCapability
    from datadog_api_client.v1.model.synthetics_assertion_mcp_server_capabilities_type import (
        SyntheticsAssertionMCPServerCapabilitiesType,
    )


class SyntheticsAssertionMCPServerCapabilitiesTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
        from datadog_api_client.v1.model.synthetics_mcp_server_capability import SyntheticsMCPServerCapability
        from datadog_api_client.v1.model.synthetics_assertion_mcp_server_capabilities_type import (
            SyntheticsAssertionMCPServerCapabilitiesType,
        )

        return {
            "operator": (SyntheticsAssertionOperator,),
            "target": ([SyntheticsMCPServerCapability],),
            "type": (SyntheticsAssertionMCPServerCapabilitiesType,),
        }

    attribute_map = {
        "operator": "operator",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsAssertionOperator,
        target: List[SyntheticsMCPServerCapability],
        type: SyntheticsAssertionMCPServerCapabilitiesType,
        **kwargs,
    ):
        """
        An assertion that checks that an MCP server advertises the expected capabilities.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionOperator

        :param target: List of MCP server capabilities to assert against.
        :type target: [SyntheticsMCPServerCapability]

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionMCPServerCapabilitiesType
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.target = target
        self_.type = type
