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
    from datadog_api_client.v2.model.synthetics_network_assertion_operator import SyntheticsNetworkAssertionOperator
    from datadog_api_client.v2.model.synthetics_network_assertion_packet_loss_percentage_type import (
        SyntheticsNetworkAssertionPacketLossPercentageType,
    )


class SyntheticsNetworkAssertionPacketLossPercentage(ModelNormal):
    validations = {
        "target": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_assertion_operator import SyntheticsNetworkAssertionOperator
        from datadog_api_client.v2.model.synthetics_network_assertion_packet_loss_percentage_type import (
            SyntheticsNetworkAssertionPacketLossPercentageType,
        )

        return {
            "operator": (SyntheticsNetworkAssertionOperator,),
            "target": (float,),
            "type": (SyntheticsNetworkAssertionPacketLossPercentageType,),
        }

    attribute_map = {
        "operator": "operator",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsNetworkAssertionOperator,
        target: float,
        type: SyntheticsNetworkAssertionPacketLossPercentageType,
        **kwargs,
    ):
        """
        Packet loss percentage assertion for a Network Path test.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsNetworkAssertionOperator

        :param target: Target value as a percentage (0 to 1).
        :type target: float

        :param type: Type of the packet loss percentage assertion.
        :type type: SyntheticsNetworkAssertionPacketLossPercentageType
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.target = target
        self_.type = type
