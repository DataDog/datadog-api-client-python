# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.mute_rule_type import MuteRuleType


class MuteRuleReorderItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rule_type import MuteRuleType

        return {
            "id": (UUID,),
            "type": (MuteRuleType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: MuteRuleType, **kwargs):
        """
        A reference to a mute rule used for reordering.

        :param id: The ID of the automation rule.
        :type id: UUID

        :param type: The JSON:API type for mute rules.
        :type type: MuteRuleType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
