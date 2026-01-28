# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.patch_status_page_request_data_attributes import (
        PatchStatusPageRequestDataAttributes,
    )
    from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType


class PatchStatusPageRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_status_page_request_data_attributes import (
            PatchStatusPageRequestDataAttributes,
        )
        from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

        return {
            "attributes": (PatchStatusPageRequestDataAttributes,),
            "id": (UUID,),
            "type": (StatusPageDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PatchStatusPageRequestDataAttributes, id: UUID, type: StatusPageDataType, **kwargs):
        """


        :param attributes: The supported attributes for updating a status page.
        :type attributes: PatchStatusPageRequestDataAttributes

        :param id: The ID of the status page.
        :type id: UUID

        :param type: Status pages resource type.
        :type type: StatusPageDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
