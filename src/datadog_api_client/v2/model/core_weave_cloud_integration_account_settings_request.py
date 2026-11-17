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


class CoreWeaveCloudIntegrationAccountSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "account_tags": ([str],),
            "cluster_filters": ([str],),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "cluster_filters": "cluster_filters",
    }

    def __init__(
        self_,
        account_tags: Union[List[str], UnsetType] = unset,
        cluster_filters: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for creating the CoreWeave integration account.

        :param account_tags: Tags added to all metrics and logs collected from this CoreWeave account. Defaults to no tags.
        :type account_tags: [str], optional

        :param cluster_filters: Tag-filter rules limiting metric collection to matching clusters, for cost savings. Include rules ( ``key:value`` ) are combined with OR, exclusion rules ( ``!key:value`` ) are then applied with AND, and ``?`` and ``*`` are wildcards; for example ``cluster:prod-*`` collects only matching clusters and ``!cluster:dev`` excludes a cluster. Defaults to no filters: every cluster is collected. Only cluster-scoped metrics are filtered; billing and object storage metrics are always collected.
        :type cluster_filters: [str], optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if cluster_filters is not unset:
            kwargs["cluster_filters"] = cluster_filters
        super().__init__(kwargs)
