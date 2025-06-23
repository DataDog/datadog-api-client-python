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
    from datadog_api_client.v2.model.event_create_response_attributes_attributes import (
        EventCreateResponseAttributesAttributes,
    )


class EventCreateResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_create_response_attributes_attributes import (
            EventCreateResponseAttributesAttributes,
        )

        return {
            "attributes": (EventCreateResponseAttributesAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self_, attributes: Union[EventCreateResponseAttributesAttributes, UnsetType] = unset, **kwargs):
        """
        JSON object containing all events attributes and their associated values.

        :param attributes: JSON object of attributes from your events.
        :type attributes: EventCreateResponseAttributesAttributes, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
