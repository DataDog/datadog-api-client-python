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
    from datadog_api_client.v2.model.security_monitoring_dataset_update_data_request import (
        SecurityMonitoringDatasetUpdateDataRequest,
    )


class SecurityMonitoringDatasetUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_update_data_request import (
            SecurityMonitoringDatasetUpdateDataRequest,
        )

        return {
            "data": (SecurityMonitoringDatasetUpdateDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringDatasetUpdateDataRequest, **kwargs):
        """
        Request to update a security monitoring dataset.

        :param data: Data for updating a security monitoring dataset.
        :type data: SecurityMonitoringDatasetUpdateDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
