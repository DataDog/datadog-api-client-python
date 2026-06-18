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
    from datadog_api_client.v2.model.mute_rule_reorder_item import MuteRuleReorderItem


class MuteRuleReorderRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rule_reorder_item import MuteRuleReorderItem

        return {
            "data": ([MuteRuleReorderItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[MuteRuleReorderItem], **kwargs):
        """
        The body of the mute rule reorder request.

        :param data: The ordered list of all mute rules; every rule must be included.
        :type data: [MuteRuleReorderItem]
        """
        super().__init__(kwargs)

        self_.data = data
