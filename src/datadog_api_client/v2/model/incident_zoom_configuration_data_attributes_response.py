# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentZoomConfigurationDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "manual_meeting_creation": (bool,),
            "meeting_chat_timeline_sync": (bool,),
            "modified_at": (datetime,),
            "post_meeting_summary": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "manual_meeting_creation": "manual_meeting_creation",
        "meeting_chat_timeline_sync": "meeting_chat_timeline_sync",
        "modified_at": "modified_at",
        "post_meeting_summary": "post_meeting_summary",
    }

    def __init__(
        self_,
        created_at: datetime,
        manual_meeting_creation: bool,
        meeting_chat_timeline_sync: bool,
        modified_at: datetime,
        post_meeting_summary: bool,
        **kwargs,
    ):
        """
        Attributes of a Zoom configuration.

        :param created_at: Timestamp when the configuration was created.
        :type created_at: datetime

        :param manual_meeting_creation: Whether manual meeting creation is enabled.
        :type manual_meeting_creation: bool

        :param meeting_chat_timeline_sync: Whether meeting chat timeline sync is enabled.
        :type meeting_chat_timeline_sync: bool

        :param modified_at: Timestamp when the configuration was last modified.
        :type modified_at: datetime

        :param post_meeting_summary: Whether post-meeting summary is enabled.
        :type post_meeting_summary: bool
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.manual_meeting_creation = manual_meeting_creation
        self_.meeting_chat_timeline_sync = meeting_chat_timeline_sync
        self_.modified_at = modified_at
        self_.post_meeting_summary = post_meeting_summary
