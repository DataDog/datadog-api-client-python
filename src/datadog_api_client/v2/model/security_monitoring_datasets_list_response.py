# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_data_response import (
        SecurityMonitoringDatasetDataResponse,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_list_meta import SecurityMonitoringDatasetListMeta


class SecurityMonitoringDatasetsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_data_response import (
            SecurityMonitoringDatasetDataResponse,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_list_meta import SecurityMonitoringDatasetListMeta

        return {
            "data": ([SecurityMonitoringDatasetDataResponse],),
            "meta": (SecurityMonitoringDatasetListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[SecurityMonitoringDatasetDataResponse], meta: SecurityMonitoringDatasetListMeta, **kwargs
    ):
        """
        Response containing a list of security monitoring datasets.

        :param data: Array of datasets.
        :type data: [SecurityMonitoringDatasetDataResponse]

        :param meta: Metadata for dataset list responses.
        :type meta: SecurityMonitoringDatasetListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
