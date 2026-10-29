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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_live_call import OnCallPageLiveCall
    from datadog_api_client.v2.model.on_call_page_release_origin import OnCallPageReleaseOrigin
    from datadog_api_client.v2.model.on_call_page_status import OnCallPageStatus
    from datadog_api_client.v2.model.page_urgency import PageUrgency


class OnCallPageDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_live_call import OnCallPageLiveCall
        from datadog_api_client.v2.model.on_call_page_release_origin import OnCallPageReleaseOrigin
        from datadog_api_client.v2.model.on_call_page_status import OnCallPageStatus
        from datadog_api_client.v2.model.page_urgency import PageUrgency

        return {
            "acknowledged_at": (datetime,),
            "closed_at": (datetime,),
            "comment_count": (int,),
            "created_at": (datetime,),
            "description": (str,),
            "escalation_policy_uuid": (UUID,),
            "key": (str,),
            "live_call": (OnCallPageLiveCall,),
            "modified_at": (datetime,),
            "release_at": (datetime,),
            "release_origin": (OnCallPageReleaseOrigin,),
            "responders_added_at": (datetime,),
            "services": ([str],),
            "status": (OnCallPageStatus,),
            "tags": ([str],),
            "title": (str,),
            "urgency": (PageUrgency,),
        }

    attribute_map = {
        "acknowledged_at": "acknowledged_at",
        "closed_at": "closed_at",
        "comment_count": "comment_count",
        "created_at": "created_at",
        "description": "description",
        "escalation_policy_uuid": "escalation_policy_uuid",
        "key": "key",
        "live_call": "live_call",
        "modified_at": "modified_at",
        "release_at": "release_at",
        "release_origin": "release_origin",
        "responders_added_at": "responders_added_at",
        "services": "services",
        "status": "status",
        "tags": "tags",
        "title": "title",
        "urgency": "urgency",
    }

    def __init__(
        self_,
        created_at: datetime,
        description: str,
        key: str,
        status: OnCallPageStatus,
        tags: List[str],
        title: str,
        urgency: PageUrgency,
        acknowledged_at: Union[datetime, UnsetType] = unset,
        closed_at: Union[datetime, UnsetType] = unset,
        comment_count: Union[int, UnsetType] = unset,
        escalation_policy_uuid: Union[UUID, UnsetType] = unset,
        live_call: Union[OnCallPageLiveCall, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        release_at: Union[datetime, UnsetType] = unset,
        release_origin: Union[OnCallPageReleaseOrigin, UnsetType] = unset,
        responders_added_at: Union[datetime, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an On-Call Page.

        :param acknowledged_at: The time when the Page was first acknowledged.
        :type acknowledged_at: datetime, optional

        :param closed_at: The time when the Page was resolved.
        :type closed_at: datetime, optional

        :param comment_count: The number of comments on the Page.
        :type comment_count: int, optional

        :param created_at: The time when the Page was created.
        :type created_at: datetime

        :param description: A short summary of the issue or context.
        :type description: str

        :param escalation_policy_uuid: The ID of the escalation policy used to route the Page.
        :type escalation_policy_uuid: UUID, optional

        :param key: An alternative numeric identifier of the Page, as displayed in the Datadog UI.
        :type key: str

        :param live_call: Live call information for a Page triggered by a live call route.
        :type live_call: OnCallPageLiveCall, optional

        :param modified_at: The time when the Page was last modified.
        :type modified_at: datetime, optional

        :param release_at: The time when the snooze ends. Only set while the Page is snoozed, together with ``release_origin``.
        :type release_at: datetime, optional

        :param release_origin: What snoozed the Page. Only set while the Page is snoozed, together with ``release_at``.
            `ack_timeout`: the acknowledgment timeout. `team_rules_active_hours`: the Page was
            triggered outside of the active hours of the team's routing rules. ``manual_snooze`` :
            a user snoozed the Page.
        :type release_origin: OnCallPageReleaseOrigin, optional

        :param responders_added_at: The time when responders were first added to the Page.
        :type responders_added_at: datetime, optional

        :param services: The services associated with the Page.
        :type services: [str], optional

        :param status: The current status of the On-Call Page.
        :type status: OnCallPageStatus

        :param tags: Tags associated with the Page.
        :type tags: [str]

        :param title: The title of the Page.
        :type title: str

        :param urgency: On-Call Page urgency level.
        :type urgency: PageUrgency
        """
        if acknowledged_at is not unset:
            kwargs["acknowledged_at"] = acknowledged_at
        if closed_at is not unset:
            kwargs["closed_at"] = closed_at
        if comment_count is not unset:
            kwargs["comment_count"] = comment_count
        if escalation_policy_uuid is not unset:
            kwargs["escalation_policy_uuid"] = escalation_policy_uuid
        if live_call is not unset:
            kwargs["live_call"] = live_call
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if release_at is not unset:
            kwargs["release_at"] = release_at
        if release_origin is not unset:
            kwargs["release_origin"] = release_origin
        if responders_added_at is not unset:
            kwargs["responders_added_at"] = responders_added_at
        if services is not unset:
            kwargs["services"] = services
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.description = description
        self_.key = key
        self_.status = status
        self_.tags = tags
        self_.title = title
        self_.urgency = urgency
