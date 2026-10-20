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
    from datadog_api_client.v2.model.temporary_grant_request_attributes import TemporaryGrantRequestAttributes
    from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType


class TemporaryGrantRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_attributes import TemporaryGrantRequestAttributes
        from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType

        return {
            "attributes": (TemporaryGrantRequestAttributes,),
            "id": (UUID,),
            "type": (TemporaryGrantRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TemporaryGrantRequestAttributes, id: UUID, type: TemporaryGrantRequestType, **kwargs
    ):
        """
        A temporary grant request resource.

        :param attributes: Request history and the linked grant state. List and detail reads include grant_state for approved requests. Decision responses record the decision; read the request for current grant state.
        :type attributes: TemporaryGrantRequestAttributes

        :param id: Server-generated request UUID.
        :type id: UUID

        :param type: The temporary grant request resource type.
        :type type: TemporaryGrantRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
