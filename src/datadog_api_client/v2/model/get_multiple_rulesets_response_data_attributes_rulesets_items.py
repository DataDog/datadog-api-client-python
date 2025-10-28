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
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsData,
    )
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems,
    )


class GetMultipleRulesetsResponseDataAttributesRulesetsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsData,
        )
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems,
        )

        return {
            "data": (GetMultipleRulesetsResponseDataAttributesRulesetsItemsData,),
            "description": (str,),
            "name": (str,),
            "rules": ([GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems],),
            "short_description": (str,),
        }

    attribute_map = {
        "data": "data",
        "description": "description",
        "name": "name",
        "rules": "rules",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        data: GetMultipleRulesetsResponseDataAttributesRulesetsItemsData,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rules: Union[List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems], UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: GetMultipleRulesetsResponseDataAttributesRulesetsItemsData

        :param description:
        :type description: str, optional

        :param name:
        :type name: str, optional

        :param rules:
        :type rules: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems], optional

        :param short_description:
        :type short_description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if rules is not unset:
            kwargs["rules"] = rules
        if short_description is not unset:
            kwargs["short_description"] = short_description
        super().__init__(kwargs)

        self_.data = data
