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
        Dataflows to configure on the Elastic Cloud integration account, keyed by dataflow id.

        :param elastic_cloud_detailed_index_stats: The Elastic Cloud detailed index stats dataflow.
        :type elastic_cloud_detailed_index_stats: ElasticCloudDetailedIndexStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_index_stats: The Elastic Cloud index stats dataflow.
        :type elastic_cloud_index_stats: ElasticCloudIndexStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_pending_task_stats: The Elastic Cloud pending task stats dataflow.
        :type elastic_cloud_pending_task_stats: ElasticCloudPendingTaskStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_primary_shard_graceful_timeout: The Elastic Cloud primary shard graceful timeout dataflow.
        :type elastic_cloud_primary_shard_graceful_timeout: ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest, optional

        :param elastic_cloud_primary_shard_stats: The Elastic Cloud primary shard stats dataflow.
        :type elastic_cloud_primary_shard_stats: ElasticCloudPrimaryShardStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_shard_allocation_stats: The Elastic Cloud shard allocation stats dataflow.
        :type elastic_cloud_shard_allocation_stats: ElasticCloudShardAllocationStatsIntegrationDataflowRequest, optional

        :param elastic_cloud_slm_stats: The Elastic Cloud snapshot lifecycle management stats dataflow.
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
