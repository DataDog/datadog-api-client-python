# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CoreWeaveCloudLogsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Service logs for CoreWeave-managed components in each CoreWeave region: the CKS control plane (such as ``kube-apiserver`` and ``etcd`` ), CoreWeave add-on services in the ``cw-*`` and ``kube-system`` namespaces, SUNK, and node system logs such as ``kubelet`` and ``containerd``. Logs from your own workloads and Kubernetes audit logs are not collected. Logs are sent with ``source:coreweave`` , with CoreWeave log labels such as ``namespace`` , ``app`` , and ``systemd_unit`` added as tags.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
