# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPMonitoredResourceConfigType(ModelSimple):
    """
    The GCP monitored resource type. Only a subset of resource types are supported.

    :param value: Must be one of ["cloud_function", "cloud_run_revision", "gce_instance"].
    :type value: str
    """

    allowed_values = {
        "cloud_function",
        "cloud_run_revision",
        "gce_instance",
    }
    CLOUD_FUNCTION: ClassVar["GCPMonitoredResourceConfigType"]
    CLOUD_RUN_REVISION: ClassVar["GCPMonitoredResourceConfigType"]
    GCE_INSTANCE: ClassVar["GCPMonitoredResourceConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPMonitoredResourceConfigType.CLOUD_FUNCTION = GCPMonitoredResourceConfigType("cloud_function")
GCPMonitoredResourceConfigType.CLOUD_RUN_REVISION = GCPMonitoredResourceConfigType("cloud_run_revision")
GCPMonitoredResourceConfigType.GCE_INSTANCE = GCPMonitoredResourceConfigType("gce_instance")
