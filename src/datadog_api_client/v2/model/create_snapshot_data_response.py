# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_snapshot_data_attributes_response import (
        CreateSnapshotDataAttributesResponse,
    )
    from datadog_api_client.v2.model.create_snapshot_type import CreateSnapshotType


class CreateSnapshotDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_snapshot_data_attributes_response import (
            CreateSnapshotDataAttributesResponse,
        )
        from datadog_api_client.v2.model.create_snapshot_type import CreateSnapshotType

        return {
            "attributes": (CreateSnapshotDataAttributesResponse,),
            "id": (str,),
            "type": (CreateSnapshotType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CreateSnapshotDataAttributesResponse, id: str, type: CreateSnapshotType, **kwargs):
        """
        Data envelope for the snapshot creation response.

        :param attributes: Attributes of the created snapshot.
        :type attributes: CreateSnapshotDataAttributesResponse

        :param id: The unique identifier of the created snapshot.
        :type id: str

        :param type: The type identifier for snapshot creation resources.
        :type type: CreateSnapshotType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
