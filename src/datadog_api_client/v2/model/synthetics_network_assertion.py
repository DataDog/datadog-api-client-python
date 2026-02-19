# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SyntheticsNetworkAssertion(ModelComposed):
    def __init__(self, **kwargs):
        """
        Object describing an assertion for a Network Path test.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsNetworkAssertionOperator

        :param _property: The associated assertion property.
        :type _property: SyntheticsNetworkAssertionProperty

        :param target: Target value in milliseconds.
        :type target: float

        :param type: Type of the latency assertion.
        :type type: SyntheticsNetworkAssertionLatencyType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.synthetics_network_assertion_latency import SyntheticsNetworkAssertionLatency
        from datadog_api_client.v2.model.synthetics_network_assertion_multi_network_hop import (
            SyntheticsNetworkAssertionMultiNetworkHop,
        )
        from datadog_api_client.v2.model.synthetics_network_assertion_packet_loss_percentage import (
            SyntheticsNetworkAssertionPacketLossPercentage,
        )
        from datadog_api_client.v2.model.synthetics_network_assertion_jitter import SyntheticsNetworkAssertionJitter

        return {
            "oneOf": [
                SyntheticsNetworkAssertionLatency,
                SyntheticsNetworkAssertionMultiNetworkHop,
                SyntheticsNetworkAssertionPacketLossPercentage,
                SyntheticsNetworkAssertionJitter,
            ],
        }
