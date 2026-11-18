# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_launch_event_finding import ProductAnalyticsLaunchEventFinding


class ProductAnalyticsLaunchCodeAnalysis(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_event_finding import (
            ProductAnalyticsLaunchEventFinding,
        )

        return {
            "analyzed_at": (datetime,),
            "events": ([ProductAnalyticsLaunchEventFinding],),
            "revision": (str,),
        }

    attribute_map = {
        "analyzed_at": "analyzed_at",
        "events": "events",
        "revision": "revision",
    }
    read_only_vars = {
        "analyzed_at",
    }

    def __init__(
        self_,
        analyzed_at: Union[datetime, UnsetType] = unset,
        events: Union[List[ProductAnalyticsLaunchEventFinding], UnsetType] = unset,
        revision: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Latest inspection of the repository for the tracking plan instrumentation. A new analysis replaces the stored
        one.
        Events and properties that it does not list are not verified.

        :param analyzed_at: Time of the analysis. Set by the server.
        :type analyzed_at: datetime, optional

        :param events: Results for the events of the tracking plan. List each event once.
        :type events: [ProductAnalyticsLaunchEventFinding], optional

        :param revision: Code revision that was inspected, such as a commit SHA.
        :type revision: str, optional
        """
        if analyzed_at is not unset:
            kwargs["analyzed_at"] = analyzed_at
        if events is not unset:
            kwargs["events"] = events
        if revision is not unset:
            kwargs["revision"] = revision
        super().__init__(kwargs)
