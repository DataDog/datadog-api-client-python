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
    from datadog_api_client.v2.model.synthetics_network_assertion_jitter_type import (
        SyntheticsNetworkAssertionJitterType,
    )


class SyntheticsNetworkAssertionJitter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_assertion_operator import SyntheticsNetworkAssertionOperator
        from datadog_api_client.v2.model.synthetics_network_assertion_jitter_type import (
            SyntheticsNetworkAssertionJitterType,
        )

        return {
            "operator": (SyntheticsNetworkAssertionOperator,),
            "target": (float,),
            "type": (SyntheticsNetworkAssertionJitterType,),
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
        type: SyntheticsNetworkAssertionJitterType,
        **kwargs,
    ):
        """
        Jitter assertion for a Network Path test.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsNetworkAssertionOperator

        :param target: Target value in milliseconds.
        :type target: float

        :param type: Type of the jitter assertion.
        :type type: SyntheticsNetworkAssertionJitterType
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.target = target
        self_.type = type
