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
    from datadog_api_client.v2.model.arbitrary_rule_status_response_data_attributes import (
        ArbitraryRuleStatusResponseDataAttributes,
    )
    from datadog_api_client.v2.model.arbitrary_rule_status_response_data_type import ArbitraryRuleStatusResponseDataType


class ArbitraryRuleStatusResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_status_response_data_attributes import (
            ArbitraryRuleStatusResponseDataAttributes,
        )
        from datadog_api_client.v2.model.arbitrary_rule_status_response_data_type import (
            ArbitraryRuleStatusResponseDataType,
        )

        return {
            "attributes": (ArbitraryRuleStatusResponseDataAttributes,),
            "id": (str,),
            "type": (ArbitraryRuleStatusResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ArbitraryRuleStatusResponseDataAttributes,
        id: str,
        type: ArbitraryRuleStatusResponseDataType,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleStatusResponseData`` object.

        :param attributes: The definition of ``ArbitraryRuleStatusResponseDataAttributes`` object.
        :type attributes: ArbitraryRuleStatusResponseDataAttributes

        :param id: The unique identifier of the custom allocation rule.
        :type id: str

        :param type: Arbitrary rule status resource type.
        :type type: ArbitraryRuleStatusResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
