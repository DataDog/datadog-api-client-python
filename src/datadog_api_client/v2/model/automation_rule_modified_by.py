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
    from datadog_api_client.v2.model.automation_rule_actor_type import AutomationRuleActorType


class AutomationRuleModifiedBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_actor_type import AutomationRuleActorType

        return {
            "id": (str,),
            "name": (str,),
            "type": (AutomationRuleActorType,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "type": "type",
    }

    def __init__(self_, id: str, name: str, type: AutomationRuleActorType, **kwargs):
        """
        The user or Datadog system who last modified the rule.

        :param id: The actor's identifier (a user UUID or a system identifier).
        :type id: str

        :param name: The name of the actor.
        :type name: str

        :param type: Whether the actor is a user or the Datadog system.
        :type type: AutomationRuleActorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.type = type
