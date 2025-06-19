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
    from datadog_api_client.v2.model.event_create_response_attributes_attributes_evt import (
        EventCreateResponseAttributesAttributesEvt,
    )


class EventCreateResponseAttributesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_create_response_attributes_attributes_evt import (
            EventCreateResponseAttributesAttributesEvt,
        )

        return {
            "evt": (EventCreateResponseAttributesAttributesEvt,),
        }

    attribute_map = {
        "evt": "evt",
    }

    def __init__(self_, evt: Union[EventCreateResponseAttributesAttributesEvt, UnsetType] = unset, **kwargs):
        """
        JSON object for category-specific attributes.

        :param evt: JSON object of event system attributes.
        :type evt: EventCreateResponseAttributesAttributesEvt, optional
        """
        if evt is not unset:
            kwargs["evt"] = evt
        super().__init__(kwargs)
