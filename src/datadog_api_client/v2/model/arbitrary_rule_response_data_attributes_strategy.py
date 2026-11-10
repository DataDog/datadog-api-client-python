# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_items import (
        ArbitraryRuleResponseDataAttributesStrategyAllocatedByItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_filters_items import (
        ArbitraryRuleResponseDataAttributesStrategyAllocatedByFiltersItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_based_on_costs_items import (
        ArbitraryRuleResponseDataAttributesStrategyBasedOnCostsItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_evaluate_grouped_by_filters_items import (
        ArbitraryRuleResponseDataAttributesStrategyEvaluateGroupedByFiltersItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_mapping_transform import ArbitraryRuleMappingTransform
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_items_allocated_tags_items import (
        ArbitraryRuleResponseDataAttributesStrategyAllocatedByItemsAllocatedTagsItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_tag_transforms import ArbitraryRuleTagTransforms


class ArbitraryRuleResponseDataAttributesStrategy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_items import (
            ArbitraryRuleResponseDataAttributesStrategyAllocatedByItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_filters_items import (
            ArbitraryRuleResponseDataAttributesStrategyAllocatedByFiltersItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_based_on_costs_items import (
            ArbitraryRuleResponseDataAttributesStrategyBasedOnCostsItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_evaluate_grouped_by_filters_items import (
            ArbitraryRuleResponseDataAttributesStrategyEvaluateGroupedByFiltersItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_mapping_transform import ArbitraryRuleMappingTransform
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy_allocated_by_items_allocated_tags_items import (
            ArbitraryRuleResponseDataAttributesStrategyAllocatedByItemsAllocatedTagsItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_tag_transforms import ArbitraryRuleTagTransforms

        return {
            "allocated_by": ([ArbitraryRuleResponseDataAttributesStrategyAllocatedByItems],),
            "allocated_by_filters": ([ArbitraryRuleResponseDataAttributesStrategyAllocatedByFiltersItems],),
            "allocated_by_tag_keys": ([str],),
            "based_on_costs": ([ArbitraryRuleResponseDataAttributesStrategyBasedOnCostsItems],),
            "based_on_timeseries": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "evaluate_grouped_by_filters": (
                [ArbitraryRuleResponseDataAttributesStrategyEvaluateGroupedByFiltersItems],
            ),
            "evaluate_grouped_by_tag_keys": ([str],),
            "granularity": (str,),
            "mapping_transform": (ArbitraryRuleMappingTransform,),
            "method": (str,),
            "static_tags": ([ArbitraryRuleResponseDataAttributesStrategyAllocatedByItemsAllocatedTagsItems],),
            "supporting_timeseries": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "tag_transforms": (ArbitraryRuleTagTransforms,),
        }

    attribute_map = {
        "allocated_by": "allocated_by",
        "allocated_by_filters": "allocated_by_filters",
        "allocated_by_tag_keys": "allocated_by_tag_keys",
        "based_on_costs": "based_on_costs",
        "based_on_timeseries": "based_on_timeseries",
        "evaluate_grouped_by_filters": "evaluate_grouped_by_filters",
        "evaluate_grouped_by_tag_keys": "evaluate_grouped_by_tag_keys",
        "granularity": "granularity",
        "mapping_transform": "mapping_transform",
        "method": "method",
        "static_tags": "static_tags",
        "supporting_timeseries": "supporting_timeseries",
        "tag_transforms": "tag_transforms",
    }

    def __init__(
        self_,
        method: str,
        allocated_by: Union[List[ArbitraryRuleResponseDataAttributesStrategyAllocatedByItems], UnsetType] = unset,
        allocated_by_filters: Union[
            List[ArbitraryRuleResponseDataAttributesStrategyAllocatedByFiltersItems], UnsetType
        ] = unset,
        allocated_by_tag_keys: Union[List[str], UnsetType] = unset,
        based_on_costs: Union[List[ArbitraryRuleResponseDataAttributesStrategyBasedOnCostsItems], UnsetType] = unset,
        based_on_timeseries: Union[Dict[str, Any], UnsetType] = unset,
        evaluate_grouped_by_filters: Union[
            List[ArbitraryRuleResponseDataAttributesStrategyEvaluateGroupedByFiltersItems], UnsetType
        ] = unset,
        evaluate_grouped_by_tag_keys: Union[List[str], UnsetType] = unset,
        granularity: Union[str, UnsetType] = unset,
        mapping_transform: Union[ArbitraryRuleMappingTransform, UnsetType] = unset,
        static_tags: Union[
            List[ArbitraryRuleResponseDataAttributesStrategyAllocatedByItemsAllocatedTagsItems], UnsetType
        ] = unset,
        supporting_timeseries: Union[Dict[str, Any], none_type, UnsetType] = unset,
        tag_transforms: Union[ArbitraryRuleTagTransforms, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleResponseDataAttributesStrategy`` object.

        :param allocated_by: The ``strategy`` ``allocated_by``.
        :type allocated_by: [ArbitraryRuleResponseDataAttributesStrategyAllocatedByItems], optional

        :param allocated_by_filters: The ``strategy`` ``allocated_by_filters``.
        :type allocated_by_filters: [ArbitraryRuleResponseDataAttributesStrategyAllocatedByFiltersItems], optional

        :param allocated_by_tag_keys: The ``strategy`` ``allocated_by_tag_keys``.
        :type allocated_by_tag_keys: [str], optional

        :param based_on_costs: The ``strategy`` ``based_on_costs``.
        :type based_on_costs: [ArbitraryRuleResponseDataAttributesStrategyBasedOnCostsItems], optional

        :param based_on_timeseries: The rule ``strategy`` ``based_on_timeseries``.
        :type based_on_timeseries: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param evaluate_grouped_by_filters: The ``strategy`` ``evaluate_grouped_by_filters``.
        :type evaluate_grouped_by_filters: [ArbitraryRuleResponseDataAttributesStrategyEvaluateGroupedByFiltersItems], optional

        :param evaluate_grouped_by_tag_keys: The ``strategy`` ``evaluate_grouped_by_tag_keys``.
        :type evaluate_grouped_by_tag_keys: [str], optional

        :param granularity: The ``strategy`` ``granularity``.
        :type granularity: str, optional

        :param mapping_transform: Only supported for ``proportional_timeseries`` and ``even_timeseries`` rules. Creates a synthetic tag from timeseries input rows before ``tag_transforms`` are applied.
        :type mapping_transform: ArbitraryRuleMappingTransform, optional

        :param method: The ``strategy`` ``method``.
        :type method: str

        :param static_tags: Tags added to every cost row allocated by the rule.
        :type static_tags: [ArbitraryRuleResponseDataAttributesStrategyAllocatedByItemsAllocatedTagsItems], optional

        :param supporting_timeseries: Integration metrics query used to calculate coverage.
        :type supporting_timeseries: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param tag_transforms: Only supported for ``proportional_timeseries`` and ``even_timeseries`` rules. Applies tag key renames and tag value transforms to timeseries input rows after ``mapping_transform``.
        :type tag_transforms: ArbitraryRuleTagTransforms, optional
        """
        if allocated_by is not unset:
            kwargs["allocated_by"] = allocated_by
        if allocated_by_filters is not unset:
            kwargs["allocated_by_filters"] = allocated_by_filters
        if allocated_by_tag_keys is not unset:
            kwargs["allocated_by_tag_keys"] = allocated_by_tag_keys
        if based_on_costs is not unset:
            kwargs["based_on_costs"] = based_on_costs
        if based_on_timeseries is not unset:
            kwargs["based_on_timeseries"] = based_on_timeseries
        if evaluate_grouped_by_filters is not unset:
            kwargs["evaluate_grouped_by_filters"] = evaluate_grouped_by_filters
        if evaluate_grouped_by_tag_keys is not unset:
            kwargs["evaluate_grouped_by_tag_keys"] = evaluate_grouped_by_tag_keys
        if granularity is not unset:
            kwargs["granularity"] = granularity
        if mapping_transform is not unset:
            kwargs["mapping_transform"] = mapping_transform
        if static_tags is not unset:
            kwargs["static_tags"] = static_tags
        if supporting_timeseries is not unset:
            kwargs["supporting_timeseries"] = supporting_timeseries
        if tag_transforms is not unset:
            kwargs["tag_transforms"] = tag_transforms
        super().__init__(kwargs)

        self_.method = method
