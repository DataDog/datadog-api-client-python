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
    from datadog_api_client.v2.model.ai_custom_rule_item import AiCustomRuleItem
    from datadog_api_client.v2.model.ai_custom_rule_data_type import AiCustomRuleDataType


class AiCustomRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_rule_item import AiCustomRuleItem
        from datadog_api_client.v2.model.ai_custom_rule_data_type import AiCustomRuleDataType

        return {
            "attributes": (AiCustomRuleItem,),
            "id": (str,),
            "type": (AiCustomRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiCustomRuleItem, id: str, type: AiCustomRuleDataType, **kwargs):
        """
        Response data for an AI custom rule.

        :param attributes: An AI custom rule embedded within a ruleset response.
        :type attributes: AiCustomRuleItem

        :param id: The rule identifier.
        :type id: str

        :param type: AI custom rule resource type.
        :type type: AiCustomRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
