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


class PlaylistsSessionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
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
        "session_event": "session_event",
        "track": "track",
    }

    def __init__(
        self_, session_event: Union[Dict[str, Any], UnsetType] = unset, track: Union[str, UnsetType] = unset, **kwargs
    ):
        """


        :param session_event:
        :type session_event: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param track:
        :type track: str, optional
        """
        if session_event is not unset:
            kwargs["session_event"] = session_event
        if track is not unset:
            kwargs["track"] = track
        super().__init__(kwargs)
