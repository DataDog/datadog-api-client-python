# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions


class TagIndexingRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions

        return {
            "created_at": (datetime,),
            "created_by_handle": (str,),
            "exclude_tags_mode": (bool,),
            "ignored_metric_name_matches": ([str],),
            "metric_name_matches": ([str],),
            "modified_at": (datetime,),
            "modified_by_handle": (str,),
            "name": (str,),
            "options": (TagIndexingRuleOptions,),
            "rule_order": (int,),
            "tags": ([str],),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "exclude_tags_mode": "exclude_tags_mode",
        "ignored_metric_name_matches": "ignored_metric_name_matches",
        "metric_name_matches": "metric_name_matches",
        "modified_at": "modified_at",
        "modified_by_handle": "modified_by_handle",
        "name": "name",
        "options": "options",
        "rule_order": "rule_order",
        "tags": "tags",
    }
    read_only_vars = {
        "created_at",
        "created_by_handle",
        "modified_at",
        "modified_by_handle",
        "rule_order",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        exclude_tags_mode: Union[bool, UnsetType] = unset,
        ignored_metric_name_matches: Union[List[str], UnsetType] = unset,
        metric_name_matches: Union[List[str], UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        modified_by_handle: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        options: Union[TagIndexingRuleOptions, UnsetType] = unset,
        rule_order: Union[int, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a tag indexing rule.

        :param created_at: Timestamp when the rule was created.
        :type created_at: datetime, optional

        :param created_by_handle: Handle of the user who created the rule.
        :type created_by_handle: str, optional

        :param exclude_tags_mode: When true, the rule excludes the listed tags and indexes all others. When false (default), the rule includes only the listed tags.
        :type exclude_tags_mode: bool, optional

        :param ignored_metric_name_matches: Metric name prefixes excluded from the rule's scope.
        :type ignored_metric_name_matches: [str], optional

        :param metric_name_matches: Metric name prefixes (glob patterns) this rule applies to.
        :type metric_name_matches: [str], optional

        :param modified_at: Timestamp when the rule was last modified.
        :type modified_at: datetime, optional

        :param modified_by_handle: Handle of the user who last modified the rule.
        :type modified_by_handle: str, optional

        :param name: Human-readable name for the rule.
        :type name: str, optional

        :param options: Versioned configuration options for a tag indexing rule.
        :type options: TagIndexingRuleOptions, optional

        :param rule_order: Evaluation order within the org. Lower values are evaluated first. Assigned server-side on create (max+1); pass on update to change the rule's position.
        :type rule_order: int, optional

        :param tags: Tag keys managed by this rule.
        :type tags: [str], optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if exclude_tags_mode is not unset:
            kwargs["exclude_tags_mode"] = exclude_tags_mode
        if ignored_metric_name_matches is not unset:
            kwargs["ignored_metric_name_matches"] = ignored_metric_name_matches
        if metric_name_matches is not unset:
            kwargs["metric_name_matches"] = metric_name_matches
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if modified_by_handle is not unset:
            kwargs["modified_by_handle"] = modified_by_handle
        if name is not unset:
            kwargs["name"] = name
        if options is not unset:
            kwargs["options"] = options
        if rule_order is not unset:
            kwargs["rule_order"] = rule_order
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
