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
    from datadog_api_client.v2.model.elastic_cloud_detailed_index_stats_integration_dataflow_response import (
        ElasticCloudDetailedIndexStatsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_index_stats_integration_dataflow_response import (
        ElasticCloudIndexStatsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_metrics_integration_dataflow_response import (
        ElasticCloudMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_pending_task_stats_integration_dataflow_response import (
        ElasticCloudPendingTaskStatsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_primary_shard_graceful_timeout_integration_dataflow_response import (
        ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_primary_shard_stats_integration_dataflow_response import (
        ElasticCloudPrimaryShardStatsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_shard_allocation_stats_integration_dataflow_response import (
        ElasticCloudShardAllocationStatsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_slm_stats_integration_dataflow_response import (
        ElasticCloudSlmStatsIntegrationDataflowResponse,
    )


class ElasticCloudIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_detailed_index_stats_integration_dataflow_response import (
            ElasticCloudDetailedIndexStatsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_index_stats_integration_dataflow_response import (
            ElasticCloudIndexStatsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_metrics_integration_dataflow_response import (
            ElasticCloudMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_pending_task_stats_integration_dataflow_response import (
            ElasticCloudPendingTaskStatsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_primary_shard_graceful_timeout_integration_dataflow_response import (
            ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_primary_shard_stats_integration_dataflow_response import (
            ElasticCloudPrimaryShardStatsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_shard_allocation_stats_integration_dataflow_response import (
            ElasticCloudShardAllocationStatsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_slm_stats_integration_dataflow_response import (
            ElasticCloudSlmStatsIntegrationDataflowResponse,
        )

        return {
            "elastic_cloud_detailed_index_stats": (ElasticCloudDetailedIndexStatsIntegrationDataflowResponse,),
            "elastic_cloud_index_stats": (ElasticCloudIndexStatsIntegrationDataflowResponse,),
            "elastic_cloud_metrics": (ElasticCloudMetricsIntegrationDataflowResponse,),
            "elastic_cloud_pending_task_stats": (ElasticCloudPendingTaskStatsIntegrationDataflowResponse,),
            "elastic_cloud_primary_shard_graceful_timeout": (
                ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowResponse,
            ),
            "elastic_cloud_primary_shard_stats": (ElasticCloudPrimaryShardStatsIntegrationDataflowResponse,),
            "elastic_cloud_shard_allocation_stats": (ElasticCloudShardAllocationStatsIntegrationDataflowResponse,),
            "elastic_cloud_slm_stats": (ElasticCloudSlmStatsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "elastic_cloud_detailed_index_stats": "elastic-cloud-detailed-index-stats",
        "elastic_cloud_index_stats": "elastic-cloud-index-stats",
        "elastic_cloud_metrics": "elastic-cloud-metrics",
        "elastic_cloud_pending_task_stats": "elastic-cloud-pending-task-stats",
        "elastic_cloud_primary_shard_graceful_timeout": "elastic-cloud-primary-shard-graceful-timeout",
        "elastic_cloud_primary_shard_stats": "elastic-cloud-primary-shard-stats",
        "elastic_cloud_shard_allocation_stats": "elastic-cloud-shard-allocation-stats",
        "elastic_cloud_slm_stats": "elastic-cloud-slm-stats",
    }

    def __init__(
        self_,
        elastic_cloud_detailed_index_stats: Union[
            ElasticCloudDetailedIndexStatsIntegrationDataflowResponse, UnsetType
        ] = unset,
        elastic_cloud_index_stats: Union[ElasticCloudIndexStatsIntegrationDataflowResponse, UnsetType] = unset,
        elastic_cloud_metrics: Union[ElasticCloudMetricsIntegrationDataflowResponse, UnsetType] = unset,
        elastic_cloud_pending_task_stats: Union[
            ElasticCloudPendingTaskStatsIntegrationDataflowResponse, UnsetType
        ] = unset,
        elastic_cloud_primary_shard_graceful_timeout: Union[
            ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowResponse, UnsetType
        ] = unset,
        elastic_cloud_primary_shard_stats: Union[
            ElasticCloudPrimaryShardStatsIntegrationDataflowResponse, UnsetType
        ] = unset,
        elastic_cloud_shard_allocation_stats: Union[
            ElasticCloudShardAllocationStatsIntegrationDataflowResponse, UnsetType
        ] = unset,
        elastic_cloud_slm_stats: Union[ElasticCloudSlmStatsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dataflows configured on the Elastic Cloud integration account, keyed by dataflow id.

        :param elastic_cloud_detailed_index_stats: The Elastic Cloud detailed index stats dataflow.
        :type elastic_cloud_detailed_index_stats: ElasticCloudDetailedIndexStatsIntegrationDataflowResponse, optional

        :param elastic_cloud_index_stats: The Elastic Cloud index stats dataflow.
        :type elastic_cloud_index_stats: ElasticCloudIndexStatsIntegrationDataflowResponse, optional

        :param elastic_cloud_metrics: The Elastic Cloud metrics dataflow.
        :type elastic_cloud_metrics: ElasticCloudMetricsIntegrationDataflowResponse, optional

        :param elastic_cloud_pending_task_stats: The Elastic Cloud pending task stats dataflow.
        :type elastic_cloud_pending_task_stats: ElasticCloudPendingTaskStatsIntegrationDataflowResponse, optional

        :param elastic_cloud_primary_shard_graceful_timeout: The Elastic Cloud primary shard graceful timeout dataflow.
        :type elastic_cloud_primary_shard_graceful_timeout: ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowResponse, optional

        :param elastic_cloud_primary_shard_stats: The Elastic Cloud primary shard stats dataflow.
        :type elastic_cloud_primary_shard_stats: ElasticCloudPrimaryShardStatsIntegrationDataflowResponse, optional

        :param elastic_cloud_shard_allocation_stats: The Elastic Cloud shard allocation stats dataflow.
        :type elastic_cloud_shard_allocation_stats: ElasticCloudShardAllocationStatsIntegrationDataflowResponse, optional

        :param elastic_cloud_slm_stats: The Elastic Cloud snapshot lifecycle management stats dataflow.
        :type elastic_cloud_slm_stats: ElasticCloudSlmStatsIntegrationDataflowResponse, optional
        """
        if elastic_cloud_detailed_index_stats is not unset:
            kwargs["elastic_cloud_detailed_index_stats"] = elastic_cloud_detailed_index_stats
        if elastic_cloud_index_stats is not unset:
            kwargs["elastic_cloud_index_stats"] = elastic_cloud_index_stats
        if elastic_cloud_metrics is not unset:
            kwargs["elastic_cloud_metrics"] = elastic_cloud_metrics
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
