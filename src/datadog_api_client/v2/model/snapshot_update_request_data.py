# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.snapshot_update_request_data_attributes import SnapshotUpdateRequestDataAttributes
    from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType


class SnapshotUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snapshot_update_request_data_attributes import (
            SnapshotUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.snapshot_update_request_data_type import SnapshotUpdateRequestDataType

        return {
            "attributes": (SnapshotUpdateRequestDataAttributes,),
            "id": (str,),
            "type": (SnapshotUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: SnapshotUpdateRequestDataType,
        attributes: Union[SnapshotUpdateRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a heatmap snapshot update request, containing the resource identifier, type, and attributes.

        :param attributes: Attributes for updating a heatmap snapshot, including event, session, and view context.
        :type attributes: SnapshotUpdateRequestDataAttributes, optional

        :param id: Unique identifier of the heatmap snapshot to update.
        :type id: str, optional

        :param type: Snapshots resource type.
        :type type: SnapshotUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
