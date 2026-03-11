# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class SnapshotDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "created_by_handle": (str,),
            "created_by_user_id": (int,),
            "device_type": (str,),
            "event_id": (str,),
            "is_device_type_selected_by_user": (bool,),
            "modified_at": (datetime,),
            "org_id": (int,),
            "session_id": (str,),
            "snapshot_name": (str,),
            "start": (int,),
            "view_id": (str,),
            "view_name": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "created_at": "created_at",
        "created_by": "created_by",
        "created_by_handle": "created_by_handle",
        "created_by_user_id": "created_by_user_id",
        "device_type": "device_type",
        "event_id": "event_id",
        "is_device_type_selected_by_user": "is_device_type_selected_by_user",
        "modified_at": "modified_at",
        "org_id": "org_id",
        "session_id": "session_id",
        "snapshot_name": "snapshot_name",
        "start": "start",
        "view_id": "view_id",
        "view_name": "view_name",
    }
    read_only_vars = {
        "created_at",
        "created_by",
        "created_by_handle",
        "created_by_user_id",
        "modified_at",
        "org_id",
    }

    def __init__(
        self_,
        application_id: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        created_by_user_id: Union[int, UnsetType] = unset,
        device_type: Union[str, UnsetType] = unset,
        event_id: Union[str, UnsetType] = unset,
        is_device_type_selected_by_user: Union[bool, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        session_id: Union[str, UnsetType] = unset,
        snapshot_name: Union[str, UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
        view_id: Union[str, UnsetType] = unset,
        view_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a heatmap snapshot, including view context, device information, and audit metadata.

        :param application_id: Unique identifier of the RUM application.
        :type application_id: str, optional

        :param created_at: Timestamp when the snapshot was created.
        :type created_at: datetime, optional

        :param created_by: Display name of the user who created the snapshot.
        :type created_by: str, optional

        :param created_by_handle: Email handle of the user who created the snapshot.
        :type created_by_handle: str, optional

        :param created_by_user_id: Numeric identifier of the user who created the snapshot.
        :type created_by_user_id: int, optional

        :param device_type: Device type used when capturing the snapshot (e.g., desktop, mobile, tablet).
        :type device_type: str, optional

        :param event_id: Unique identifier of the RUM event associated with the snapshot.
        :type event_id: str, optional

        :param is_device_type_selected_by_user: Indicates whether the device type was explicitly selected by the user rather than auto-detected.
        :type is_device_type_selected_by_user: bool, optional

        :param modified_at: Timestamp when the snapshot was last modified.
        :type modified_at: datetime, optional

        :param org_id: Numeric identifier of the organization that owns the snapshot.
        :type org_id: int, optional

        :param session_id: Unique identifier of the RUM session associated with the snapshot.
        :type session_id: str, optional

        :param snapshot_name: Human-readable name for the snapshot.
        :type snapshot_name: str, optional

        :param start: Offset in milliseconds from the start of the session at which the snapshot was captured.
        :type start: int, optional

        :param view_id: Unique identifier of the RUM view associated with the snapshot.
        :type view_id: str, optional

        :param view_name: URL path or name of the view where the snapshot was captured.
        :type view_name: str, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if created_by_user_id is not unset:
            kwargs["created_by_user_id"] = created_by_user_id
        if device_type is not unset:
            kwargs["device_type"] = device_type
        if event_id is not unset:
            kwargs["event_id"] = event_id
        if is_device_type_selected_by_user is not unset:
            kwargs["is_device_type_selected_by_user"] = is_device_type_selected_by_user
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if snapshot_name is not unset:
            kwargs["snapshot_name"] = snapshot_name
        if start is not unset:
            kwargs["start"] = start
        if view_id is not unset:
            kwargs["view_id"] = view_id
        if view_name is not unset:
            kwargs["view_name"] = view_name
        super().__init__(kwargs)
