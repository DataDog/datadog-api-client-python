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
    from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType


class SecurityMonitoringDatasetCreateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_type import SecurityMonitoringDatasetType

        return {
            "id": (str,),
            "type": (SecurityMonitoringDatasetType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: SecurityMonitoringDatasetType, **kwargs):
        """
        The data wrapper of a dataset create response.

        :param id: The UUID of the newly created dataset.
        :type id: str

        :param type: The type of resource for a dataset response.
        :type type: SecurityMonitoringDatasetType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
