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
    from datadog_api_client.v2.model.severity_modifier_rule_reorder_item import SeverityModifierRuleReorderItem


class SeverityModifierRuleReorderRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_rule_reorder_item import SeverityModifierRuleReorderItem

        return {
            "data": ([SeverityModifierRuleReorderItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SeverityModifierRuleReorderItem], **kwargs):
        """
        The body of a severity modifier rule reorder request.

        :param data: The ordered list of severity modifier rules; every rule must be included.
        :type data: [SeverityModifierRuleReorderItem]
        """
        super().__init__(kwargs)

        self_.data = data
