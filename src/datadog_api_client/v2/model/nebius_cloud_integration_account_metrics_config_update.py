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


class NebiusCloudIntegrationAccountMetricsConfigUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "cluster_filters": ([str],),
        }

    attribute_map = {
        "cluster_filters": "cluster_filters",
    }

    def __init__(self_, cluster_filters: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Configuration for metric collection. Only the fields provided are changed.

        :param cluster_filters: Tag-filter rules limiting metric collection to matching Kubernetes clusters. Sending metrics_config replaces the stored object's cluster_filters list; omit it to keep the stored value. Include rules ( ``key:value`` ) are combined with OR, exclusion rules ( ``!key:value`` ) are then applied with AND, and ``?`` and ``*`` are wildcards.
        :type cluster_filters: [str], optional
        """
        if cluster_filters is not unset:
            kwargs["cluster_filters"] = cluster_filters
        super().__init__(kwargs)
