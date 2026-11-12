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
    from datadog_api_client.v1_20270101.model.dashboard_summary_definition import DashboardSummaryDefinition


class DashboardSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_summary_definition import DashboardSummaryDefinition

        return {
            "dashboards": ([DashboardSummaryDefinition],),
            "total": (int,),
        }

    attribute_map = {
        "dashboards": "dashboards",
        "total": "total",
    }
    read_only_vars = {
        "total",
    }

    def __init__(
        self_,
        dashboards: Union[List[DashboardSummaryDefinition], UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dashboard summary response.

        :param dashboards: List of dashboard definitions.
        :type dashboards: [DashboardSummaryDefinition], optional

        :param total: Number of dashboards.
        :type total: int, optional
        """
        if dashboards is not unset:
            kwargs["dashboards"] = dashboards
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
