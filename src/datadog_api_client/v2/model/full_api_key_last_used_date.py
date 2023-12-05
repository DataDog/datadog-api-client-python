# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FullAPIKeyLastUsedDate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "timestamp": (str, none_type),
        }

    attribute_map = {
        "description": "description",
        "timestamp": "timestamp",
    }

    def __init__(
        self_, description: Union[str, UnsetType] = unset, timestamp: Union[str, none_type, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for the last time the specific API key was used.

        :param description: The description of the what the API key was used for.
        :type description: str, optional

        :param timestamp: The data and time of when the API key was last used.
        :type timestamp: str, none_type, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
