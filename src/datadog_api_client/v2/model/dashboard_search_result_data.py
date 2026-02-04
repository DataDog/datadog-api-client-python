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
    from datadog_api_client.v2.model.dashboard_search_attributes import DashboardSearchAttributes
    from datadog_api_client.v2.model.dashboard_search_metadata import DashboardSearchMetadata
    from datadog_api_client.v2.model.metric_dashboard_type import MetricDashboardType


class DashboardSearchResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_search_attributes import DashboardSearchAttributes
        from datadog_api_client.v2.model.dashboard_search_metadata import DashboardSearchMetadata
        from datadog_api_client.v2.model.metric_dashboard_type import MetricDashboardType

        return {
            "attributes": (DashboardSearchAttributes,),
            "id": (str,),
            "meta": (DashboardSearchMetadata,),
            "type": (MetricDashboardType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DashboardSearchAttributes,
        id: str,
        meta: DashboardSearchMetadata,
        type: MetricDashboardType,
        **kwargs,
    ):
        """
        A dashboard search result.

        :param attributes: Dashboard search result attributes.
        :type attributes: DashboardSearchAttributes

        :param id: Dashboard identifier.
        :type id: str

        :param meta: Metadata about the dashboard.
        :type meta: DashboardSearchMetadata

        :param type: Dashboard resource type.
        :type type: MetricDashboardType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.meta = meta
        self_.type = type
