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
    from datadog_api_client.v2.model.synthetics_network_assertion_property import SyntheticsNetworkAssertionProperty
    from datadog_api_client.v2.model.synthetics_network_assertion_multi_network_hop_type import (
        SyntheticsNetworkAssertionMultiNetworkHopType,
    )


class SyntheticsNetworkAssertionMultiNetworkHop(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_network_assertion_operator import SyntheticsNetworkAssertionOperator
        from datadog_api_client.v2.model.synthetics_network_assertion_property import SyntheticsNetworkAssertionProperty
        from datadog_api_client.v2.model.synthetics_network_assertion_multi_network_hop_type import (
            SyntheticsNetworkAssertionMultiNetworkHopType,
        )

        return {
            "operator": (SyntheticsNetworkAssertionOperator,),
            "_property": (SyntheticsNetworkAssertionProperty,),
            "target": (float,),
            "type": (SyntheticsNetworkAssertionMultiNetworkHopType,),
        }

    attribute_map = {
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsNetworkAssertionOperator,
        _property: SyntheticsNetworkAssertionProperty,
        target: float,
        type: SyntheticsNetworkAssertionMultiNetworkHopType,
        **kwargs,
    ):
        """
        Multi-network hop assertion for a Network Path test.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsNetworkAssertionOperator

        :param _property: The associated assertion property.
        :type _property: SyntheticsNetworkAssertionProperty

        :param target: Target value in number of hops.
        :type target: float

        :param type: Type of the multi-network hop assertion.
        :type type: SyntheticsNetworkAssertionMultiNetworkHopType
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_._property = _property
        self_.target = target
        self_.type = type
