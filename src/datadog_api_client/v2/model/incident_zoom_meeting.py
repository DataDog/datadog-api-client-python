# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentZoomMeeting(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "host_id": (str,),
            "join_url": (str,),
            "meeting_id": (int,),
            "password": (str,),
            "recording_url": (str,),
        }

    attribute_map = {
        "host_id": "host_id",
        "join_url": "join_url",
        "meeting_id": "meeting_id",
        "password": "password",
        "recording_url": "recording_url",
    }

    def __init__(
        self_,
        join_url: str,
        meeting_id: int,
        host_id: Union[str, UnsetType] = unset,
        password: Union[str, UnsetType] = unset,
        recording_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Zoom meeting associated with an incident.

        :param host_id: The Zoom host identifier.
        :type host_id: str, optional

        :param join_url: The URL to join the meeting.
        :type join_url: str

        :param meeting_id: The Zoom meeting identifier.
        :type meeting_id: int

        :param password: The meeting password.
        :type password: str, optional

        :param recording_url: The URL of the meeting recording.
        :type recording_url: str, optional
        """
        if host_id is not unset:
            kwargs["host_id"] = host_id
        if password is not unset:
            kwargs["password"] = password
        if recording_url is not unset:
            kwargs["recording_url"] = recording_url
        super().__init__(kwargs)

        self_.join_url = join_url
        self_.meeting_id = meeting_id
