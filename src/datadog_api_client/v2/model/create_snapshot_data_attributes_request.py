# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_snapshot_additional_config import CreateSnapshotAdditionalConfig
    from datadog_api_client.v2.model.create_snapshot_ttl import CreateSnapshotTTL


class CreateSnapshotDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_snapshot_additional_config import CreateSnapshotAdditionalConfig
        from datadog_api_client.v2.model.create_snapshot_ttl import CreateSnapshotTTL

        return {
            "additional_config": (CreateSnapshotAdditionalConfig,),
            "end": (int,),
            "height": (int,),
            "is_authenticated": (bool,),
            "start": (int,),
            "ttl": (CreateSnapshotTTL,),
            "widget_definition": (
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
            "width": (int,),
        }

    attribute_map = {
        "additional_config": "additional_config",
        "end": "end",
        "height": "height",
        "is_authenticated": "is_authenticated",
        "start": "start",
        "ttl": "ttl",
        "widget_definition": "widget_definition",
        "width": "width",
    }

    def __init__(
        self_,
        end: int,
        start: int,
        widget_definition: Dict[str, Any],
        additional_config: Union[CreateSnapshotAdditionalConfig, UnsetType] = unset,
        height: Union[int, UnsetType] = unset,
        is_authenticated: Union[bool, UnsetType] = unset,
        ttl: Union[CreateSnapshotTTL, UnsetType] = unset,
        width: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for snapshot creation.

        :param additional_config: Additional configuration options for snapshot creation.
        :type additional_config: CreateSnapshotAdditionalConfig, optional

        :param end: End of the time window for the snapshot, in milliseconds since Unix epoch.
        :type end: int

        :param height: The height of the rendered snapshot in pixels.
        :type height: int, optional

        :param is_authenticated: Whether the snapshot requires authentication to view. Authenticated snapshots are scoped to the creating organization.
        :type is_authenticated: bool, optional

        :param start: Start of the time window for the snapshot, in milliseconds since Unix epoch.
        :type start: int

        :param ttl: The time-to-live for the snapshot. This value corresponds to storage lifecycle policies that automatically delete the snapshot after the specified period.
        :type ttl: CreateSnapshotTTL, optional

        :param widget_definition: The widget definition to render as a snapshot. Must include a valid ``type`` field and non-empty ``requests`` array.
        :type widget_definition: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param width: The width of the rendered snapshot in pixels.
        :type width: int, optional
        """
        if additional_config is not unset:
            kwargs["additional_config"] = additional_config
        if height is not unset:
            kwargs["height"] = height
        if is_authenticated is not unset:
            kwargs["is_authenticated"] = is_authenticated
        if ttl is not unset:
            kwargs["ttl"] = ttl
        if width is not unset:
            kwargs["width"] = width
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
        self_.widget_definition = widget_definition
