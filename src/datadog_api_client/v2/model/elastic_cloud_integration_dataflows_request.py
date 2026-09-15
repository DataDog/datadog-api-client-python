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
    from datadog_api_client.v2.model.elastic_cloud_detailed_index_stats_integration_dataflow_request import (
        ElasticCloudDetailedIndexStatsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_index_stats_integration_dataflow_request import (
        ElasticCloudIndexStatsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_pending_task_stats_integration_dataflow_request import (
        ElasticCloudPendingTaskStatsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_primary_shard_graceful_timeout_integration_dataflow_request import (
        ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_primary_shard_stats_integration_dataflow_request import (
        ElasticCloudPrimaryShardStatsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_shard_allocation_stats_integration_dataflow_request import (
        ElasticCloudShardAllocationStatsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_slm_stats_integration_dataflow_request import (
        ElasticCloudSlmStatsIntegrationDataflowRequest,
    )


class ElasticCloudIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_detailed_index_stats_integration_dataflow_request import (
            ElasticCloudDetailedIndexStatsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_index_stats_integration_dataflow_request import (
            ElasticCloudIndexStatsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_pending_task_stats_integration_dataflow_request import (
            ElasticCloudPendingTaskStatsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_primary_shard_graceful_timeout_integration_dataflow_request import (
            ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_primary_shard_stats_integration_dataflow_request import (
            ElasticCloudPrimaryShardStatsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_shard_allocation_stats_integration_dataflow_request import (
            ElasticCloudShardAllocationStatsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_slm_stats_integration_dataflow_request import (
            ElasticCloudSlmStatsIntegrationDataflowRequest,
        )

        return {
            "elastic_cloud_detailed_index_stats": (ElasticCloudDetailedIndexStatsIntegrationDataflowRequest,),
            "elastic_cloud_index_stats": (ElasticCloudIndexStatsIntegrationDataflowRequest,),
            "elastic_cloud_pending_task_stats": (ElasticCloudPendingTaskStatsIntegrationDataflowRequest,),
            "elastic_cloud_primary_shard_graceful_timeout": (
                ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest,
            ),
            "elastic_cloud_primary_shard_stats": (ElasticCloudPrimaryShardStatsIntegrationDataflowRequest,),
            "elastic_cloud_shard_allocation_stats": (ElasticCloudShardAllocationStatsIntegrationDataflowRequest,),
            "elastic_cloud_slm_stats": (ElasticCloudSlmStatsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "elastic_cloud_detailed_index_stats": "elastic-cloud-detailed-index-stats",
        "elastic_cloud_index_stats": "elastic-cloud-index-stats",
        "elastic_cloud_pending_task_stats": "elastic-cloud-pending-task-stats",
        "elastic_cloud_primary_shard_graceful_timeout": "elastic-cloud-primary-shard-graceful-timeout",
        "elastic_cloud_primary_shard_stats": "elastic-cloud-primary-shard-stats",
        "elastic_cloud_shard_allocation_stats": "elastic-cloud-shard-allocation-stats",
        "elastic_cloud_slm_stats": "elastic-cloud-slm-stats",
    }

    def __init__(
        self_,
        elastic_cloud_detailed_index_stats: Union[
            ElasticCloudDetailedIndexStatsIntegrationDataflowRequest, UnsetType
        ] = unset,
        elastic_cloud_index_stats: Union[ElasticCloudIndexStatsIntegrationDataflowRequest, UnsetType] = unset,
        elastic_cloud_pending_task_stats: Union[
            ElasticCloudPendingTaskStatsIntegrationDataflowRequest, UnsetType
        ] = unset,
        elastic_cloud_primary_shard_graceful_timeout: Union[
            ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest, UnsetType
        ] = unset,
        elastic_cloud_primary_shard_stats: Union[
            ElasticCloudPrimaryShardStatsIntegrationDataflowRequest, UnsetType
        ] = unset,
        elastic_cloud_shard_allocation_stats: Union[
            ElasticCloudShardAllocationStatsIntegrationDataflowRequest, UnsetType
        ] = unset,
        elastic_cloud_slm_stats: Union[ElasticCloudSlmStatsIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Elastic Cloud, keyed by dataflow id. Node-level cluster statistics are always collected; each dataflow here adds a further set of metrics on top of that baseline, so set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow queries the deployment as the user in ``authentication`` , so that user's role must hold the required Elasticsearch privileges; a dataflow enabled without them is stored but collects no data.

        :param elastic_cloud_detailed_index_stats: Primary shard metrics broken down per index, rather than aggregated across the cluster.
        :type elastic_cloud_detailed_index_stats: ElasticCloudDetailedIndexStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_index_stats: Metrics for individual indices. Only the indices granted to the role of the user in ``authentication`` are collected.
        :type elastic_cloud_index_stats: ElasticCloudIndexStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_pending_task_stats: Metrics for cluster-level changes that have been submitted but not yet executed.
        :type elastic_cloud_pending_task_stats: ElasticCloudPendingTaskStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_primary_shard_graceful_timeout: Tolerance for slow primary shard requests. Primary shard metrics can grow large enough for the request to time out; enabling this keeps the rest of the collection running when that happens instead of failing the run. Only has an effect alongside ``elastic-cloud-primary-shard-stats``.
        :type elastic_cloud_primary_shard_graceful_timeout: ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest, optional

        :param elastic_cloud_primary_shard_stats: Metrics covering only the cluster's primary shards.
        :type elastic_cloud_primary_shard_stats: ElasticCloudPrimaryShardStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_shard_allocation_stats: Metrics for how many shards are allocated to each data node, and the disk space they use.
        :type elastic_cloud_shard_allocation_stats: ElasticCloudShardAllocationStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_slm_stats: Metrics about the actions taken by snapshot lifecycle management. Requires the ``read_slm`` Elasticsearch cluster privilege on the role of the user in ``authentication`` ; without it this dataflow collects no data.
        :type elastic_cloud_slm_stats: ElasticCloudSlmStatsIntegrationDataflowRequest, optional
        """
        if elastic_cloud_detailed_index_stats is not unset:
            kwargs["elastic_cloud_detailed_index_stats"] = elastic_cloud_detailed_index_stats
        if elastic_cloud_index_stats is not unset:
            kwargs["elastic_cloud_index_stats"] = elastic_cloud_index_stats
        if elastic_cloud_pending_task_stats is not unset:
            kwargs["elastic_cloud_pending_task_stats"] = elastic_cloud_pending_task_stats
        if elastic_cloud_primary_shard_graceful_timeout is not unset:
            kwargs["elastic_cloud_primary_shard_graceful_timeout"] = elastic_cloud_primary_shard_graceful_timeout
        if elastic_cloud_primary_shard_stats is not unset:
            kwargs["elastic_cloud_primary_shard_stats"] = elastic_cloud_primary_shard_stats
        if elastic_cloud_shard_allocation_stats is not unset:
            kwargs["elastic_cloud_shard_allocation_stats"] = elastic_cloud_shard_allocation_stats
        if elastic_cloud_slm_stats is not unset:
            kwargs["elastic_cloud_slm_stats"] = elastic_cloud_slm_stats
        super().__init__(kwargs)
