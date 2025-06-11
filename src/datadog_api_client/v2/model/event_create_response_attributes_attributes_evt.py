# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EventCreateResponseAttributesAttributesEvt(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "uid": (str,),
        }

    attribute_map = {
        "id": "id",
        "uid": "uid",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, uid: Union[str, UnsetType] = unset, **kwargs):
        """
        JSON object of event system attributes.

        :param id: Event identifier. This field is deprecated and will be removed in a future version. Use the ``uid`` field instead. **Deprecated**.
        :type id: str, optional

        :param uid: A unique identifier for the event. You can use this identifier to query or reference the event.
        :type uid: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if uid is not unset:
            kwargs["uid"] = uid
        super().__init__(kwargs)
