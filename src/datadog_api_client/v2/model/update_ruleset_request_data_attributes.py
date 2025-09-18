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
    from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items import (
        UpdateRulesetRequestDataAttributesRulesItems,
    )


class UpdateRulesetRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items import (
            UpdateRulesetRequestDataAttributesRulesItems,
        )

        return {
            "enabled": (bool,),
            "last_version": (int,),
            "rules": ([UpdateRulesetRequestDataAttributesRulesItems],),
        }

    attribute_map = {
        "enabled": "enabled",
        "last_version": "last_version",
        "rules": "rules",
    }

    def __init__(
        self_,
        enabled: bool,
        rules: List[UpdateRulesetRequestDataAttributesRulesItems],
        last_version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateRulesetRequestDataAttributes`` object.

        :param enabled: The ``attributes`` ``enabled``.
        :type enabled: bool

        :param last_version: The ``attributes`` ``last_version``.
        :type last_version: int, optional

        :param rules: The ``attributes`` ``rules``.
        :type rules: [UpdateRulesetRequestDataAttributesRulesItems]
        """
        if last_version is not unset:
            kwargs["last_version"] = last_version
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.rules = rules
