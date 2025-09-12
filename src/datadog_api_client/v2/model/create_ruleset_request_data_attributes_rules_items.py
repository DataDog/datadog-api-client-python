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
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_mapping import (
        CreateRulesetRequestDataAttributesRulesItemsMapping,
    )
    from datadog_api_client.v2.model.ruleset_item_metadata import RulesetItemMetadata
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query import (
        CreateRulesetRequestDataAttributesRulesItemsQuery,
    )
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_reference_table import (
        CreateRulesetRequestDataAttributesRulesItemsReferenceTable,
    )


class CreateRulesetRequestDataAttributesRulesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_mapping import (
            CreateRulesetRequestDataAttributesRulesItemsMapping,
        )
        from datadog_api_client.v2.model.ruleset_item_metadata import RulesetItemMetadata
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query import (
            CreateRulesetRequestDataAttributesRulesItemsQuery,
        )
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_reference_table import (
            CreateRulesetRequestDataAttributesRulesItemsReferenceTable,
        )

        return {
            "enabled": (bool,),
            "mapping": (CreateRulesetRequestDataAttributesRulesItemsMapping,),
            "metadata": (RulesetItemMetadata,),
            "name": (str,),
            "query": (CreateRulesetRequestDataAttributesRulesItemsQuery,),
            "reference_table": (CreateRulesetRequestDataAttributesRulesItemsReferenceTable,),
        }

    attribute_map = {
        "enabled": "enabled",
        "mapping": "mapping",
        "metadata": "metadata",
        "name": "name",
        "query": "query",
        "reference_table": "reference_table",
    }

    def __init__(
        self_,
        enabled: bool,
        name: str,
        mapping: Union[CreateRulesetRequestDataAttributesRulesItemsMapping, none_type, UnsetType] = unset,
        metadata: Union[RulesetItemMetadata, none_type, UnsetType] = unset,
        query: Union[CreateRulesetRequestDataAttributesRulesItemsQuery, none_type, UnsetType] = unset,
        reference_table: Union[
            CreateRulesetRequestDataAttributesRulesItemsReferenceTable, none_type, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateRulesetRequestDataAttributesRulesItems`` object.

        :param enabled: The ``items`` ``enabled``.
        :type enabled: bool

        :param mapping: The definition of ``CreateRulesetRequestDataAttributesRulesItemsMapping`` object.
        :type mapping: CreateRulesetRequestDataAttributesRulesItemsMapping, none_type, optional

        :param metadata: The ``items`` ``metadata``.
        :type metadata: RulesetItemMetadata, none_type, optional

        :param name: The ``items`` ``name``.
        :type name: str

        :param query: The definition of ``CreateRulesetRequestDataAttributesRulesItemsQuery`` object.
        :type query: CreateRulesetRequestDataAttributesRulesItemsQuery, none_type, optional

        :param reference_table: The definition of ``CreateRulesetRequestDataAttributesRulesItemsReferenceTable`` object.
        :type reference_table: CreateRulesetRequestDataAttributesRulesItemsReferenceTable, none_type, optional
        """
        if mapping is not unset:
            kwargs["mapping"] = mapping
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if query is not unset:
            kwargs["query"] = query
        if reference_table is not unset:
            kwargs["reference_table"] = reference_table
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.name = name
