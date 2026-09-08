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
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems,
    )


class GetMultipleRulesetsResponseDataAttributesRulesetsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems,
        )

        return {
            "description": (str,),
            "id": (str,),
            "name": (str,),
            "rules": ([GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems],),
            "short_description": (str,),
        }

    attribute_map = {
        "description": "description",
        "id": "id",
        "name": "name",
        "rules": "rules",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        description: str,
        id: str,
        name: str,
        rules: List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems],
        short_description: str,
        **kwargs,
    ):
        """
        A ruleset returned in the response, containing its metadata and associated rules.

        :param description: A detailed description of the ruleset's purpose and the types of issues it targets.
        :type description: str

        :param id: The unique identifier of the ruleset, which is the same as its name.
        :type id: str

        :param name: The unique name of the ruleset.
        :type name: str

        :param rules: The list of static analysis rules included in this ruleset.
        :type rules: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems]

        :param short_description: A brief summary of the ruleset, suitable for display in listings.
        :type short_description: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.id = id
        self_.name = name
        self_.rules = rules
        self_.short_description = short_description
