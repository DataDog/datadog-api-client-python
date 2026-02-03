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


class SnapshotUpdateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_id": (str,),
            "is_device_type_selected_by_user": (bool,),
            "session_id": (str,),
            "start": (int,),
            "view_id": (str,),
        }

    attribute_map = {
        "event_id": "event_id",
        "is_device_type_selected_by_user": "is_device_type_selected_by_user",
        "session_id": "session_id",
        "start": "start",
        "view_id": "view_id",
    }

    def __init__(
        self_,
        event_id: str,
        is_device_type_selected_by_user: bool,
        start: int,
        session_id: Union[str, UnsetType] = unset,
        view_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param event_id:
        :type event_id: str

        :param is_device_type_selected_by_user:
        :type is_device_type_selected_by_user: bool

        :param session_id:
        :type session_id: str, optional

        :param start:
        :type start: int

        :param view_id:
        :type view_id: str, optional
        """
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if view_id is not unset:
            kwargs["view_id"] = view_id
        super().__init__(kwargs)

        self_.event_id = event_id
        self_.is_device_type_selected_by_user = is_device_type_selected_by_user
        self_.start = start
