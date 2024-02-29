# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class MetricAssetResponseIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        List of included assets with full set of attributes.

        :param attributes: Attributes related to the dashboard, including title and popularity.
        :type attributes: MetricDashboardAttributes, optional

        :param id: The related dashboard's ID.
        :type id: str

        :param type: Dashboard resource type.
        :type type: MetricDashboardType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.metric_dashboard_asset import MetricDashboardAsset
        from datadog_api_client.v2.model.metric_monitor_asset import MetricMonitorAsset
        from datadog_api_client.v2.model.metric_notebook_asset import MetricNotebookAsset
        from datadog_api_client.v2.model.metric_slo_asset import MetricSLOAsset

        return {
            "oneOf": [
                MetricDashboardAsset,
                MetricMonitorAsset,
                MetricNotebookAsset,
                MetricSLOAsset,
            ],
        }
