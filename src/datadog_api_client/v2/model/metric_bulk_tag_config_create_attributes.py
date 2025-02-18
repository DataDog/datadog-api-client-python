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
    from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
    from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList


class MetricBulkTagConfigCreateAttributes(ModelNormal):
    validations = {
        "include_actively_queried_tags_window": {
            "inclusive_maximum": 7776000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
        from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

        return {
            "emails": (MetricBulkTagConfigEmailList,),
            "exclude_tags_mode": (bool,),
            "include_actively_queried_tags_window": (float,),
            "override_existing_configurations": (bool,),
            "tags": (MetricBulkTagConfigTagNameList,),
        }

    attribute_map = {
        "emails": "emails",
        "exclude_tags_mode": "exclude_tags_mode",
        "include_actively_queried_tags_window": "include_actively_queried_tags_window",
        "override_existing_configurations": "override_existing_configurations",
        "tags": "tags",
    }

    def __init__(
        self_,
        emails: Union[MetricBulkTagConfigEmailList, UnsetType] = unset,
        exclude_tags_mode: Union[bool, UnsetType] = unset,
        include_actively_queried_tags_window: Union[float, UnsetType] = unset,
        override_existing_configurations: Union[bool, UnsetType] = unset,
        tags: Union[MetricBulkTagConfigTagNameList, UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional parameters for bulk creating metric tag configurations.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: MetricBulkTagConfigEmailList, optional

        :param exclude_tags_mode: When set to true, the configuration will exclude the configured tags and include any other submitted tags.
            When set to false, the configuration will include the configured tags and exclude any other submitted tags.
            Defaults to false.
        :type exclude_tags_mode: bool, optional

        :param include_actively_queried_tags_window: When provided, all tags that have been actively queried are
            configured (and, therefore, remain queryable) for each metric that
            matches the given prefix.  Minimum value is 1 second, and maximum
            value is 7,776,000 seconds (90 days).
        :type include_actively_queried_tags_window: float, optional

        :param override_existing_configurations: When set to true, the configuration overrides any existing
            configurations for the given metric with the new set of tags in this
            configuration request. If false, old configurations are kept and
            are merged with the set of tags in this configuration request.
            Defaults to true.
        :type override_existing_configurations: bool, optional

        :param tags: A list of tag names to apply to the configuration.
        :type tags: MetricBulkTagConfigTagNameList, optional
        """
        if emails is not unset:
            kwargs["emails"] = emails
        if exclude_tags_mode is not unset:
            kwargs["exclude_tags_mode"] = exclude_tags_mode
        if include_actively_queried_tags_window is not unset:
            kwargs["include_actively_queried_tags_window"] = include_actively_queried_tags_window
        if override_existing_configurations is not unset:
            kwargs["override_existing_configurations"] = override_existing_configurations
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
