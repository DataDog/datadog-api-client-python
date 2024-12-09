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
    from datadog_api_client.v2.model.aws_namespace_filters import AWSNamespaceFilters
    from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
    from datadog_api_client.v2.model.aws_namespace_filters_exclude_only import AWSNamespaceFiltersExcludeOnly
    from datadog_api_client.v2.model.aws_namespace_filters_include_only import AWSNamespaceFiltersIncludeOnly


class AWSMetricsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_namespace_filters import AWSNamespaceFilters
        from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter

        return {
            "automute_enabled": (bool,),
            "collect_cloudwatch_alarms": (bool,),
            "collect_custom_metrics": (bool,),
            "enabled": (bool,),
            "namespace_filters": (AWSNamespaceFilters,),
            "tag_filters": ([AWSNamespaceTagFilter],),
        }

    attribute_map = {
        "automute_enabled": "automute_enabled",
        "collect_cloudwatch_alarms": "collect_cloudwatch_alarms",
        "collect_custom_metrics": "collect_custom_metrics",
        "enabled": "enabled",
        "namespace_filters": "namespace_filters",
        "tag_filters": "tag_filters",
    }

    def __init__(
        self_,
        automute_enabled: Union[bool, UnsetType] = unset,
        collect_cloudwatch_alarms: Union[bool, UnsetType] = unset,
        collect_custom_metrics: Union[bool, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        namespace_filters: Union[
            AWSNamespaceFilters, AWSNamespaceFiltersExcludeOnly, AWSNamespaceFiltersIncludeOnly, UnsetType
        ] = unset,
        tag_filters: Union[List[AWSNamespaceTagFilter], UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Metrics Collection config.

        :param automute_enabled: Enable EC2 automute for AWS metrics. Defaults to ``true``.
        :type automute_enabled: bool, optional

        :param collect_cloudwatch_alarms: Enable CloudWatch alarms collection. Defaults to ``false``.
        :type collect_cloudwatch_alarms: bool, optional

        :param collect_custom_metrics: Enable custom metrics collection. Defaults to ``false``.
        :type collect_custom_metrics: bool, optional

        :param enabled: Enable AWS metrics collection. Defaults to ``true``.
        :type enabled: bool, optional

        :param namespace_filters: AWS Metrics namespace filters. Defaults to ``exclude_only``.
        :type namespace_filters: AWSNamespaceFilters, optional

        :param tag_filters: AWS Metrics collection tag filters list. Defaults to ``[]``.
        :type tag_filters: [AWSNamespaceTagFilter], optional
        """
        if automute_enabled is not unset:
            kwargs["automute_enabled"] = automute_enabled
        if collect_cloudwatch_alarms is not unset:
            kwargs["collect_cloudwatch_alarms"] = collect_cloudwatch_alarms
        if collect_custom_metrics is not unset:
            kwargs["collect_custom_metrics"] = collect_custom_metrics
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if namespace_filters is not unset:
            kwargs["namespace_filters"] = namespace_filters
        if tag_filters is not unset:
            kwargs["tag_filters"] = tag_filters
        super().__init__(kwargs)
