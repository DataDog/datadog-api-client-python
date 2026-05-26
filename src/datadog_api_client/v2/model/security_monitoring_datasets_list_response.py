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
    from datadog_api_client.v2.model.security_monitoring_dataset_data import SecurityMonitoringDatasetData
    from datadog_api_client.v2.model.security_monitoring_datasets_list_meta import SecurityMonitoringDatasetsListMeta


class SecurityMonitoringDatasetsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_data import SecurityMonitoringDatasetData
        from datadog_api_client.v2.model.security_monitoring_datasets_list_meta import (
            SecurityMonitoringDatasetsListMeta,
        )

        return {
            "data": ([SecurityMonitoringDatasetData],),
            "meta": (SecurityMonitoringDatasetsListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[SecurityMonitoringDatasetData], meta: SecurityMonitoringDatasetsListMeta, **kwargs):
        """
        Response containing a paginated list of Cloud SIEM datasets.

        :param data: A list of dataset data items.
        :type data: [SecurityMonitoringDatasetData]

        :param meta: Metadata returned with a list of datasets.
        :type meta: SecurityMonitoringDatasetsListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
