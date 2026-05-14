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
    from datadog_api_client.v2.model.rule_based_view_attributes import RuleBasedViewAttributes
    from datadog_api_client.v2.model.rule_based_view_type import RuleBasedViewType


class RuleBasedViewData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_based_view_attributes import RuleBasedViewAttributes
        from datadog_api_client.v2.model.rule_based_view_type import RuleBasedViewType

        return {
            "attributes": (RuleBasedViewAttributes,),
            "id": (str,),
            "type": (RuleBasedViewType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RuleBasedViewAttributes, id: str, type: RuleBasedViewType, **kwargs):
        """
        Data envelope for the rule-based view response.

        :param attributes: Attributes of the rule-based view.
        :type attributes: RuleBasedViewAttributes

        :param id: Unique identifier of the rule-based view document.
        :type id: str

        :param type: The type of the resource. The value should always be ``rule_based_view``.
        :type type: RuleBasedViewType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
