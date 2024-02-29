# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_asset_response_data import MetricAssetResponseData
    from datadog_api_client.v2.model.metric_asset_response_included import MetricAssetResponseIncluded
    from datadog_api_client.v2.model.metric_dashboard_asset import MetricDashboardAsset
    from datadog_api_client.v2.model.metric_monitor_asset import MetricMonitorAsset
    from datadog_api_client.v2.model.metric_notebook_asset import MetricNotebookAsset
    from datadog_api_client.v2.model.metric_slo_asset import MetricSLOAsset


class MetricAssetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_response_data import MetricAssetResponseData
        from datadog_api_client.v2.model.metric_asset_response_included import MetricAssetResponseIncluded

        return {
            "data": (MetricAssetResponseData,),
            "included": ([MetricAssetResponseIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[MetricAssetResponseData, UnsetType] = unset,
        included: Union[
            List[
                Union[
                    MetricAssetResponseIncluded,
                    MetricDashboardAsset,
                    MetricMonitorAsset,
                    MetricNotebookAsset,
                    MetricSLOAsset,
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Response object that includes related dashboards, monitors, notebooks, and SLOs.

        :param data: Metric assets response data.
        :type data: MetricAssetResponseData, optional

        :param included: Array of objects related to the metric assets.
        :type included: [MetricAssetResponseIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
