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
    from datadog_api_client.v2.model.mute_rule_attributes import MuteRuleAttributes
    from datadog_api_client.v2.model.mute_rules_type import MuteRulesType


class MuteRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rule_attributes import MuteRuleAttributes
        from datadog_api_client.v2.model.mute_rules_type import MuteRulesType

        return {
            "attributes": (MuteRuleAttributes,),
            "id": (UUID,),
            "type": (MuteRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: MuteRuleAttributes, id: UUID, type: MuteRulesType, **kwargs):
        """
        Mute rules are used to proactively filter out known false positives or accepted risks.
        A mute rule is composed of a rule UUID, a rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the mute rule
        :type attributes: MuteRuleAttributes

        :param id: The ID of a pipeline rule
        :type id: UUID

        :param type: The pipeline rule type associated to mute rules
        :type type: MuteRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
