# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_asset_dashboard_relationships import MetricAssetDashboardRelationships
    from datadog_api_client.v2.model.metric_asset_monitor_relationships import MetricAssetMonitorRelationships
    from datadog_api_client.v2.model.metric_asset_notebook_relationships import MetricAssetNotebookRelationships
    from datadog_api_client.v2.model.metric_asset_slo_relationships import MetricAssetSLORelationships


class MetricAssetResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_dashboard_relationships import MetricAssetDashboardRelationships
        from datadog_api_client.v2.model.metric_asset_monitor_relationships import MetricAssetMonitorRelationships
        from datadog_api_client.v2.model.metric_asset_notebook_relationships import MetricAssetNotebookRelationships
        from datadog_api_client.v2.model.metric_asset_slo_relationships import MetricAssetSLORelationships

        return {
            "dashboards": (MetricAssetDashboardRelationships,),
            "monitors": (MetricAssetMonitorRelationships,),
            "notebooks": (MetricAssetNotebookRelationships,),
            "slos": (MetricAssetSLORelationships,),
        }

    attribute_map = {
        "dashboards": "dashboards",
        "monitors": "monitors",
        "notebooks": "notebooks",
        "slos": "slos",
    }

    def __init__(
        self_,
        dashboards: Union[MetricAssetDashboardRelationships, UnsetType] = unset,
        monitors: Union[MetricAssetMonitorRelationships, UnsetType] = unset,
        notebooks: Union[MetricAssetNotebookRelationships, UnsetType] = unset,
        slos: Union[MetricAssetSLORelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships to assets related to the metric.

        :param dashboards: An object containing the list of dashboards that can be referenced in the ``included`` data.
        :type dashboards: MetricAssetDashboardRelationships, optional

        :param monitors: A object containing the list of monitors that can be referenced in the ``included`` data.
        :type monitors: MetricAssetMonitorRelationships, optional

        :param notebooks: An object containing the list of notebooks that can be referenced in the ``included`` data.
        :type notebooks: MetricAssetNotebookRelationships, optional

        :param slos: An object containing a list of SLOs that can be referenced in the ``included`` data.
        :type slos: MetricAssetSLORelationships, optional
        """
        if dashboards is not unset:
            kwargs["dashboards"] = dashboards
        if monitors is not unset:
            kwargs["monitors"] = monitors
        if notebooks is not unset:
            kwargs["notebooks"] = notebooks
        if slos is not unset:
            kwargs["slos"] = slos
        super().__init__(kwargs)
