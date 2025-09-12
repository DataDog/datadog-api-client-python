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
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_mapping import (
        RulesetRespDataAttributesRulesItemsMapping,
    )
    from datadog_api_client.v2.model.ruleset_item_metadata import RulesetItemMetadata
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_query import (
        RulesetRespDataAttributesRulesItemsQuery,
    )
    from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_reference_table import (
        RulesetRespDataAttributesRulesItemsReferenceTable,
    )


class RulesetRespDataAttributesRulesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_mapping import (
            RulesetRespDataAttributesRulesItemsMapping,
        )
        from datadog_api_client.v2.model.ruleset_item_metadata import RulesetItemMetadata
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_query import (
            RulesetRespDataAttributesRulesItemsQuery,
        )
        from datadog_api_client.v2.model.ruleset_resp_data_attributes_rules_items_reference_table import (
            RulesetRespDataAttributesRulesItemsReferenceTable,
        )

        return {
            "enabled": (bool,),
            "mapping": (RulesetRespDataAttributesRulesItemsMapping,),
            "metadata": (RulesetItemMetadata,),
            "name": (str,),
            "query": (RulesetRespDataAttributesRulesItemsQuery,),
            "reference_table": (RulesetRespDataAttributesRulesItemsReferenceTable,),
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
        mapping: Union[RulesetRespDataAttributesRulesItemsMapping, none_type, UnsetType] = unset,
        metadata: Union[RulesetItemMetadata, none_type, UnsetType] = unset,
        query: Union[RulesetRespDataAttributesRulesItemsQuery, none_type, UnsetType] = unset,
        reference_table: Union[RulesetRespDataAttributesRulesItemsReferenceTable, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesetRespDataAttributesRulesItems`` object.

        :param enabled: The ``items`` ``enabled``.
        :type enabled: bool

        :param mapping: The definition of ``RulesetRespDataAttributesRulesItemsMapping`` object.
        :type mapping: RulesetRespDataAttributesRulesItemsMapping, none_type, optional

        :param metadata: The ``items`` ``metadata``.
        :type metadata: RulesetItemMetadata, none_type, optional

        :param name: The ``items`` ``name``.
        :type name: str

        :param query: The definition of ``RulesetRespDataAttributesRulesItemsQuery`` object.
        :type query: RulesetRespDataAttributesRulesItemsQuery, none_type, optional

        :param reference_table: The definition of ``RulesetRespDataAttributesRulesItemsReferenceTable`` object.
        :type reference_table: RulesetRespDataAttributesRulesItemsReferenceTable, none_type, optional
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
