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
    from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_attributes_request import (
        SecurityMonitoringDatasetDependenciesAttributesRequest,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_type import (
        SecurityMonitoringDatasetDependenciesType,
    )


class SecurityMonitoringDatasetDependenciesDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_attributes_request import (
            SecurityMonitoringDatasetDependenciesAttributesRequest,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_type import (
            SecurityMonitoringDatasetDependenciesType,
        )

        return {
            "attributes": (SecurityMonitoringDatasetDependenciesAttributesRequest,),
            "type": (SecurityMonitoringDatasetDependenciesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetDependenciesAttributesRequest,
        type: SecurityMonitoringDatasetDependenciesType,
        **kwargs,
    ):
        """
        Data for dataset dependencies request.

        :param attributes: Attributes for dataset dependencies request.
        :type attributes: SecurityMonitoringDatasetDependenciesAttributesRequest

        :param type: The type of the response.
        :type type: SecurityMonitoringDatasetDependenciesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
