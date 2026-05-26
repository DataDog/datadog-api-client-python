# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetUpdateType(ModelSimple):
    """
    The type of resource for a dataset update request.

    :param value: If omitted defaults to "datasetUpdate". Must be one of ["datasetUpdate"].
    :type value: str
    """

    allowed_values = {
        "datasetUpdate",
    }
    DATASET_UPDATE: ClassVar["SecurityMonitoringDatasetUpdateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetUpdateType.DATASET_UPDATE = SecurityMonitoringDatasetUpdateType("datasetUpdate")
