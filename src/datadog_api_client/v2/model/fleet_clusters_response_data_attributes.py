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
    from datadog_api_client.v2.model.fleet_cluster_attributes import FleetClusterAttributes


class FleetClustersResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_cluster_attributes import FleetClusterAttributes

        return {
            "clusters": ([FleetClusterAttributes],),
        }

    attribute_map = {
        "clusters": "clusters",
    }

    def __init__(self_, clusters: Union[List[FleetClusterAttributes], UnsetType] = unset, **kwargs):
        """
        Attributes of the fleet clusters response containing the list of clusters.

        :param clusters: Array of clusters matching the query criteria.
        :type clusters: [FleetClusterAttributes], optional
        """
        if clusters is not unset:
            kwargs["clusters"] = clusters
        super().__init__(kwargs)
