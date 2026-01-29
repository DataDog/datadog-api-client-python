# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProjectNotificationSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "destinations": ([int],),
            "enabled": (bool,),
            "notify_on_case_assignment": (bool,),
            "notify_on_case_closed": (bool,),
            "notify_on_case_comment": (bool,),
            "notify_on_case_comment_mention": (bool,),
            "notify_on_case_priority_change": (bool,),
            "notify_on_case_status_change": (bool,),
            "notify_on_case_unassignment": (bool,),
        }

    attribute_map = {
        "destinations": "destinations",
        "enabled": "enabled",
        "notify_on_case_assignment": "notify_on_case_assignment",
        "notify_on_case_closed": "notify_on_case_closed",
        "notify_on_case_comment": "notify_on_case_comment",
        "notify_on_case_comment_mention": "notify_on_case_comment_mention",
        "notify_on_case_priority_change": "notify_on_case_priority_change",
        "notify_on_case_status_change": "notify_on_case_status_change",
        "notify_on_case_unassignment": "notify_on_case_unassignment",
    }

    def __init__(
        self_,
        destinations: Union[List[int], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        notify_on_case_assignment: Union[bool, UnsetType] = unset,
        notify_on_case_closed: Union[bool, UnsetType] = unset,
        notify_on_case_comment: Union[bool, UnsetType] = unset,
        notify_on_case_comment_mention: Union[bool, UnsetType] = unset,
        notify_on_case_priority_change: Union[bool, UnsetType] = unset,
        notify_on_case_status_change: Union[bool, UnsetType] = unset,
        notify_on_case_unassignment: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project notification settings

        :param destinations: Notification destinations (1=email, 2=slack, 3=in-app)
        :type destinations: [int], optional

        :param enabled: Whether notifications are enabled
        :type enabled: bool, optional

        :param notify_on_case_assignment:
        :type notify_on_case_assignment: bool, optional

        :param notify_on_case_closed:
        :type notify_on_case_closed: bool, optional

        :param notify_on_case_comment:
        :type notify_on_case_comment: bool, optional

        :param notify_on_case_comment_mention:
        :type notify_on_case_comment_mention: bool, optional

        :param notify_on_case_priority_change:
        :type notify_on_case_priority_change: bool, optional

        :param notify_on_case_status_change:
        :type notify_on_case_status_change: bool, optional

        :param notify_on_case_unassignment:
        :type notify_on_case_unassignment: bool, optional
        """
        if destinations is not unset:
            kwargs["destinations"] = destinations
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if notify_on_case_assignment is not unset:
            kwargs["notify_on_case_assignment"] = notify_on_case_assignment
        if notify_on_case_closed is not unset:
            kwargs["notify_on_case_closed"] = notify_on_case_closed
        if notify_on_case_comment is not unset:
            kwargs["notify_on_case_comment"] = notify_on_case_comment
        if notify_on_case_comment_mention is not unset:
            kwargs["notify_on_case_comment_mention"] = notify_on_case_comment_mention
        if notify_on_case_priority_change is not unset:
            kwargs["notify_on_case_priority_change"] = notify_on_case_priority_change
        if notify_on_case_status_change is not unset:
            kwargs["notify_on_case_status_change"] = notify_on_case_status_change
        if notify_on_case_unassignment is not unset:
            kwargs["notify_on_case_unassignment"] = notify_on_case_unassignment
        super().__init__(kwargs)
