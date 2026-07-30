# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ElasticCloudSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cat_allocation_stats_enabled": (bool,),
            "detailed_index_stats_enabled": (bool,),
            "index_stats_enabled": (bool,),
            "pending_task_stats_enabled": (bool,),
            "pshard_graceful_to_enabled": (bool,),
            "pshard_stats_enabled": (bool,),
            "slm_stats_enabled": (bool,),
            "tags": ([str],),
            "url": (str,),
        }

    attribute_map = {
        "cat_allocation_stats_enabled": "cat_allocation_stats_enabled",
        "detailed_index_stats_enabled": "detailed_index_stats_enabled",
        "index_stats_enabled": "index_stats_enabled",
        "pending_task_stats_enabled": "pending_task_stats_enabled",
        "pshard_graceful_to_enabled": "pshard_graceful_to_enabled",
        "pshard_stats_enabled": "pshard_stats_enabled",
        "slm_stats_enabled": "slm_stats_enabled",
        "tags": "tags",
        "url": "url",
    }

    def __init__(
        self_,
        url: str,
        cat_allocation_stats_enabled: Union[bool, UnsetType] = unset,
        detailed_index_stats_enabled: Union[bool, UnsetType] = unset,
        index_stats_enabled: Union[bool, UnsetType] = unset,
        pending_task_stats_enabled: Union[bool, UnsetType] = unset,
        pshard_graceful_to_enabled: Union[bool, UnsetType] = unset,
        pshard_stats_enabled: Union[bool, UnsetType] = unset,
        slm_stats_enabled: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Elastic Cloud monitoring interface settings.

        :param cat_allocation_stats_enabled: Enable to collect shard allocation metrics.
        :type cat_allocation_stats_enabled: bool, optional

        :param detailed_index_stats_enabled: Enable to collect index-specific stats.
        :type detailed_index_stats_enabled: bool, optional

        :param index_stats_enabled: Enable to collect metrics about the indices in your cluster.
        :type index_stats_enabled: bool, optional

        :param pending_task_stats_enabled: Enable to collect metrics about pending tasks.
        :type pending_task_stats_enabled: bool, optional

        :param pshard_graceful_to_enabled: Enable to collect all metrics even if primary shard metric collection times out.
        :type pshard_graceful_to_enabled: bool, optional

        :param pshard_stats_enabled: Enable to collect metrics over primary shards.
        :type pshard_stats_enabled: bool, optional

        :param slm_stats_enabled: Enable to collect snapshot lifecycle management metrics.
        :type slm_stats_enabled: bool, optional

        :param tags: Custom tags for this deployment.
        :type tags: [str], optional

        :param url: Deployment URL.
        :type url: str
        """
        if cat_allocation_stats_enabled is not unset:
            kwargs["cat_allocation_stats_enabled"] = cat_allocation_stats_enabled
        if detailed_index_stats_enabled is not unset:
            kwargs["detailed_index_stats_enabled"] = detailed_index_stats_enabled
        if index_stats_enabled is not unset:
            kwargs["index_stats_enabled"] = index_stats_enabled
        if pending_task_stats_enabled is not unset:
            kwargs["pending_task_stats_enabled"] = pending_task_stats_enabled
        if pshard_graceful_to_enabled is not unset:
            kwargs["pshard_graceful_to_enabled"] = pshard_graceful_to_enabled
        if pshard_stats_enabled is not unset:
            kwargs["pshard_stats_enabled"] = pshard_stats_enabled
        if slm_stats_enabled is not unset:
            kwargs["slm_stats_enabled"] = slm_stats_enabled
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.url = url
