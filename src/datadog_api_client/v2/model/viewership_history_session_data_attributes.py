# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ViewershipHistorySessionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_id": (str,),
            "last_watched_at": (datetime,),
            "session_event": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "track": (str,),
        }

    attribute_map = {
        "event_id": "event_id",
        "last_watched_at": "last_watched_at",
        "session_event": "session_event",
        "track": "track",
    }

    def __init__(
        self_,
        last_watched_at: datetime,
        event_id: Union[str, UnsetType] = unset,
        session_event: Union[Dict[str, Any], UnsetType] = unset,
        track: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param event_id:
        :type event_id: str, optional

        :param last_watched_at:
        :type last_watched_at: datetime

        :param session_event:
        :type session_event: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param track:
        :type track: str, optional
        """
        if event_id is not unset:
            kwargs["event_id"] = event_id
        if session_event is not unset:
            kwargs["session_event"] = session_event
        if track is not unset:
            kwargs["track"] = track
        super().__init__(kwargs)

        self_.last_watched_at = last_watched_at
