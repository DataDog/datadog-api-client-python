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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporary_grant_request_decision_attributes import (
        TemporaryGrantRequestDecisionAttributes,
    )
    from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType


class TemporaryGrantRequestDecisionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_decision_attributes import (
            TemporaryGrantRequestDecisionAttributes,
        )
        from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType

        return {
            "attributes": (TemporaryGrantRequestDecisionAttributes,),
            "id": (UUID,),
            "type": (TemporaryGrantRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TemporaryGrantRequestDecisionAttributes,
        type: TemporaryGrantRequestType,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        A decision on a pending request.

        :param attributes: Binary decision. Overrides, reason fields, and unknown attributes are rejected, including null values.
        :type attributes: TemporaryGrantRequestDecisionAttributes

        :param id: Optional request UUID. If supplied it must match request_id in the path.
        :type id: UUID, optional

        :param type: The temporary grant request resource type.
        :type type: TemporaryGrantRequestType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
