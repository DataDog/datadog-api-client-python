# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetType(ModelSimple):
    """
    Type for security monitoring dataset objects.

    :param value: If omitted defaults to "security_monitoring_dataset". Must be one of ["security_monitoring_dataset"].
    :type value: str
    """

    allowed_values = {
        "security_monitoring_dataset",
    }
    SECURITY_MONITORING_DATASET: ClassVar["SecurityMonitoringDatasetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetType.SECURITY_MONITORING_DATASET = SecurityMonitoringDatasetType("security_monitoring_dataset")
