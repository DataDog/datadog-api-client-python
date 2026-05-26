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
    from datadog_api_client.v2.model.sast_ruleset_data_attributes import SastRulesetDataAttributes
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data_type import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
    )


class SastRulesetData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sast_ruleset_data_attributes import SastRulesetDataAttributes
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data_type import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
        )

        return {
            "attributes": (SastRulesetDataAttributes,),
            "id": (str,),
            "type": (GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SastRulesetDataAttributes,
        id: str,
        type: GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
        **kwargs,
    ):
        """
        The primary data object representing a SAST ruleset.

        :param attributes: The attributes of a SAST ruleset, including its name, description, and rules.
        :type attributes: SastRulesetDataAttributes

        :param id: The unique identifier of the ruleset resource.
        :type id: str

        :param type: Rulesets resource type.
        :type type: GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
