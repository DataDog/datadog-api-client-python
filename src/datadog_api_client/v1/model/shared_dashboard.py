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
    from datadog_api_client.v1.model.shared_dashboard_author import SharedDashboardAuthor
    from datadog_api_client.v1.model.dashboard_type import DashboardType
    from datadog_api_client.v1.model.dashboard_global_time import DashboardGlobalTime
    from datadog_api_client.v1.model.shared_dashboard_invitees_items import SharedDashboardInviteesItems
    from datadog_api_client.v1.model.selectable_template_variable_items import SelectableTemplateVariableItems
    from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
    from datadog_api_client.v1.model.shared_dashboard_status import SharedDashboardStatus
    from datadog_api_client.v1.model.viewing_preferences import ViewingPreferences


class SharedDashboard(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.shared_dashboard_author import SharedDashboardAuthor
        from datadog_api_client.v1.model.dashboard_type import DashboardType
        from datadog_api_client.v1.model.dashboard_global_time import DashboardGlobalTime
        from datadog_api_client.v1.model.shared_dashboard_invitees_items import SharedDashboardInviteesItems
        from datadog_api_client.v1.model.selectable_template_variable_items import SelectableTemplateVariableItems
        from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
        from datadog_api_client.v1.model.shared_dashboard_status import SharedDashboardStatus
        from datadog_api_client.v1.model.viewing_preferences import ViewingPreferences

        return {
            "author": (SharedDashboardAuthor,),
            "created": (datetime,),
            "dashboard_id": (str,),
            "dashboard_type": (DashboardType,),
            "embeddable_domains": ([str],),
            "expiration": (datetime, none_type),
            "global_time": (DashboardGlobalTime,),
            "global_time_selectable_enabled": (bool, none_type),
            "invitees": ([SharedDashboardInviteesItems],),
            "last_accessed": (datetime, none_type),
            "public_url": (str,),
            "selectable_template_vars": ([SelectableTemplateVariableItems], none_type),
            "share_list": ([str], none_type),
            "share_type": (DashboardShareType,),
            "status": (SharedDashboardStatus,),
            "title": (str,),
            "token": (str,),
            "viewing_preferences": (ViewingPreferences,),
        }

    attribute_map = {
        "author": "author",
        "created": "created",
        "dashboard_id": "dashboard_id",
        "dashboard_type": "dashboard_type",
        "embeddable_domains": "embeddable_domains",
        "expiration": "expiration",
        "global_time": "global_time",
        "global_time_selectable_enabled": "global_time_selectable_enabled",
        "invitees": "invitees",
        "last_accessed": "last_accessed",
        "public_url": "public_url",
        "selectable_template_vars": "selectable_template_vars",
        "share_list": "share_list",
        "share_type": "share_type",
        "status": "status",
        "title": "title",
        "token": "token",
        "viewing_preferences": "viewing_preferences",
    }
    read_only_vars = {
        "author",
        "created",
        "last_accessed",
        "public_url",
        "token",
    }

    def __init__(
        self_,
        dashboard_id: str,
        dashboard_type: DashboardType,
        author: Union[SharedDashboardAuthor, UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        embeddable_domains: Union[List[str], UnsetType] = unset,
        expiration: Union[datetime, none_type, UnsetType] = unset,
        global_time: Union[DashboardGlobalTime, UnsetType] = unset,
        global_time_selectable_enabled: Union[bool, none_type, UnsetType] = unset,
        invitees: Union[List[SharedDashboardInviteesItems], UnsetType] = unset,
        last_accessed: Union[datetime, none_type, UnsetType] = unset,
        public_url: Union[str, UnsetType] = unset,
        selectable_template_vars: Union[List[SelectableTemplateVariableItems], none_type, UnsetType] = unset,
        share_list: Union[List[str], none_type, UnsetType] = unset,
        share_type: Union[DashboardShareType, none_type, UnsetType] = unset,
        status: Union[SharedDashboardStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        token: Union[str, UnsetType] = unset,
        viewing_preferences: Union[ViewingPreferences, UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata object associated with how a dashboard has been/will be shared.

        :param author: User who shared the dashboard.
        :type author: SharedDashboardAuthor, optional

        :param created: Date the dashboard was shared.
        :type created: datetime, optional

        :param dashboard_id: ID of the dashboard to share.
        :type dashboard_id: str

        :param dashboard_type: The type of the associated private dashboard.
        :type dashboard_type: DashboardType

        :param embeddable_domains: The ``SharedDashboard`` ``embeddable_domains``.
        :type embeddable_domains: [str], optional

        :param expiration: The time when an OPEN shared dashboard becomes publicly unavailable.
        :type expiration: datetime, none_type, optional

        :param global_time: Object containing the live span selection for the dashboard.
        :type global_time: DashboardGlobalTime, optional

        :param global_time_selectable_enabled: Whether to allow viewers to select a different global time setting for the shared dashboard.
        :type global_time_selectable_enabled: bool, none_type, optional

        :param invitees: The ``SharedDashboard`` ``invitees``.
        :type invitees: [SharedDashboardInviteesItems], optional

        :param last_accessed: The last time the shared dashboard was accessed. Null if never accessed.
        :type last_accessed: datetime, none_type, optional

        :param public_url: URL of the shared dashboard.
        :type public_url: str, optional

        :param selectable_template_vars: List of objects representing template variables on the shared dashboard which can have selectable values.
        :type selectable_template_vars: [SelectableTemplateVariableItems], none_type, optional

        :param share_list: List of email addresses that can receive an invitation to access to the shared dashboard. **Deprecated**.
        :type share_list: [str], none_type, optional

        :param share_type: Type of sharing access (either open to anyone who has the public URL or invite-only).
        :type share_type: DashboardShareType, none_type, optional

        :param status: Active means the dashboard is publicly available. Paused means the dashboard is not publicly available.
        :type status: SharedDashboardStatus, optional

        :param title: Title of the shared dashboard.
        :type title: str, optional

        :param token: A unique token assigned to the shared dashboard.
        :type token: str, optional

        :param viewing_preferences: The viewing preferences for a shared dashboard.
        :type viewing_preferences: ViewingPreferences, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if created is not unset:
            kwargs["created"] = created
        if embeddable_domains is not unset:
            kwargs["embeddable_domains"] = embeddable_domains
        if expiration is not unset:
            kwargs["expiration"] = expiration
        if global_time is not unset:
            kwargs["global_time"] = global_time
        if global_time_selectable_enabled is not unset:
            kwargs["global_time_selectable_enabled"] = global_time_selectable_enabled
        if invitees is not unset:
            kwargs["invitees"] = invitees
        if last_accessed is not unset:
            kwargs["last_accessed"] = last_accessed
        if public_url is not unset:
            kwargs["public_url"] = public_url
        if selectable_template_vars is not unset:
            kwargs["selectable_template_vars"] = selectable_template_vars
        if share_list is not unset:
            kwargs["share_list"] = share_list
        if share_type is not unset:
            kwargs["share_type"] = share_type
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if token is not unset:
            kwargs["token"] = token
        if viewing_preferences is not unset:
            kwargs["viewing_preferences"] = viewing_preferences
        super().__init__(kwargs)

        self_.dashboard_id = dashboard_id
        self_.dashboard_type = dashboard_type
