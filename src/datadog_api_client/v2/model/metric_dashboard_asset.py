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
    from datadog_api_client.v2.model.metric_dashboard_attributes import MetricDashboardAttributes
    from datadog_api_client.v2.model.metric_dashboard_type import MetricDashboardType


class MetricDashboardAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_dashboard_attributes import MetricDashboardAttributes
        from datadog_api_client.v2.model.metric_dashboard_type import MetricDashboardType

        return {
            "attributes": (MetricDashboardAttributes,),
            "id": (str,),
            "type": (MetricDashboardType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: MetricDashboardType,
        attributes: Union[MetricDashboardAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A dashboard object with title and popularity.

        :param attributes: Attributes related to the dashboard, including title and popularity.
        :type attributes: MetricDashboardAttributes, optional

        :param id: The related dashboard's ID.
        :type id: str

        :param type: Dashboard resource type.
        :type type: MetricDashboardType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
