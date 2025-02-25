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
    from datadog_api_client.v1.model.shared_dashboard_update_request_global_time import (
        SharedDashboardUpdateRequestGlobalTime,
    )
    from datadog_api_client.v1.model.shared_dashboard_invitees_items import SharedDashboardInviteesItems
    from datadog_api_client.v1.model.selectable_template_variable_items import SelectableTemplateVariableItems
    from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
    from datadog_api_client.v1.model.shared_dashboard_status import SharedDashboardStatus
    from datadog_api_client.v1.model.viewing_preferences import ViewingPreferences


class SharedDashboardUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.shared_dashboard_update_request_global_time import (
            SharedDashboardUpdateRequestGlobalTime,
        )
        from datadog_api_client.v1.model.shared_dashboard_invitees_items import SharedDashboardInviteesItems
        from datadog_api_client.v1.model.selectable_template_variable_items import SelectableTemplateVariableItems
        from datadog_api_client.v1.model.dashboard_share_type import DashboardShareType
        from datadog_api_client.v1.model.shared_dashboard_status import SharedDashboardStatus
        from datadog_api_client.v1.model.viewing_preferences import ViewingPreferences

        return {
            "embeddable_domains": ([str],),
            "expiration": (datetime, none_type),
            "global_time": (SharedDashboardUpdateRequestGlobalTime,),
            "global_time_selectable_enabled": (bool, none_type),
            "invitees": ([SharedDashboardInviteesItems],),
            "selectable_template_vars": ([SelectableTemplateVariableItems], none_type),
            "share_list": ([str], none_type),
            "share_type": (DashboardShareType,),
            "status": (SharedDashboardStatus,),
            "title": (str,),
            "viewing_preferences": (ViewingPreferences,),
        }

    attribute_map = {
        "embeddable_domains": "embeddable_domains",
        "expiration": "expiration",
        "global_time": "global_time",
        "global_time_selectable_enabled": "global_time_selectable_enabled",
        "invitees": "invitees",
        "selectable_template_vars": "selectable_template_vars",
        "share_list": "share_list",
        "share_type": "share_type",
        "status": "status",
        "title": "title",
        "viewing_preferences": "viewing_preferences",
    }

    def __init__(
        self_,
        embeddable_domains: Union[List[str], UnsetType] = unset,
        expiration: Union[datetime, none_type, UnsetType] = unset,
        global_time: Union[SharedDashboardUpdateRequestGlobalTime, none_type, UnsetType] = unset,
        global_time_selectable_enabled: Union[bool, none_type, UnsetType] = unset,
        invitees: Union[List[SharedDashboardInviteesItems], UnsetType] = unset,
        selectable_template_vars: Union[List[SelectableTemplateVariableItems], none_type, UnsetType] = unset,
        share_list: Union[List[str], none_type, UnsetType] = unset,
        share_type: Union[DashboardShareType, none_type, UnsetType] = unset,
        status: Union[SharedDashboardStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        viewing_preferences: Union[ViewingPreferences, UnsetType] = unset,
        **kwargs,
    ):
        """
        Update a shared dashboard's settings.

        :param embeddable_domains: The ``SharedDashboard`` ``embeddable_domains``.
        :type embeddable_domains: [str], optional

        :param expiration: The time when an OPEN shared dashboard becomes publicly unavailable.
        :type expiration: datetime, none_type, optional

        :param global_time: Timeframe setting for the shared dashboard.
        :type global_time: SharedDashboardUpdateRequestGlobalTime, none_type, optional

        :param global_time_selectable_enabled: Whether to allow viewers to select a different global time setting for the shared dashboard.
        :type global_time_selectable_enabled: bool, none_type, optional

        :param invitees: The ``SharedDashboard`` ``invitees``.
        :type invitees: [SharedDashboardInviteesItems], optional

        :param selectable_template_vars: List of objects representing template variables on the shared dashboard which can have selectable values.
        :type selectable_template_vars: [SelectableTemplateVariableItems], none_type, optional

        :param share_list: List of email addresses that can be given access to the shared dashboard. **Deprecated**.
        :type share_list: [str], none_type, optional

        :param share_type: Type of sharing access (either open to anyone who has the public URL or invite-only).
        :type share_type: DashboardShareType, none_type, optional

        :param status: Active means the dashboard is publicly available. Paused means the dashboard is not publicly available.
        :type status: SharedDashboardStatus, optional

        :param title: Title of the shared dashboard.
        :type title: str, optional

        :param viewing_preferences: The viewing preferences for a shared dashboard.
        :type viewing_preferences: ViewingPreferences, optional
        """
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
        if viewing_preferences is not unset:
            kwargs["viewing_preferences"] = viewing_preferences
        super().__init__(kwargs)
