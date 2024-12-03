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
    from datadog_api_client.v2.model.data_deletion_response_item_attributes import DataDeletionResponseItemAttributes


class DataDeletionResponseItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_deletion_response_item_attributes import (
            DataDeletionResponseItemAttributes,
        )

        return {
            "attributes": (DataDeletionResponseItemAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DataDeletionResponseItemAttributes, id: str, type: str, **kwargs):
        """
        The created data deletion request information.

        :param attributes: Deletion attribute for data deletion response.
        :type attributes: DataDeletionResponseItemAttributes

        :param id: The ID of the created data deletion request.
        :type id: str

        :param type: The type of the request created.
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
