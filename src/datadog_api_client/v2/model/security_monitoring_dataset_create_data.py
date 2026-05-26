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
    from datadog_api_client.v2.model.security_monitoring_dataset_attributes_request import (
        SecurityMonitoringDatasetAttributesRequest,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_create_type import SecurityMonitoringDatasetCreateType


class SecurityMonitoringDatasetCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_attributes_request import (
            SecurityMonitoringDatasetAttributesRequest,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_create_type import (
            SecurityMonitoringDatasetCreateType,
        )

        return {
            "attributes": (SecurityMonitoringDatasetAttributesRequest,),
            "type": (SecurityMonitoringDatasetCreateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetAttributesRequest,
        type: SecurityMonitoringDatasetCreateType,
        **kwargs,
    ):
        """
        The data wrapper of a dataset create request.

        :param attributes: The attributes of a dataset create or update request.
        :type attributes: SecurityMonitoringDatasetAttributesRequest

        :param type: The type of resource for a dataset create request.
        :type type: SecurityMonitoringDatasetCreateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
