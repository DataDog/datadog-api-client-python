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
    from datadog_api_client.v2.model.core_weave_cloud_logs_integration_dataflow_request import (
        CoreWeaveCloudLogsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.core_weave_cloud_metrics_integration_dataflow_request import (
        CoreWeaveCloudMetricsIntegrationDataflowRequest,
    )


class CoreWeaveCloudIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_logs_integration_dataflow_request import (
            CoreWeaveCloudLogsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.core_weave_cloud_metrics_integration_dataflow_request import (
            CoreWeaveCloudMetricsIntegrationDataflowRequest,
        )

        return {
            "coreweave_cloud_logs": (CoreWeaveCloudLogsIntegrationDataflowRequest,),
            "coreweave_cloud_metrics": (CoreWeaveCloudMetricsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "coreweave_cloud_logs": "coreweave-cloud-logs",
        "coreweave_cloud_metrics": "coreweave-cloud-metrics",
    }

    def __init__(
        self_,
        coreweave_cloud_logs: Union[CoreWeaveCloudLogsIntegrationDataflowRequest, UnsetType] = unset,
        coreweave_cloud_metrics: Union[CoreWeaveCloudMetricsIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from CoreWeave, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted dataflow ids keep their current values. Collection runs with the API access token in ``authentication`` , whose user must have the Observability Viewer role; a dataflow enabled without that role is stored but collects no data.

        :param coreweave_cloud_logs: Service logs for CoreWeave-managed components in each CoreWeave region: the CKS control plane (such as ``kube-apiserver`` and ``etcd`` ), CoreWeave add-on services in the ``cw-*`` and ``kube-system`` namespaces, SUNK, and node system logs such as ``kubelet`` and ``containerd``. Logs from your own workloads and Kubernetes audit logs are not collected. Logs are sent with ``source:coreweave`` , with CoreWeave log labels such as ``namespace`` , ``app`` , and ``systemd_unit`` added as tags.
        :type coreweave_cloud_logs: CoreWeaveCloudLogsIntegrationDataflowRequest, optional

        :param coreweave_cloud_metrics: Metrics from your CoreWeave organization: CoreWeave service metrics collected through its PromQL-compatible Prometheus endpoint, plus the ``coreweave.*`` namespaces from CoreWeave products such as Kubernetes, Database, Distributed File Storage, Inference, and Object Storage. Compute metrics ( ``coreweave.bare_metal`` , ``coreweave.gpu`` , ``coreweave.nccl`` , and ``coreweave.node`` ) are in Preview. Container metrics are not collected; install the Datadog Agent on your clusters for those.
        :type coreweave_cloud_metrics: CoreWeaveCloudMetricsIntegrationDataflowRequest, optional
        """
        if coreweave_cloud_logs is not unset:
            kwargs["coreweave_cloud_logs"] = coreweave_cloud_logs
        if coreweave_cloud_metrics is not unset:
            kwargs["coreweave_cloud_metrics"] = coreweave_cloud_metrics
        super().__init__(kwargs)
