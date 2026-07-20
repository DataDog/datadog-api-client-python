# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tag_indexing_rule_dynamic_tags import TagIndexingRuleDynamicTags
    from datadog_api_client.v2.model.tag_indexing_rule_metric_match import TagIndexingRuleMetricMatch


class TagIndexingRuleOptionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_dynamic_tags import TagIndexingRuleDynamicTags
        from datadog_api_client.v2.model.tag_indexing_rule_metric_match import TagIndexingRuleMetricMatch

        return {
            "dynamic_tags": (TagIndexingRuleDynamicTags,),
            "manage_preexisting_metrics": (bool,),
            "metric_match": (TagIndexingRuleMetricMatch,),
            "override_previous_rules": (bool,),
        }

    attribute_map = {
        "dynamic_tags": "dynamic_tags",
        "manage_preexisting_metrics": "manage_preexisting_metrics",
        "metric_match": "metric_match",
        "override_previous_rules": "override_previous_rules",
    }

    def __init__(
        self_,
        dynamic_tags: Union[TagIndexingRuleDynamicTags, UnsetType] = unset,
        manage_preexisting_metrics: Union[bool, UnsetType] = unset,
        metric_match: Union[TagIndexingRuleMetricMatch, UnsetType] = unset,
        override_previous_rules: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data payload for tag indexing rule options.

        :param dynamic_tags: Options for dynamic tag indexing applied per metric, such as tags filtered by query usage.

            Before a tag key is dropped by this rule, two grace period conditions must be met:

            #. The metric must be submitted for at least as long as the selected window.
            #. A tag key must have been submitted for at least 15 days.

            Any metric or tag key that does not meet these conditions are excluded from this
            indexing rule. The ``exclude_not_*`` fields require ``exclude_tags_mode`` to be set to ``true``.
        :type dynamic_tags: TagIndexingRuleDynamicTags, optional

        :param manage_preexisting_metrics: When true, the rule applies to metrics that were ingested before the rule was created.
        :type manage_preexisting_metrics: bool, optional

        :param metric_match: Criteria for matching metrics based on query state.
        :type metric_match: TagIndexingRuleMetricMatch, optional

        :param override_previous_rules: When true, this rule's tag list overrides tags configured by earlier rules for the same metric. When false (default), tags from all matching rules are combined.
        :type override_previous_rules: bool, optional
        """
        if dynamic_tags is not unset:
            kwargs["dynamic_tags"] = dynamic_tags
        if manage_preexisting_metrics is not unset:
            kwargs["manage_preexisting_metrics"] = manage_preexisting_metrics
        if metric_match is not unset:
            kwargs["metric_match"] = metric_match
        if override_previous_rules is not unset:
            kwargs["override_previous_rules"] = override_previous_rules
        super().__init__(kwargs)
