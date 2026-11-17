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
    from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_response import (
        NebiusCloudCostCollectionIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_response import (
        NebiusCloudLogsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_resources_integration_dataflow_response import (
        NebiusCloudResourcesIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_service_quota_collection_integration_dataflow_response import (
        NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse,
    )


class NebiusCloudIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_response import (
            NebiusCloudCostCollectionIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_response import (
            NebiusCloudLogsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.nebius_cloud_resources_integration_dataflow_response import (
            NebiusCloudResourcesIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.nebius_cloud_service_quota_collection_integration_dataflow_response import (
            NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse,
        )

        return {
            "nebius_cloud_cost_collection": (NebiusCloudCostCollectionIntegrationDataflowResponse,),
            "nebius_cloud_logs": (NebiusCloudLogsIntegrationDataflowResponse,),
            "nebius_cloud_resources": (NebiusCloudResourcesIntegrationDataflowResponse,),
            "nebius_cloud_service_quota_collection": (NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse,),
        }

    attribute_map = {
        "nebius_cloud_cost_collection": "nebius-cloud-cost-collection",
        "nebius_cloud_logs": "nebius-cloud-logs",
        "nebius_cloud_resources": "nebius-cloud-resources",
        "nebius_cloud_service_quota_collection": "nebius-cloud-service-quota-collection",
    }

    def __init__(
        self_,
        nebius_cloud_cost_collection: Union[NebiusCloudCostCollectionIntegrationDataflowResponse, UnsetType] = unset,
        nebius_cloud_logs: Union[NebiusCloudLogsIntegrationDataflowResponse, UnsetType] = unset,
        nebius_cloud_resources: Union[NebiusCloudResourcesIntegrationDataflowResponse, UnsetType] = unset,
        nebius_cloud_service_quota_collection: Union[
            NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Nebius Cloud, keyed by dataflow id.

        :param nebius_cloud_cost_collection: Cloud cost data read from a Nebius Object Storage bucket export and used by `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Requires a bucket holding your cost export and a Nebius access key pair that can read it; without both this dataflow collects no data.
        :type nebius_cloud_cost_collection: NebiusCloudCostCollectionIntegrationDataflowResponse, optional

        :param nebius_cloud_logs: Logs from your Nebius tenant: Kubernetes control plane and audit logs, tenant-level audit events, compute serial console logs, cloud apps and AI inference logs, PostgreSQL logs, and MLflow logs, collected from the services named in ``settings.enabled_services``.
        :type nebius_cloud_logs: NebiusCloudLogsIntegrationDataflowResponse, optional

        :param nebius_cloud_resources: Metadata about resources in your Nebius tenant, such as compute instances and Kubernetes clusters.
        :type nebius_cloud_resources: NebiusCloudResourcesIntegrationDataflowResponse, optional

        :param nebius_cloud_service_quota_collection: Usage metrics tracked against your Nebius service quotas, such as ``nebius_cloud.servicequota.percentage_used`` and ``nebius_cloud.servicequota.limit``.
        :type nebius_cloud_service_quota_collection: NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse, optional
        """
        if nebius_cloud_cost_collection is not unset:
            kwargs["nebius_cloud_cost_collection"] = nebius_cloud_cost_collection
        if nebius_cloud_logs is not unset:
            kwargs["nebius_cloud_logs"] = nebius_cloud_logs
        if nebius_cloud_resources is not unset:
            kwargs["nebius_cloud_resources"] = nebius_cloud_resources
        if nebius_cloud_service_quota_collection is not unset:
            kwargs["nebius_cloud_service_quota_collection"] = nebius_cloud_service_quota_collection
        super().__init__(kwargs)
