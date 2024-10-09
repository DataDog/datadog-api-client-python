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
    from datadog_api_client.v2.model.change_event import ChangeEvent
    from datadog_api_client.v2.model.change_event_create_request_type import ChangeEventCreateRequestType


class ChangeEventCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event import ChangeEvent
        from datadog_api_client.v2.model.change_event_create_request_type import ChangeEventCreateRequestType

        return {
            "attributes": (ChangeEvent,),
            "type": (ChangeEventCreateRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ChangeEvent, UnsetType] = unset,
        type: Union[ChangeEventCreateRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object representing an event.

        :param attributes: Object representing a change event.
        :type attributes: ChangeEvent, optional

        :param type: Entity type.
        :type type: ChangeEventCreateRequestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
