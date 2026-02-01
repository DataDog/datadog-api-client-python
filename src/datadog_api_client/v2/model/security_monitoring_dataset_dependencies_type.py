# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetDependenciesType(ModelSimple):
    """
    The type of the response.

    :param value: If omitted defaults to "security_monitoring_dataset_dependencies". Must be one of ["security_monitoring_dataset_dependencies"].
    :type value: str
    """

    allowed_values = {
        "security_monitoring_dataset_dependencies",
    }
    SECURITY_MONITORING_DATASET_DEPENDENCIES: ClassVar["SecurityMonitoringDatasetDependenciesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetDependenciesType.SECURITY_MONITORING_DATASET_DEPENDENCIES = (
    SecurityMonitoringDatasetDependenciesType("security_monitoring_dataset_dependencies")
)
