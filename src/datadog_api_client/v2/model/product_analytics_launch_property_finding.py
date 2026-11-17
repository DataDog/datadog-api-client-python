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
    from datadog_api_client.v2.model.product_analytics_launch_code_status import ProductAnalyticsLaunchCodeStatus


class ProductAnalyticsLaunchPropertyFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_code_status import ProductAnalyticsLaunchCodeStatus

        return {
            "id": (str,),
            "status": (ProductAnalyticsLaunchCodeStatus,),
        }

    attribute_map = {
        "id": "id",
        "status": "status",
    }

    def __init__(self_, id: str, status: ProductAnalyticsLaunchCodeStatus, **kwargs):
        """
        Code analysis result for a property of an event.

        :param id: ID of the property in the tracking plan.
        :type id: str

        :param status: Whether the inspected code sends the event, or attaches the property to the event.
        :type status: ProductAnalyticsLaunchCodeStatus
        """
        super().__init__(kwargs)

        self_.id = id
        self_.status = status
