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
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1_20270101.model.dashboard_summary_id import DashboardSummaryID


class DashboardSummaryDefinition(ModelNormal):
    validations = {
        "popularity": {
            "inclusive_maximum": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.creator import Creator
        from datadog_api_client.v1_20270101.model.dashboard_summary_id import DashboardSummaryID

        return {
            "author": (Creator,),
            "created": (datetime, none_type),
            "icon": (str, none_type),
            "id": (DashboardSummaryID,),
            "integration_id": (str, none_type),
            "is_favorite": (bool,),
            "is_read_only": (bool,),
            "is_shared": (bool,),
            "last_view_date": (str, none_type),
            "modified": (datetime, none_type),
            "popularity": (int,),
            "tags": ([str], none_type),
            "title": (str,),
            "type": (str,),
            "url": (str,),
        }

    attribute_map = {
        "author": "author",
        "created": "created",
        "icon": "icon",
        "id": "id",
        "integration_id": "integration_id",
        "is_favorite": "is_favorite",
        "is_read_only": "is_read_only",
        "is_shared": "is_shared",
        "last_view_date": "last_view_date",
        "modified": "modified",
        "popularity": "popularity",
        "tags": "tags",
        "title": "title",
        "type": "type",
        "url": "url",
    }
    read_only_vars = {
        "author",
        "created",
        "icon",
        "integration_id",
        "is_favorite",
        "is_read_only",
        "is_shared",
        "last_view_date",
        "modified",
        "popularity",
        "tags",
        "title",
        "type",
        "url",
    }

    def __init__(
        self_,
        author: Union[Creator, UnsetType] = unset,
        created: Union[datetime, none_type, UnsetType] = unset,
        icon: Union[str, none_type, UnsetType] = unset,
        id: Union[DashboardSummaryID, str, int, UnsetType] = unset,
        integration_id: Union[str, none_type, UnsetType] = unset,
        is_favorite: Union[bool, UnsetType] = unset,
        is_read_only: Union[bool, UnsetType] = unset,
        is_shared: Union[bool, UnsetType] = unset,
        last_view_date: Union[str, none_type, UnsetType] = unset,
        modified: Union[datetime, none_type, UnsetType] = unset,
        popularity: Union[int, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dashboard definition.

        :param author: Object describing the creator of the shared element.
        :type author: Creator, optional

        :param created: Date of creation of the dashboard.
        :type created: datetime, none_type, optional

        :param icon: URL to the icon of the dashboard.
        :type icon: str, none_type, optional

        :param id: ID of the dashboard.
        :type id: DashboardSummaryID, optional

        :param integration_id: The short name of the integration.
        :type integration_id: str, none_type, optional

        :param is_favorite: Whether the dashboard is in the favorites.
        :type is_favorite: bool, optional

        :param is_read_only: Whether the dashboard is read only.
        :type is_read_only: bool, optional

        :param is_shared: Whether the dashboard is publicly shared.
        :type is_shared: bool, optional

        :param last_view_date: Date when the dashboard was last viewed.
        :type last_view_date: str, none_type, optional

        :param modified: Date of last edition of the dashboard.
        :type modified: datetime, none_type, optional

        :param popularity: Popularity of the dashboard.
        :type popularity: int, optional

        :param tags: List of team names representing ownership of the dashboard.
        :type tags: [str], none_type, optional

        :param title: Title of the dashboard.
        :type title: str, optional

        :param type: The type of the dashboard.
        :type type: str, optional

        :param url: URL path to the dashboard.
        :type url: str, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if created is not unset:
            kwargs["created"] = created
        if icon is not unset:
            kwargs["icon"] = icon
        if id is not unset:
            kwargs["id"] = id
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
        if is_favorite is not unset:
            kwargs["is_favorite"] = is_favorite
        if is_read_only is not unset:
            kwargs["is_read_only"] = is_read_only
        if is_shared is not unset:
            kwargs["is_shared"] = is_shared
        if last_view_date is not unset:
            kwargs["last_view_date"] = last_view_date
        if modified is not unset:
            kwargs["modified"] = modified
        if popularity is not unset:
            kwargs["popularity"] = popularity
        if tags is not unset:
            kwargs["tags"] = tags
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
