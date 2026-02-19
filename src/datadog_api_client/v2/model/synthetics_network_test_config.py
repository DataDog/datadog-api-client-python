# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_network_assertion import SyntheticsNetworkAssertion
    from datadog_api_client.v2.model.synthetics_network_test_request import SyntheticsNetworkTestRequest
    from datadog_api_client.v2.model.synthetics_network_assertion_latency import SyntheticsNetworkAssertionLatency
    from datadog_api_client.v2.model.synthetics_network_assertion_multi_network_hop import (
        SyntheticsNetworkAssertionMultiNetworkHop,
    )
    from datadog_api_client.v2.model.synthetics_network_assertion_packet_loss_percentage import (
        SyntheticsNetworkAssertionPacketLossPercentage,
    )
    from datadog_api_client.v2.model.synthetics_network_assertion_jitter import SyntheticsNetworkAssertionJitter


class SyntheticsNetworkTestConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_assertion import SyntheticsNetworkAssertion
        from datadog_api_client.v2.model.synthetics_network_test_request import SyntheticsNetworkTestRequest

        return {
            "assertions": ([SyntheticsNetworkAssertion],),
            "request": (SyntheticsNetworkTestRequest,),
        }

    attribute_map = {
        "assertions": "assertions",
        "request": "request",
    }

    def __init__(
        self_,
        assertions: Union[
            List[
                Union[
                    SyntheticsNetworkAssertion,
                    SyntheticsNetworkAssertionLatency,
                    SyntheticsNetworkAssertionMultiNetworkHop,
                    SyntheticsNetworkAssertionPacketLossPercentage,
                    SyntheticsNetworkAssertionJitter,
                ]
            ],
            UnsetType,
        ] = unset,
        request: Union[SyntheticsNetworkTestRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration object for a Network Path test.

        :param assertions: Array of assertions used for the test.
        :type assertions: [SyntheticsNetworkAssertion], optional

        :param request: Object describing the request for a Network Path test.
        :type request: SyntheticsNetworkTestRequest, optional
        """
        if assertions is not unset:
            kwargs["assertions"] = assertions
        if request is not unset:
            kwargs["request"] = request
        super().__init__(kwargs)
