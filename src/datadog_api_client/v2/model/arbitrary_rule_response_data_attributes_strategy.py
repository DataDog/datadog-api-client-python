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
            "method": (str,),
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
        "method": "method",
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

        :param method: The ``strategy`` ``method``.
        :type method: str
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
        super().__init__(kwargs)

        self_.method = method
