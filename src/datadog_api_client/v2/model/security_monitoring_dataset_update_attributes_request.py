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
    from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition


class SecurityMonitoringDatasetUpdateAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition import (
            SecurityMonitoringDatasetDefinition,
        )

        return {
            "definition": (SecurityMonitoringDatasetDefinition,),
            "description": (str,),
            "version": (int,),
        }

    attribute_map = {
        "definition": "definition",
        "description": "description",
        "version": "version",
    }

    def __init__(
        self_,
        definition: SecurityMonitoringDatasetDefinition,
        description: str,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a security monitoring dataset.

        :param definition: The definition of a dataset, including its data source, name, indexes, and columns.
        :type definition: SecurityMonitoringDatasetDefinition

        :param description: A description of the dataset (maximum 255 characters).
        :type description: str

        :param version: The expected version of the dataset for concurrent modification detection.
        :type version: int, optional
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.definition = definition
        self_.description = description
