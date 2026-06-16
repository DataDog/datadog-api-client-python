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
    from datadog_api_client.v2.model.shared_dashboard_global_time import SharedDashboardGlobalTime
    from datadog_api_client.v2.model.shared_dashboard_invitee import SharedDashboardInvitee
    from datadog_api_client.v2.model.shared_dashboard_selectable_template_variable import (
        SharedDashboardSelectableTemplateVariable,
    )
    from datadog_api_client.v2.model.shared_dashboard_share_type import SharedDashboardShareType
    from datadog_api_client.v2.model.shared_dashboard_status import SharedDashboardStatus
    from datadog_api_client.v2.model.shared_dashboard_viewing_preferences import SharedDashboardViewingPreferences


class SharedDashboardResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_global_time import SharedDashboardGlobalTime
        from datadog_api_client.v2.model.shared_dashboard_invitee import SharedDashboardInvitee
        from datadog_api_client.v2.model.shared_dashboard_selectable_template_variable import (
            SharedDashboardSelectableTemplateVariable,
        )
        from datadog_api_client.v2.model.shared_dashboard_share_type import SharedDashboardShareType
        from datadog_api_client.v2.model.shared_dashboard_status import SharedDashboardStatus
        from datadog_api_client.v2.model.shared_dashboard_viewing_preferences import SharedDashboardViewingPreferences

        return {
            "created_at": (datetime,),
            "embeddable_domains": ([str],),
            "expiration": (datetime, none_type),
            "global_time": (SharedDashboardGlobalTime,),
            "global_time_selectable": (bool,),
            "invitees": ([SharedDashboardInvitee],),
            "last_accessed": (datetime, none_type),
            "selectable_template_vars": ([SharedDashboardSelectableTemplateVariable],),
            "share_type": (SharedDashboardShareType,),
            "sharer_disabled": (bool,),
            "status": (SharedDashboardStatus,),
            "title": (str,),
            "token": (str,),
            "url": (str,),
            "viewing_preferences": (SharedDashboardViewingPreferences,),
        }

    attribute_map = {
        "created_at": "created_at",
        "embeddable_domains": "embeddable_domains",
        "expiration": "expiration",
        "global_time": "global_time",
        "global_time_selectable": "global_time_selectable",
        "invitees": "invitees",
        "last_accessed": "last_accessed",
        "selectable_template_vars": "selectable_template_vars",
        "share_type": "share_type",
        "sharer_disabled": "sharer_disabled",
        "status": "status",
        "title": "title",
        "token": "token",
        "url": "url",
        "viewing_preferences": "viewing_preferences",
    }

    def __init__(
        self_,
        created_at: datetime,
        embeddable_domains: List[str],
        expiration: Union[datetime, none_type],
        global_time: Union[SharedDashboardGlobalTime, none_type],
        global_time_selectable: bool,
        invitees: List[SharedDashboardInvitee],
        last_accessed: Union[datetime, none_type],
        selectable_template_vars: List[SharedDashboardSelectableTemplateVariable],
        share_type: SharedDashboardShareType,
        sharer_disabled: bool,
        status: SharedDashboardStatus,
        title: str,
        token: str,
        url: str,
        viewing_preferences: SharedDashboardViewingPreferences,
        **kwargs,
    ):
        """
        Attributes of a shared dashboard response.

        :param created_at: Time when the shared dashboard was created.
        :type created_at: datetime

        :param embeddable_domains: Domains where embed-type shared dashboards can be embedded.
        :type embeddable_domains: [str]

        :param expiration: Time when the shared dashboard expires.
        :type expiration: datetime, none_type

        :param global_time: Default time range configuration for the shared dashboard.
        :type global_time: SharedDashboardGlobalTime, none_type

        :param global_time_selectable: Whether viewers can select a different global time setting.
        :type global_time_selectable: bool

        :param invitees: Invitees for invite-only shared dashboards.
        :type invitees: [SharedDashboardInvitee]

        :param last_accessed: Time when the shared dashboard was last accessed.
        :type last_accessed: datetime, none_type

        :param selectable_template_vars: Template variables that viewers can modify.
        :type selectable_template_vars: [SharedDashboardSelectableTemplateVariable]

        :param share_type: Type of dashboard sharing.
        :type share_type: SharedDashboardShareType

        :param sharer_disabled: Whether the user who shared the dashboard is disabled.
        :type sharer_disabled: bool

        :param status: Status of the shared dashboard.
        :type status: SharedDashboardStatus

        :param title: Display title for the shared dashboard.
        :type title: str

        :param token: Token assigned to the shared dashboard.
        :type token: str

        :param url: URL for the shared dashboard.
        :type url: str

        :param viewing_preferences: Display settings for the shared dashboard.
        :type viewing_preferences: SharedDashboardViewingPreferences
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.embeddable_domains = embeddable_domains
        self_.expiration = expiration
        self_.global_time = global_time
        self_.global_time_selectable = global_time_selectable
        self_.invitees = invitees
        self_.last_accessed = last_accessed
        self_.selectable_template_vars = selectable_template_vars
        self_.share_type = share_type
        self_.sharer_disabled = sharer_disabled
        self_.status = status
        self_.title = title
        self_.token = token
        self_.url = url
        self_.viewing_preferences = viewing_preferences
