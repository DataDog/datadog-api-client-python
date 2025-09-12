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
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_reference_table_field_pairs_items import (
        RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems,
    )


class RulesetRespDataAttributesRulesItemsReferenceTable(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_reference_table_field_pairs_items import (
            RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems,
        )

        return {
            "case_insensitivity": (bool,),
            "field_pairs": ([RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems],),
            "if_not_exists": (bool,),
            "source_keys": ([str],),
            "table_name": (str,),
        }

    attribute_map = {
        "case_insensitivity": "case_insensitivity",
        "field_pairs": "field_pairs",
        "if_not_exists": "if_not_exists",
        "source_keys": "source_keys",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        field_pairs: List[RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems],
        source_keys: List[str],
        table_name: str,
        case_insensitivity: Union[bool, UnsetType] = unset,
        if_not_exists: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesetRespDataAttributesRulesItemsReferenceTable`` object.

        :param case_insensitivity: The ``reference_table`` ``case_insensitivity``.
        :type case_insensitivity: bool, optional

        :param field_pairs: The ``reference_table`` ``field_pairs``.
        :type field_pairs: [RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems]

        :param if_not_exists: The ``reference_table`` ``if_not_exists``.
        :type if_not_exists: bool, optional

        :param source_keys: The ``reference_table`` ``source_keys``.
        :type source_keys: [str]

        :param table_name: The ``reference_table`` ``table_name``.
        :type table_name: str
        """
        if case_insensitivity is not unset:
            kwargs["case_insensitivity"] = case_insensitivity
        if if_not_exists is not unset:
            kwargs["if_not_exists"] = if_not_exists
        super().__init__(kwargs)

        self_.field_pairs = field_pairs
        self_.source_keys = source_keys
        self_.table_name = table_name
