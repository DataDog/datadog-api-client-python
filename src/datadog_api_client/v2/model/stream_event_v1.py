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


class StreamEventV1(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data": (dict,),
            "type": (str,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(self_, type: str, data: Union[dict, UnsetType] = unset, **kwargs):
        """


        :param data: The event data payload.
        :type data: dict, optional

        :param type: The type of stream event.
        :type type: str
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

        self_.type = type
