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


class EventCreateResponsePayloadLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "self": (str,),
        }

    attribute_map = {
        "self": "self",
    }

    def __init__(self_, self: Union[str, UnsetType] = unset, **kwargs):
        """
        Links to the event.

        :param self: The URL of the event. This link is only functional when using the default subdomain.
        :type self: str, optional
        """
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
