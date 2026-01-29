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
    from datadog_api_client.v2.model.security_monitoring_dataset_attributes_response import (
        SecurityMonitoringDatasetAttributesResponse,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType


class SecurityMonitoringDatasetDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_attributes_response import (
            SecurityMonitoringDatasetAttributesResponse,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType

        return {
            "attributes": (SecurityMonitoringDatasetAttributesResponse,),
            "id": (str,),
            "type": (SecurityMonitoringDatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetAttributesResponse,
        id: str,
        type: SecurityMonitoringDatasetType,
        **kwargs,
    ):
        """
        A security monitoring dataset.

        :param attributes: Attributes of a security monitoring dataset.
        :type attributes: SecurityMonitoringDatasetAttributesResponse

        :param id: The unique identifier of the dataset.
        :type id: str

        :param type: Type for security monitoring dataset objects.
        :type type: SecurityMonitoringDatasetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
