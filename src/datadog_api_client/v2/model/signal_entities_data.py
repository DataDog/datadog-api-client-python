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
    from datadog_api_client.v2.model.signal_entities_attributes import SignalEntitiesAttributes
    from datadog_api_client.v2.model.signal_entities_type import SignalEntitiesType


class SignalEntitiesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.signal_entities_attributes import SignalEntitiesAttributes
        from datadog_api_client.v2.model.signal_entities_type import SignalEntitiesType

        return {
            "attributes": (SignalEntitiesAttributes,),
            "id": (str,),
            "type": (SignalEntitiesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SignalEntitiesAttributes, id: str, type: SignalEntitiesType, **kwargs):
        """
        Entities related to a security signal.

        :param attributes: Attributes containing the entities related to the signal.
        :type attributes: SignalEntitiesAttributes

        :param id: The signal ID the entities are associated with.
        :type id: str

        :param type: The type of the resource. The value should always be ``entities``.
        :type type: SignalEntitiesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
