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
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_created import RulesetRespDataAttributesCreated
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_modified import RulesetRespDataAttributesModified
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items import RulesetRespDataAttributesRulesItems


class RulesetRespDataAttributes(ModelNormal):
    validations = {
        "position": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_created import RulesetRespDataAttributesCreated
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_modified import RulesetRespDataAttributesModified
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items import (
            RulesetRespDataAttributesRulesItems,
        )

        return {
            "created": (RulesetRespDataAttributesCreated,),
            "enabled": (bool,),
            "last_modified_user_uuid": (str,),
            "modified": (RulesetRespDataAttributesModified,),
            "name": (str,),
            "position": (int,),
            "rules": ([RulesetRespDataAttributesRulesItems],),
            "version": (int,),
        }

    attribute_map = {
        "created": "created",
        "enabled": "enabled",
        "last_modified_user_uuid": "last_modified_user_uuid",
        "modified": "modified",
        "name": "name",
        "position": "position",
        "rules": "rules",
        "version": "version",
    }

    def __init__(
        self_,
        created: RulesetRespDataAttributesCreated,
        enabled: bool,
        last_modified_user_uuid: str,
        modified: RulesetRespDataAttributesModified,
        name: str,
        position: int,
        rules: List[RulesetRespDataAttributesRulesItems],
        version: int,
        **kwargs,
    ):
        """
        The definition of ``RulesetRespDataAttributes`` object.

        :param created: The definition of ``RulesetRespDataAttributesCreated`` object.
        :type created: RulesetRespDataAttributesCreated

        :param enabled: The ``attributes`` ``enabled``.
        :type enabled: bool

        :param last_modified_user_uuid: The ``attributes`` ``last_modified_user_uuid``.
        :type last_modified_user_uuid: str

        :param modified: The definition of ``RulesetRespDataAttributesModified`` object.
        :type modified: RulesetRespDataAttributesModified

        :param name: The ``attributes`` ``name``.
        :type name: str

        :param position: The ``attributes`` ``position``.
        :type position: int

        :param rules: The ``attributes`` ``rules``.
        :type rules: [RulesetRespDataAttributesRulesItems]

        :param version: The ``attributes`` ``version``.
        :type version: int
        """
        super().__init__(kwargs)

        self_.created = created
        self_.enabled = enabled
        self_.last_modified_user_uuid = last_modified_user_uuid
        self_.modified = modified
        self_.name = name
        self_.position = position
        self_.rules = rules
        self_.version = version
