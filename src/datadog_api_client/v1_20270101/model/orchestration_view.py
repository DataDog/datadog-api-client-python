# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrchestrationView(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["service", "cluster", "job", "node", "deployment", "namespace", "pod", "genericWorkload", "inferenceWorkload", "replicaSet", "cronJob", "daemonSet", "statefulSet", "persistentVolume", "persistentVolumeClaim", "role", "roleBinding", "clusterRole", "clusterRoleBinding", "serviceAccount", "ingress", "configMap", "verticalPodAutoscaler", "horizontalPodAutoscaler", "crd", "cr", "networkPolicy", "podDisruptionBudget", "ecsTask", "ecsTaskDefinition", "ecsDaemonTaskDefinition", "ecsService", "ecsDaemon", "ecsCluster", "ecsContainerInstance"].
    :type value: str
    """

    allowed_values = {
        "service",
        "cluster",
        "job",
        "node",
        "deployment",
        "namespace",
        "pod",
        "genericWorkload",
        "inferenceWorkload",
        "replicaSet",
        "cronJob",
        "daemonSet",
        "statefulSet",
        "persistentVolume",
        "persistentVolumeClaim",
        "role",
        "roleBinding",
        "clusterRole",
        "clusterRoleBinding",
        "serviceAccount",
        "ingress",
        "configMap",
        "verticalPodAutoscaler",
        "horizontalPodAutoscaler",
        "crd",
        "cr",
        "networkPolicy",
        "podDisruptionBudget",
        "ecsTask",
        "ecsTaskDefinition",
        "ecsDaemonTaskDefinition",
        "ecsService",
        "ecsDaemon",
        "ecsCluster",
        "ecsContainerInstance",
    }
    SERVICE: ClassVar["OrchestrationView"]
    CLUSTER: ClassVar["OrchestrationView"]
    JOB: ClassVar["OrchestrationView"]
    NODE: ClassVar["OrchestrationView"]
    DEPLOYMENT: ClassVar["OrchestrationView"]
    NAMESPACE: ClassVar["OrchestrationView"]
    POD: ClassVar["OrchestrationView"]
    GENERICWORKLOAD: ClassVar["OrchestrationView"]
    INFERENCEWORKLOAD: ClassVar["OrchestrationView"]
    REPLICASET: ClassVar["OrchestrationView"]
    CRONJOB: ClassVar["OrchestrationView"]
    DAEMONSET: ClassVar["OrchestrationView"]
    STATEFULSET: ClassVar["OrchestrationView"]
    PERSISTENTVOLUME: ClassVar["OrchestrationView"]
    PERSISTENTVOLUMECLAIM: ClassVar["OrchestrationView"]
    ROLE: ClassVar["OrchestrationView"]
    ROLEBINDING: ClassVar["OrchestrationView"]
    CLUSTERROLE: ClassVar["OrchestrationView"]
    CLUSTERROLEBINDING: ClassVar["OrchestrationView"]
    SERVICEACCOUNT: ClassVar["OrchestrationView"]
    INGRESS: ClassVar["OrchestrationView"]
    CONFIGMAP: ClassVar["OrchestrationView"]
    VERTICALPODAUTOSCALER: ClassVar["OrchestrationView"]
    HORIZONTALPODAUTOSCALER: ClassVar["OrchestrationView"]
    CRD: ClassVar["OrchestrationView"]
    CR: ClassVar["OrchestrationView"]
    NETWORKPOLICY: ClassVar["OrchestrationView"]
    PODDISRUPTIONBUDGET: ClassVar["OrchestrationView"]
    ECSTASK: ClassVar["OrchestrationView"]
    ECSTASKDEFINITION: ClassVar["OrchestrationView"]
    ECSDAEMONTASKDEFINITION: ClassVar["OrchestrationView"]
    ECSSERVICE: ClassVar["OrchestrationView"]
    ECSDAEMON: ClassVar["OrchestrationView"]
    ECSCLUSTER: ClassVar["OrchestrationView"]
    ECSCONTAINERINSTANCE: ClassVar["OrchestrationView"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrchestrationView.SERVICE = OrchestrationView("service")
OrchestrationView.CLUSTER = OrchestrationView("cluster")
OrchestrationView.JOB = OrchestrationView("job")
OrchestrationView.NODE = OrchestrationView("node")
OrchestrationView.DEPLOYMENT = OrchestrationView("deployment")
OrchestrationView.NAMESPACE = OrchestrationView("namespace")
OrchestrationView.POD = OrchestrationView("pod")
OrchestrationView.GENERICWORKLOAD = OrchestrationView("genericWorkload")
OrchestrationView.INFERENCEWORKLOAD = OrchestrationView("inferenceWorkload")
OrchestrationView.REPLICASET = OrchestrationView("replicaSet")
OrchestrationView.CRONJOB = OrchestrationView("cronJob")
OrchestrationView.DAEMONSET = OrchestrationView("daemonSet")
OrchestrationView.STATEFULSET = OrchestrationView("statefulSet")
OrchestrationView.PERSISTENTVOLUME = OrchestrationView("persistentVolume")
OrchestrationView.PERSISTENTVOLUMECLAIM = OrchestrationView("persistentVolumeClaim")
OrchestrationView.ROLE = OrchestrationView("role")
OrchestrationView.ROLEBINDING = OrchestrationView("roleBinding")
OrchestrationView.CLUSTERROLE = OrchestrationView("clusterRole")
OrchestrationView.CLUSTERROLEBINDING = OrchestrationView("clusterRoleBinding")
OrchestrationView.SERVICEACCOUNT = OrchestrationView("serviceAccount")
OrchestrationView.INGRESS = OrchestrationView("ingress")
OrchestrationView.CONFIGMAP = OrchestrationView("configMap")
OrchestrationView.VERTICALPODAUTOSCALER = OrchestrationView("verticalPodAutoscaler")
OrchestrationView.HORIZONTALPODAUTOSCALER = OrchestrationView("horizontalPodAutoscaler")
OrchestrationView.CRD = OrchestrationView("crd")
OrchestrationView.CR = OrchestrationView("cr")
OrchestrationView.NETWORKPOLICY = OrchestrationView("networkPolicy")
OrchestrationView.PODDISRUPTIONBUDGET = OrchestrationView("podDisruptionBudget")
OrchestrationView.ECSTASK = OrchestrationView("ecsTask")
OrchestrationView.ECSTASKDEFINITION = OrchestrationView("ecsTaskDefinition")
OrchestrationView.ECSDAEMONTASKDEFINITION = OrchestrationView("ecsDaemonTaskDefinition")
OrchestrationView.ECSSERVICE = OrchestrationView("ecsService")
OrchestrationView.ECSDAEMON = OrchestrationView("ecsDaemon")
OrchestrationView.ECSCLUSTER = OrchestrationView("ecsCluster")
OrchestrationView.ECSCONTAINERINSTANCE = OrchestrationView("ecsContainerInstance")
