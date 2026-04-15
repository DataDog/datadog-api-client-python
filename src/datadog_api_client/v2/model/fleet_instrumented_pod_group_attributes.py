# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class FleetInstrumentedPodGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "applied_target": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "applied_target_name": (str,),
            "injected_tags": ([str],),
            "kube_ownerref_kind": (str,),
            "kube_ownerref_name": (str,),
            "lib_injection_annotations": ([str],),
            "namespace": (str,),
            "pod_count": (int,),
            "pod_names": ([str],),
            "tags": ({str: (str,)},),
        }

    attribute_map = {
        "applied_target": "applied_target",
        "applied_target_name": "applied_target_name",
        "injected_tags": "injected_tags",
        "kube_ownerref_kind": "kube_ownerref_kind",
        "kube_ownerref_name": "kube_ownerref_name",
        "lib_injection_annotations": "lib_injection_annotations",
        "namespace": "namespace",
        "pod_count": "pod_count",
        "pod_names": "pod_names",
        "tags": "tags",
    }

    def __init__(
        self_,
        applied_target: Union[Dict[str, Any], UnsetType] = unset,
        applied_target_name: Union[str, UnsetType] = unset,
        injected_tags: Union[List[str], UnsetType] = unset,
        kube_ownerref_kind: Union[str, UnsetType] = unset,
        kube_ownerref_name: Union[str, UnsetType] = unset,
        lib_injection_annotations: Union[List[str], UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        pod_count: Union[int, UnsetType] = unset,
        pod_names: Union[List[str], UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a group of instrumented pods targeted for SSI injection.

        :param applied_target: The SSI injection target configuration applied to the pod group.
        :type applied_target: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param applied_target_name: The name of the applied SSI injection target.
        :type applied_target_name: str, optional

        :param injected_tags: Tags injected into the pods by the Admission Controller.
        :type injected_tags: [str], optional

        :param kube_ownerref_kind: The kind of the Kubernetes owner reference.
        :type kube_ownerref_kind: str, optional

        :param kube_ownerref_name: The name of the Kubernetes owner reference (deployment, statefulset, etc.).
        :type kube_ownerref_name: str, optional

        :param lib_injection_annotations: Library injection annotations on the pod group.
        :type lib_injection_annotations: [str], optional

        :param namespace: The Kubernetes namespace of the pod group.
        :type namespace: str, optional

        :param pod_count: Total number of pods in the group.
        :type pod_count: int, optional

        :param pod_names: Names of the individual pods in the group.
        :type pod_names: [str], optional

        :param tags: Additional tags associated with the pod group.
        :type tags: {str: (str,)}, optional
        """
        if applied_target is not unset:
            kwargs["applied_target"] = applied_target
        if applied_target_name is not unset:
            kwargs["applied_target_name"] = applied_target_name
        if injected_tags is not unset:
            kwargs["injected_tags"] = injected_tags
        if kube_ownerref_kind is not unset:
            kwargs["kube_ownerref_kind"] = kube_ownerref_kind
        if kube_ownerref_name is not unset:
            kwargs["kube_ownerref_name"] = kube_ownerref_name
        if lib_injection_annotations is not unset:
            kwargs["lib_injection_annotations"] = lib_injection_annotations
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if pod_count is not unset:
            kwargs["pod_count"] = pod_count
        if pod_names is not unset:
            kwargs["pod_names"] = pod_names
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
