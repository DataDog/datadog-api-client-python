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
    from datadog_api_client.v1.model.dashboard_summary_definition_20270101 import DashboardSummaryDefinition_20270101


class DashboardSummary_20270101(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_summary_definition_20270101 import (
            DashboardSummaryDefinition_20270101,
        )

        return {
            "dashboards": ([DashboardSummaryDefinition_20270101],),
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
        dashboards: Union[List[DashboardSummaryDefinition_20270101], UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dashboard summary response.

        :param dashboards: List of dashboard definitions.
        :type dashboards: [DashboardSummaryDefinition_20270101], optional

        :param total: Number of dashboards.
        :type total: int, optional
        """
        if dashboards is not unset:
            kwargs["dashboards"] = dashboards
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
