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


class EntityV3QueueSpec(ModelNormal):
    validations = {
        "lifecycle": {
            "min_length": 1,
        },
        "tier": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "component_of": ([str],),
            "lifecycle": (str,),
            "tier": (str,),
            "type": (str,),
        }

    attribute_map = {
        "component_of": "componentOf",
        "lifecycle": "lifecycle",
        "tier": "tier",
        "type": "type",
    }

    def __init__(
        self_,
        component_of: Union[List[str], UnsetType] = unset,
        lifecycle: Union[str, UnsetType] = unset,
        tier: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 Queue Spec object.

        :param component_of: A list of components the queue is a part of
        :type component_of: [str], optional

        :param lifecycle: The lifecycle state of the queue.
        :type lifecycle: str, optional

        :param tier: The importance of the queue.
        :type tier: str, optional

        :param type: The type of queue.
        :type type: str, optional
        """
        if component_of is not unset:
            kwargs["component_of"] = component_of
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if tier is not unset:
            kwargs["tier"] = tier
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
