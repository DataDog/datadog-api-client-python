# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_dependency_attributes_response import (
        SecurityMonitoringDatasetDependencyAttributesResponse,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_type import (
        SecurityMonitoringDatasetDependenciesType,
    )


class SecurityMonitoringDatasetDependencyDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_dependency_attributes_response import (
            SecurityMonitoringDatasetDependencyAttributesResponse,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_type import (
            SecurityMonitoringDatasetDependenciesType,
        )

        return {
            "attributes": (SecurityMonitoringDatasetDependencyAttributesResponse,),
            "id": (str,),
            "type": (SecurityMonitoringDatasetDependenciesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetDependencyAttributesResponse,
        id: str,
        type: SecurityMonitoringDatasetDependenciesType,
        **kwargs,
    ):
        """
        Dependencies for a dataset.

        :param attributes: Attributes for dataset dependency.
        :type attributes: SecurityMonitoringDatasetDependencyAttributesResponse

        :param id: The dataset ID.
        :type id: str

        :param type: The type of the response.
        :type type: SecurityMonitoringDatasetDependenciesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
