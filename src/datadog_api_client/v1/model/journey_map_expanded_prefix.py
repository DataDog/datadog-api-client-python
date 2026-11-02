# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class JourneyMapExpandedPrefix(ModelNormal):
    validations = {
        "events": {
            "min_items": 1,
        },
        "path_limit": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "events": ([str],),
            "path_limit": (int,),
        }

    attribute_map = {
        "events": "events",
        "path_limit": "path_limit",
    }

    def __init__(self_, events: List[str], path_limit: Union[int, UnsetType] = unset, **kwargs):
        """
        A path expanded to show the events that follow it.

        :param events: Events of the expanded path, in order.
        :type events: [str]

        :param path_limit: Maximum number of paths shown after the expanded path.
        :type path_limit: int, optional
        """
        if path_limit is not unset:
            kwargs["path_limit"] = path_limit
        super().__init__(kwargs)

        self_.events = events
