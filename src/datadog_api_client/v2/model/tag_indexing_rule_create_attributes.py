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
    from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions


class TagIndexingRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions

        return {
            "exclude_tags_mode": (bool,),
            "ignored_metric_name_matches": ([str],),
            "metric_name_matches": ([str],),
            "name": (str,),
            "options": (TagIndexingRuleOptions,),
            "tags": ([str],),
        }

    attribute_map = {
        "exclude_tags_mode": "exclude_tags_mode",
        "ignored_metric_name_matches": "ignored_metric_name_matches",
        "metric_name_matches": "metric_name_matches",
        "name": "name",
        "options": "options",
        "tags": "tags",
    }

    def __init__(
        self_,
        metric_name_matches: List[str],
        name: str,
        exclude_tags_mode: Union[bool, UnsetType] = unset,
        ignored_metric_name_matches: Union[List[str], UnsetType] = unset,
        options: Union[TagIndexingRuleOptions, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a tag indexing rule.

        :param exclude_tags_mode: When true, the rule excludes the listed tags and indexes all others. When false (default), the rule includes only the listed tags.
        :type exclude_tags_mode: bool, optional

        :param ignored_metric_name_matches: Metric name prefixes excluded from the rule's scope.
        :type ignored_metric_name_matches: [str], optional

        :param metric_name_matches: Metric name prefixes (glob patterns) this rule applies to.
        :type metric_name_matches: [str]

        :param name: Human-readable name for the rule.
        :type name: str

        :param options: Versioned configuration options for a tag indexing rule.
        :type options: TagIndexingRuleOptions, optional

        :param tags: Tag keys managed by this rule.
        :type tags: [str], optional
        """
        if exclude_tags_mode is not unset:
            kwargs["exclude_tags_mode"] = exclude_tags_mode
        if ignored_metric_name_matches is not unset:
            kwargs["ignored_metric_name_matches"] = ignored_metric_name_matches
        if options is not unset:
            kwargs["options"] = options
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.metric_name_matches = metric_name_matches
        self_.name = name
