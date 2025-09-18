# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes import ArbitraryRuleResponseDataAttributes
    from datadog_api_client.v2.model.arbitrary_rule_response_data_type import ArbitraryRuleResponseDataType


class ArbitraryRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes import (
            ArbitraryRuleResponseDataAttributes,
        )
        from datadog_api_client.v2.model.arbitrary_rule_response_data_type import ArbitraryRuleResponseDataType

        return {
            "attributes": (ArbitraryRuleResponseDataAttributes,),
            "id": (str,),
            "type": (ArbitraryRuleResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ArbitraryRuleResponseDataType,
        attributes: Union[ArbitraryRuleResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleResponseData`` object.

        :param attributes: The definition of ``ArbitraryRuleResponseDataAttributes`` object.
        :type attributes: ArbitraryRuleResponseDataAttributes, optional

        :param id: The ``ArbitraryRuleResponseData`` ``id``.
        :type id: str, optional

        :param type: Arbitrary rule resource type.
        :type type: ArbitraryRuleResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
