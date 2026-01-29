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
    from datadog_api_client.v2.model.security_monitoring_dataset_create_attributes_request import (
        SecurityMonitoringDatasetCreateAttributesRequest,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType


class SecurityMonitoringDatasetCreateDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_create_attributes_request import (
            SecurityMonitoringDatasetCreateAttributesRequest,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType

        return {
            "attributes": (SecurityMonitoringDatasetCreateAttributesRequest,),
            "type": (SecurityMonitoringDatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetCreateAttributesRequest,
        type: SecurityMonitoringDatasetType,
        **kwargs,
    ):
        """
        Data for creating a security monitoring dataset.

        :param attributes: Attributes for creating a security monitoring dataset.
        :type attributes: SecurityMonitoringDatasetCreateAttributesRequest

        :param type: Type for security monitoring dataset objects.
        :type type: SecurityMonitoringDatasetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
