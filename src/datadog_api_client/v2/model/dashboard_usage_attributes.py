# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_usage_user import DashboardUsageUser


class DashboardUsageAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_usage_user import DashboardUsageUser

        return {
            "author": (DashboardUsageUser,),
            "created_at": (datetime, none_type),
            "dashboard_quality_score": (float, none_type),
            "edited_at": (datetime, none_type),
            "org_id": (int,),
            "teams": ([str], none_type),
            "title": (str,),
            "total_views": (int,),
            "total_views_by_type": ({str: (int,)}, none_type),
            "viewed_at": (datetime, none_type),
            "viewer": (DashboardUsageUser,),
            "widget_count": (int, none_type),
            "widget_count_by_type": ({str: (int,)}, none_type),
        }

    attribute_map = {
        "author": "author",
        "created_at": "created_at",
        "dashboard_quality_score": "dashboard_quality_score",
        "edited_at": "edited_at",
        "org_id": "org_id",
        "teams": "teams",
        "title": "title",
        "total_views": "total_views",
        "total_views_by_type": "total_views_by_type",
        "viewed_at": "viewed_at",
        "viewer": "viewer",
        "widget_count": "widget_count",
        "widget_count_by_type": "widget_count_by_type",
    }

    def __init__(
        self_,
        org_id: int,
        author: Union[DashboardUsageUser, none_type, UnsetType] = unset,
        created_at: Union[datetime, none_type, UnsetType] = unset,
        dashboard_quality_score: Union[float, none_type, UnsetType] = unset,
        edited_at: Union[datetime, none_type, UnsetType] = unset,
        teams: Union[List[str], none_type, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        total_views: Union[int, UnsetType] = unset,
        total_views_by_type: Union[Dict[str, int], none_type, UnsetType] = unset,
        viewed_at: Union[datetime, none_type, UnsetType] = unset,
        viewer: Union[DashboardUsageUser, none_type, UnsetType] = unset,
        widget_count: Union[int, none_type, UnsetType] = unset,
        widget_count_by_type: Union[Dict[str, int], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Usage statistics for a dashboard. The ``viewer`` field and all view-count fields ( ``total_views`` , ``viewed_at`` , ``total_views_by_type`` ) are populated only when Real User Monitoring (RUM) is active for the org.

        :param author: A user referenced from a dashboard usage record (author or viewer).
        :type author: DashboardUsageUser, none_type, optional

        :param created_at: When the dashboard was created.
        :type created_at: datetime, none_type, optional

        :param dashboard_quality_score: The dashboard quality score, or ``null`` when no score is available.
        :type dashboard_quality_score: float, none_type, optional

        :param edited_at: When the dashboard was most recently edited.
        :type edited_at: datetime, none_type, optional

        :param org_id: The Datadog organization that owns the dashboard.
        :type org_id: int

        :param teams: Teams the dashboard is tagged with.
        :type teams: [str], none_type, optional

        :param title: The dashboard title.
        :type title: str, optional

        :param total_views: Total view count for the dashboard. Counts only views captured by Real User Monitoring (RUM); ``0`` in orgs without RUM.
        :type total_views: int, optional

        :param total_views_by_type: View counts keyed by view type ( ``in_app`` , ``embed`` , ``public`` , ``shared`` , ``api`` , ``unknown`` ). Counts only views captured by Real User Monitoring (RUM); empty in orgs without RUM.
        :type total_views_by_type: {str: (int,)}, none_type, optional

        :param viewed_at: When the dashboard was most recently viewed. Populated only when Real User Monitoring (RUM) is active for the org; ``null`` in orgs without RUM.
        :type viewed_at: datetime, none_type, optional

        :param viewer: A user referenced from a dashboard usage record (author or viewer).
        :type viewer: DashboardUsageUser, none_type, optional

        :param widget_count: The total number of widgets on the dashboard.
        :type widget_count: int, none_type, optional

        :param widget_count_by_type: Widget counts keyed by widget type. The map includes group widgets and widgets without requests.
        :type widget_count_by_type: {str: (int,)}, none_type, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if dashboard_quality_score is not unset:
            kwargs["dashboard_quality_score"] = dashboard_quality_score
        if edited_at is not unset:
            kwargs["edited_at"] = edited_at
        if teams is not unset:
            kwargs["teams"] = teams
        if title is not unset:
            kwargs["title"] = title
        if total_views is not unset:
            kwargs["total_views"] = total_views
        if total_views_by_type is not unset:
            kwargs["total_views_by_type"] = total_views_by_type
        if viewed_at is not unset:
            kwargs["viewed_at"] = viewed_at
        if viewer is not unset:
            kwargs["viewer"] = viewer
        if widget_count is not unset:
            kwargs["widget_count"] = widget_count
        if widget_count_by_type is not unset:
            kwargs["widget_count_by_type"] = widget_count_by_type
        super().__init__(kwargs)

        self_.org_id = org_id
