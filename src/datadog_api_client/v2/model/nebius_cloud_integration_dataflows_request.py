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
    from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_request import (
        NebiusCloudCostCollectionIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_request import (
        NebiusCloudLogsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.nebius_cloud_resources_integration_dataflow_request import (
        NebiusCloudResourcesIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.nebius_cloud_service_quota_collection_integration_dataflow_request import (
        NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest,
    )


class NebiusCloudIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_request import (
            NebiusCloudCostCollectionIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_request import (
            NebiusCloudLogsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.nebius_cloud_resources_integration_dataflow_request import (
            NebiusCloudResourcesIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.nebius_cloud_service_quota_collection_integration_dataflow_request import (
            NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest,
        )

        return {
            "nebius_cloud_cost_collection": (NebiusCloudCostCollectionIntegrationDataflowRequest,),
            "nebius_cloud_logs": (NebiusCloudLogsIntegrationDataflowRequest,),
            "nebius_cloud_resources": (NebiusCloudResourcesIntegrationDataflowRequest,),
            "nebius_cloud_service_quota_collection": (NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest,),
        }

    attribute_map = {
        "nebius_cloud_cost_collection": "nebius-cloud-cost-collection",
        "nebius_cloud_logs": "nebius-cloud-logs",
        "nebius_cloud_resources": "nebius-cloud-resources",
        "nebius_cloud_service_quota_collection": "nebius-cloud-service-quota-collection",
    }

    def __init__(
        self_,
        nebius_cloud_cost_collection: Union[NebiusCloudCostCollectionIntegrationDataflowRequest, UnsetType] = unset,
        nebius_cloud_logs: Union[NebiusCloudLogsIntegrationDataflowRequest, UnsetType] = unset,
        nebius_cloud_resources: Union[NebiusCloudResourcesIntegrationDataflowRequest, UnsetType] = unset,
        nebius_cloud_service_quota_collection: Union[
            NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Nebius Cloud, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to stop or start it, and use ``settings`` to configure what it collects. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow except ``nebius-cloud-cost-collection`` runs as the service account in ``authentication`` , using its authorized key pair and the static API key; enabling one of them without those keys is rejected with a ``422`` response, and one enabled with keys that later expire is stored but collects no data.

        :param nebius_cloud_cost_collection: Cloud cost data read from a Nebius Object Storage bucket export and used by `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Enabling it requires a bucket holding your cost export and a Nebius access key pair that can read it; a request that enables this dataflow without them is rejected with a ``422`` response.
        :type nebius_cloud_cost_collection: NebiusCloudCostCollectionIntegrationDataflowRequest, optional

        :param nebius_cloud_logs: Logs from your Nebius tenant: Kubernetes control plane and audit logs, tenant-level audit events, compute serial console logs, cloud apps and AI inference logs, PostgreSQL logs, and MLflow logs, collected from the services named in ``settings.enabled_services``. ``enabled_services`` is the sole source of truth for what is collected; ``enabled`` set to ``false`` stops log collection, while ``true`` on its own changes nothing. Defaults to no services.
        :type nebius_cloud_logs: NebiusCloudLogsIntegrationDataflowRequest, optional

        :param nebius_cloud_resources: Metadata about resources in your Nebius tenant, such as compute instances and Kubernetes clusters.
        :type nebius_cloud_resources: NebiusCloudResourcesIntegrationDataflowRequest, optional

        :param nebius_cloud_service_quota_collection: Usage metrics tracked against your Nebius service quotas, such as ``nebius_cloud.servicequota.percentage_used`` and ``nebius_cloud.servicequota.limit``.
        :type nebius_cloud_service_quota_collection: NebiusCloudServiceQuotaCollectionIntegrationDataflowRequest, optional
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
