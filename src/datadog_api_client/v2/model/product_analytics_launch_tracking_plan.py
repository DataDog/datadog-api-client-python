# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_launch_code_analysis import ProductAnalyticsLaunchCodeAnalysis
    from datadog_api_client.v2.model.product_analytics_launch_event import ProductAnalyticsLaunchEvent
    from datadog_api_client.v2.model.product_analytics_launch_properties import ProductAnalyticsLaunchProperties


class ProductAnalyticsLaunchTrackingPlan(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_code_analysis import (
            ProductAnalyticsLaunchCodeAnalysis,
        )
        from datadog_api_client.v2.model.product_analytics_launch_event import ProductAnalyticsLaunchEvent
        from datadog_api_client.v2.model.product_analytics_launch_properties import ProductAnalyticsLaunchProperties

        return {
            "code_analysis": (ProductAnalyticsLaunchCodeAnalysis,),
            "codegen_session_id": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "events": ([ProductAnalyticsLaunchEvent],),
            "id": (str,),
            "jira_ticket_id": (str,),
            "pr_link": (str,),
            "properties": (ProductAnalyticsLaunchProperties,),
            "updated_at": (datetime, none_type),
            "updated_by": (str, none_type),
        }

    attribute_map = {
        "code_analysis": "code_analysis",
        "codegen_session_id": "codegen_session_id",
        "created_at": "created_at",
        "created_by": "created_by",
        "events": "events",
        "id": "id",
        "jira_ticket_id": "jira_ticket_id",
        "pr_link": "pr_link",
        "properties": "properties",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        id: str,
        code_analysis: Union[ProductAnalyticsLaunchCodeAnalysis, UnsetType] = unset,
        codegen_session_id: Union[str, UnsetType] = unset,
        events: Union[List[ProductAnalyticsLaunchEvent], UnsetType] = unset,
        jira_ticket_id: Union[str, UnsetType] = unset,
        pr_link: Union[str, UnsetType] = unset,
        properties: Union[ProductAnalyticsLaunchProperties, UnsetType] = unset,
        updated_at: Union[datetime, none_type, UnsetType] = unset,
        updated_by: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Tracking plan of a launch, listing the events and properties to instrument.

        :param code_analysis: Latest inspection of the repository for the tracking plan instrumentation. A new analysis replaces the stored
            one.
            Events and properties that it does not list are not verified.
        :type code_analysis: ProductAnalyticsLaunchCodeAnalysis, optional

        :param codegen_session_id: ID of the code generation session that implemented the plan.
        :type codegen_session_id: str, optional

        :param created_at: Time the tracking plan was created.
        :type created_at: datetime

        :param created_by: UUID of the user who created the tracking plan.
        :type created_by: str

        :param events: Events to instrument.
        :type events: [ProductAnalyticsLaunchEvent], optional

        :param id: ID of the tracking plan.
        :type id: str

        :param jira_ticket_id: ID of the Jira ticket that tracks the instrumentation work.
        :type jira_ticket_id: str, optional

        :param pr_link: Link to the pull request that implements the plan.
        :type pr_link: str, optional

        :param properties: Event properties of the tracking plan, keyed by property ID.
        :type properties: ProductAnalyticsLaunchProperties, optional

        :param updated_at: Time the tracking plan was last updated.
        :type updated_at: datetime, none_type, optional

        :param updated_by: UUID of the user who last updated the tracking plan.
        :type updated_by: str, none_type, optional
        """
        if code_analysis is not unset:
            kwargs["code_analysis"] = code_analysis
        if codegen_session_id is not unset:
            kwargs["codegen_session_id"] = codegen_session_id
        if events is not unset:
            kwargs["events"] = events
        if jira_ticket_id is not unset:
            kwargs["jira_ticket_id"] = jira_ticket_id
        if pr_link is not unset:
            kwargs["pr_link"] = pr_link
        if properties is not unset:
            kwargs["properties"] = properties
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.id = id
