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
    from datadog_api_client.v2.model.core_weave_cloud_logs_integration_dataflow_response import (
        CoreWeaveCloudLogsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.core_weave_cloud_metrics_integration_dataflow_response import (
        CoreWeaveCloudMetricsIntegrationDataflowResponse,
    )


class CoreWeaveCloudIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_logs_integration_dataflow_response import (
            CoreWeaveCloudLogsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.core_weave_cloud_metrics_integration_dataflow_response import (
            CoreWeaveCloudMetricsIntegrationDataflowResponse,
        )

        return {
            "coreweave_cloud_logs": (CoreWeaveCloudLogsIntegrationDataflowResponse,),
            "coreweave_cloud_metrics": (CoreWeaveCloudMetricsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "coreweave_cloud_logs": "coreweave-cloud-logs",
        "coreweave_cloud_metrics": "coreweave-cloud-metrics",
    }

    def __init__(
        self_,
        coreweave_cloud_logs: Union[CoreWeaveCloudLogsIntegrationDataflowResponse, UnsetType] = unset,
        coreweave_cloud_metrics: Union[CoreWeaveCloudMetricsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from CoreWeave, keyed by dataflow id.

        :param coreweave_cloud_logs: Service logs for CoreWeave-managed components in each CoreWeave region: the CKS control plane (such as ``kube-apiserver`` and ``etcd`` ), CoreWeave add-on services in the ``cw-*`` and ``kube-system`` namespaces, SUNK, and node system logs such as ``kubelet`` and ``containerd``. Logs from your own workloads and Kubernetes audit logs are not collected. Logs are sent with ``source:coreweave`` , with CoreWeave log labels such as ``namespace`` , ``app`` , and ``systemd_unit`` added as tags.
        :type coreweave_cloud_logs: CoreWeaveCloudLogsIntegrationDataflowResponse, optional

        :param coreweave_cloud_metrics: Metrics from your CoreWeave organization: CoreWeave service metrics collected through its PromQL-compatible Prometheus endpoint, plus the ``coreweave.*`` namespaces from CoreWeave products such as Kubernetes, Database, Distributed File Storage, Inference, and Object Storage. Compute metrics ( ``coreweave.bare_metal`` , ``coreweave.gpu`` , ``coreweave.nccl`` , and ``coreweave.node`` ) are in Preview. Container metrics are not collected; install the Datadog Agent on your clusters for those.
        :type coreweave_cloud_metrics: CoreWeaveCloudMetricsIntegrationDataflowResponse, optional
        """
        if coreweave_cloud_logs is not unset:
            kwargs["coreweave_cloud_logs"] = coreweave_cloud_logs
        if coreweave_cloud_metrics is not unset:
            kwargs["coreweave_cloud_metrics"] = coreweave_cloud_metrics
        super().__init__(kwargs)
