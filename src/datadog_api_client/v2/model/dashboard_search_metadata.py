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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_search_user import DashboardSearchUser


class DashboardSearchMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_search_user import DashboardSearchUser

        return {
            "author": (DashboardSearchUser,),
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "embeddable_domains": ([str], none_type),
            "experience_type": (str,),
            "expiration": (datetime, none_type),
            "has_monitors": (bool, none_type),
            "is_favorited": (bool,),
            "is_public_dashboard_ownerless": (bool,),
            "is_shared": (bool,),
            "last_accessed": (datetime, none_type),
            "modified_at": (datetime,),
            "popularity": (float,),
            "public_title": (str,),
            "quality_score": (float, none_type),
            "share_list": ([str], none_type),
            "share_type": (str,),
            "shared_by": (DashboardSearchUser,),
            "status": (str,),
            "token": (str,),
            "type": (str,),
            "url": (str,),
            "widget_count": (int,),
        }

    attribute_map = {
        "author": "author",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "embeddable_domains": "embeddable_domains",
        "experience_type": "experience_type",
        "expiration": "expiration",
        "has_monitors": "has_monitors",
        "is_favorited": "is_favorited",
        "is_public_dashboard_ownerless": "is_public_dashboard_ownerless",
        "is_shared": "is_shared",
        "last_accessed": "last_accessed",
        "modified_at": "modified_at",
        "popularity": "popularity",
        "public_title": "public_title",
        "quality_score": "quality_score",
        "share_list": "share_list",
        "share_type": "share_type",
        "shared_by": "shared_by",
        "status": "status",
        "token": "token",
        "type": "type",
        "url": "url",
        "widget_count": "widget_count",
    }

    def __init__(
        self_,
        author: DashboardSearchUser,
        created_at: datetime,
        deleted_at: Union[datetime, none_type],
        embeddable_domains: Union[List[str], none_type],
        experience_type: str,
        expiration: Union[datetime, none_type],
        has_monitors: Union[bool, none_type],
        is_favorited: bool,
        is_public_dashboard_ownerless: bool,
        is_shared: bool,
        last_accessed: Union[datetime, none_type],
        modified_at: datetime,
        popularity: float,
        public_title: str,
        quality_score: Union[float, none_type],
        share_list: Union[List[str], none_type],
        share_type: str,
        shared_by: DashboardSearchUser,
        status: str,
        token: str,
        type: str,
        url: str,
        widget_count: int,
        **kwargs,
    ):
        """
        Metadata about the dashboard.

        :param author: User information.
        :type author: DashboardSearchUser

        :param created_at: Time at which the dashboard was created.
        :type created_at: datetime

        :param deleted_at: Time at which the dashboard was deleted, or null if not deleted.
        :type deleted_at: datetime, none_type

        :param embeddable_domains: List of domains the dashboard is allowed to be embedded in.
        :type embeddable_domains: [str], none_type

        :param experience_type: Dashboard experience type.
        :type experience_type: str

        :param expiration: When the public dashboard link will expire.
        :type expiration: datetime, none_type

        :param has_monitors: Whether the dashboard has monitors.
        :type has_monitors: bool, none_type

        :param is_favorited: Whether the dashboard is favorited by the user.
        :type is_favorited: bool

        :param is_public_dashboard_ownerless: Whether the public dashboard owner is deactivated.
        :type is_public_dashboard_ownerless: bool

        :param is_shared: Whether the dashboard is shared publicly.
        :type is_shared: bool

        :param last_accessed: Last time the dashboard was accessed.
        :type last_accessed: datetime, none_type

        :param modified_at: Time at which the dashboard was last updated.
        :type modified_at: datetime

        :param popularity: Relative measure of dashboard popularity.
        :type popularity: float

        :param public_title: Published title of the public dashboard.
        :type public_title: str

        :param quality_score: Quality score of the dashboard.
        :type quality_score: float, none_type

        :param share_list: List of email addresses for invite-only public dashboards.
        :type share_list: [str], none_type

        :param share_type: Share type of the public dashboard.
        :type share_type: str

        :param shared_by: User information.
        :type shared_by: DashboardSearchUser

        :param status: Status of the public dashboard.
        :type status: str

        :param token: Unique public dashboard token.
        :type token: str

        :param type: Dashboard type.
        :type type: str

        :param url: URL path to the dashboard.
        :type url: str

        :param widget_count: Number of widgets in the dashboard.
        :type widget_count: int
        """
        super().__init__(kwargs)

        self_.author = author
        self_.created_at = created_at
        self_.deleted_at = deleted_at
        self_.embeddable_domains = embeddable_domains
        self_.experience_type = experience_type
        self_.expiration = expiration
        self_.has_monitors = has_monitors
        self_.is_favorited = is_favorited
        self_.is_public_dashboard_ownerless = is_public_dashboard_ownerless
        self_.is_shared = is_shared
        self_.last_accessed = last_accessed
        self_.modified_at = modified_at
        self_.popularity = popularity
        self_.public_title = public_title
        self_.quality_score = quality_score
        self_.share_list = share_list
        self_.share_type = share_type
        self_.shared_by = shared_by
        self_.status = status
        self_.token = token
        self_.type = type
        self_.url = url
        self_.widget_count = widget_count
