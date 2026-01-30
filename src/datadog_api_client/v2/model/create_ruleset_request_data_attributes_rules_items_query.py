# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query_addition import (
        CreateRulesetRequestDataAttributesRulesItemsQueryAddition,
    )
    from datadog_api_client.v2.model.data_attributes_rules_items_if_tag_exists import (
        DataAttributesRulesItemsIfTagExists,
    )


class CreateRulesetRequestDataAttributesRulesItemsQuery(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query_addition import (
            CreateRulesetRequestDataAttributesRulesItemsQueryAddition,
        )
        from datadog_api_client.v2.model.data_attributes_rules_items_if_tag_exists import (
            DataAttributesRulesItemsIfTagExists,
        )

        return {
            "addition": (CreateRulesetRequestDataAttributesRulesItemsQueryAddition,),
            "case_insensitivity": (bool,),
            "if_not_exists": (bool,),
            "if_tag_exists": (DataAttributesRulesItemsIfTagExists,),
            "query": (str,),
        }

    attribute_map = {
        "addition": "addition",
        "case_insensitivity": "case_insensitivity",
        "if_not_exists": "if_not_exists",
        "if_tag_exists": "if_tag_exists",
        "query": "query",
    }

    def __init__(
        self_,
        addition: Union[CreateRulesetRequestDataAttributesRulesItemsQueryAddition, none_type],
        query: str,
        case_insensitivity: Union[bool, UnsetType] = unset,
        if_not_exists: Union[bool, UnsetType] = unset,
        if_tag_exists: Union[DataAttributesRulesItemsIfTagExists, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateRulesetRequestDataAttributesRulesItemsQuery`` object.

        :param addition: The definition of ``CreateRulesetRequestDataAttributesRulesItemsQueryAddition`` object.
        :type addition: CreateRulesetRequestDataAttributesRulesItemsQueryAddition, none_type

        :param case_insensitivity: The ``query`` ``case_insensitivity``.
        :type case_insensitivity: bool, optional

        :param if_not_exists: Deprecated. Use ``if_tag_exists`` instead. The ``query`` ``if_not_exists``. **Deprecated**.
        :type if_not_exists: bool, optional

        :param if_tag_exists: The behavior when the tag already exists.
        :type if_tag_exists: DataAttributesRulesItemsIfTagExists, optional

        :param query: The ``query`` ``query``.
        :type query: str
        """
        if case_insensitivity is not unset:
            kwargs["case_insensitivity"] = case_insensitivity
        if if_not_exists is not unset:
            kwargs["if_not_exists"] = if_not_exists
        if if_tag_exists is not unset:
            kwargs["if_tag_exists"] = if_tag_exists
        super().__init__(kwargs)

        self_.addition = addition
        self_.query = query
