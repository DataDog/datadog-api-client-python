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


class SnapshotCreateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "device_type": (str,),
            "event_id": (str,),
            "is_device_type_selected_by_user": (bool,),
            "session_id": (str,),
            "snapshot_name": (str,),
            "start": (int,),
            "view_id": (str,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "device_type": "device_type",
        "event_id": "event_id",
        "is_device_type_selected_by_user": "is_device_type_selected_by_user",
        "session_id": "session_id",
        "snapshot_name": "snapshot_name",
        "start": "start",
        "view_id": "view_id",
        "view_name": "view_name",
    }

    def __init__(
        self_,
        application_id: str,
        device_type: str,
        event_id: str,
        is_device_type_selected_by_user: bool,
        snapshot_name: str,
        start: int,
        view_name: str,
        session_id: Union[str, UnsetType] = unset,
        view_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param application_id:
        :type application_id: str

        :param device_type:
        :type device_type: str

        :param event_id:
        :type event_id: str

        :param is_device_type_selected_by_user:
        :type is_device_type_selected_by_user: bool

        :param session_id:
        :type session_id: str, optional

        :param snapshot_name:
        :type snapshot_name: str

        :param start:
        :type start: int

        :param view_id:
        :type view_id: str, optional

        :param view_name:
        :type view_name: str
        """
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if view_id is not unset:
            kwargs["view_id"] = view_id
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.device_type = device_type
        self_.event_id = event_id
        self_.is_device_type_selected_by_user = is_device_type_selected_by_user
        self_.snapshot_name = snapshot_name
        self_.start = start
        self_.view_name = view_name
