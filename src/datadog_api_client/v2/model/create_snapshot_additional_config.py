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
    from datadog_api_client.v2.model.create_snapshot_template_variable import CreateSnapshotTemplateVariable
    from datadog_api_client.v2.model.create_snapshot_timeseries_legend_type import CreateSnapshotTimeseriesLegendType


class CreateSnapshotAdditionalConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_snapshot_template_variable import CreateSnapshotTemplateVariable
        from datadog_api_client.v2.model.create_snapshot_timeseries_legend_type import (
            CreateSnapshotTimeseriesLegendType,
        )

        return {
            "template_variables": ([CreateSnapshotTemplateVariable],),
            "timeseries_legend_type": (CreateSnapshotTimeseriesLegendType,),
            "timezone_offset_minutes": (int,),
        }

    attribute_map = {
        "template_variables": "template_variables",
        "timeseries_legend_type": "timeseries_legend_type",
        "timezone_offset_minutes": "timezone_offset_minutes",
    }

    def __init__(
        self_,
        template_variables: Union[List[CreateSnapshotTemplateVariable], UnsetType] = unset,
        timeseries_legend_type: Union[CreateSnapshotTimeseriesLegendType, UnsetType] = unset,
        timezone_offset_minutes: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional configuration options for snapshot creation.

        :param template_variables: List of template variable definitions for snapshot rendering.
        :type template_variables: [CreateSnapshotTemplateVariable], optional

        :param timeseries_legend_type: The legend display type for timeseries widgets. A value of ``none`` hides the legend entirely; omitting the field lets the frontend choose automatically.
        :type timeseries_legend_type: CreateSnapshotTimeseriesLegendType, optional

        :param timezone_offset_minutes: Timezone offset in minutes from UTC. Positive values are west of UTC (for example, ``300`` for UTC-5). Use ``0`` for UTC.
        :type timezone_offset_minutes: int, optional
        """
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if timeseries_legend_type is not unset:
            kwargs["timeseries_legend_type"] = timeseries_legend_type
        if timezone_offset_minutes is not unset:
            kwargs["timezone_offset_minutes"] = timezone_offset_minutes
        super().__init__(kwargs)
