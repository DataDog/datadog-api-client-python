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
    from datadog_api_client.v2.model.security_monitoring_dataset_data_response import (
        SecurityMonitoringDatasetDataResponse,
    )


class SecurityMonitoringDatasetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_data_response import (
            SecurityMonitoringDatasetDataResponse,
        )

        return {
            "data": (SecurityMonitoringDatasetDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringDatasetDataResponse, **kwargs):
        """
        Response containing a security monitoring dataset.

        :param data: A security monitoring dataset.
        :type data: SecurityMonitoringDatasetDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
