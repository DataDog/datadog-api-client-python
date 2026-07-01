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
    from datadog_api_client.v2.model.create_snapshot_data_response import CreateSnapshotDataResponse


class CreateSnapshotResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_snapshot_data_response import CreateSnapshotDataResponse

        return {
            "data": (CreateSnapshotDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateSnapshotDataResponse, **kwargs):
        """
        Response body for a snapshot creation request.

        :param data: Data envelope for the snapshot creation response.
        :type data: CreateSnapshotDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
