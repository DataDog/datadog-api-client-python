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
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_query_addition import (
        RulesetRespDataAttributesRulesItemsQueryAddition,
    )


class RulesetRespDataAttributesRulesItemsQuery(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_query_addition import (
            RulesetRespDataAttributesRulesItemsQueryAddition,
        )

        return {
            "addition": (RulesetRespDataAttributesRulesItemsQueryAddition,),
            "case_insensitivity": (bool,),
            "if_not_exists": (bool,),
            "query": (str,),
        }

    attribute_map = {
        "addition": "addition",
        "case_insensitivity": "case_insensitivity",
        "if_not_exists": "if_not_exists",
        "query": "query",
    }

    def __init__(
        self_,
        addition: Union[RulesetRespDataAttributesRulesItemsQueryAddition, none_type],
        if_not_exists: bool,
        query: str,
        case_insensitivity: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesetRespDataAttributesRulesItemsQuery`` object.

        :param addition: The definition of ``RulesetRespDataAttributesRulesItemsQueryAddition`` object.
        :type addition: RulesetRespDataAttributesRulesItemsQueryAddition, none_type

        :param case_insensitivity: The ``query`` ``case_insensitivity``.
        :type case_insensitivity: bool, optional

        :param if_not_exists: The ``query`` ``if_not_exists``.
        :type if_not_exists: bool

        :param query: The ``query`` ``query``.
        :type query: str
        """
        if case_insensitivity is not unset:
            kwargs["case_insensitivity"] = case_insensitivity
        super().__init__(kwargs)

        self_.addition = addition
        self_.if_not_exists = if_not_exists
        self_.query = query
