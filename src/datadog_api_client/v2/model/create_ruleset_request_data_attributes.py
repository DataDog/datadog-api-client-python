# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items import (
        CreateRulesetRequestDataAttributesRulesItems,
    )


class CreateRulesetRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items import (
            CreateRulesetRequestDataAttributesRulesItems,
        )

        return {
            "enabled": (bool,),
            "rules": ([CreateRulesetRequestDataAttributesRulesItems],),
        }

    attribute_map = {
        "enabled": "enabled",
        "rules": "rules",
    }

    def __init__(
        self_,
        rules: List[CreateRulesetRequestDataAttributesRulesItems],
        enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateRulesetRequestDataAttributes`` object.

        :param enabled: The ``attributes`` ``enabled``.
        :type enabled: bool, optional

        :param rules: The ``attributes`` ``rules``.
        :type rules: [CreateRulesetRequestDataAttributesRulesItems]
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)

        self_.rules = rules
