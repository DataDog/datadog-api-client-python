# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetDependentsType(ModelSimple):
    """
    The type of resource for a dataset dependents entry.

    :param value: If omitted defaults to "datasetDependents". Must be one of ["datasetDependents"].
    :type value: str
    """

    allowed_values = {
        "datasetDependents",
    }
    DATASET_DEPENDENTS: ClassVar["SecurityMonitoringDatasetDependentsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetDependentsType.DATASET_DEPENDENTS = SecurityMonitoringDatasetDependentsType(
    "datasetDependents"
)
