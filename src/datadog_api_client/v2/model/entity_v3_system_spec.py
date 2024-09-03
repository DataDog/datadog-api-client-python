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


class EntityV3SystemSpec(ModelNormal):
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
            "components": ([str],),
            "lifecycle": (str,),
            "tier": (str,),
        }

    attribute_map = {
        "components": "components",
        "lifecycle": "lifecycle",
        "tier": "tier",
    }

    def __init__(
        self_,
        components: Union[List[str], UnsetType] = unset,
        lifecycle: Union[str, UnsetType] = unset,
        tier: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 System Spec object.

        :param components: A list of components belongs to the system.
        :type components: [str], optional

        :param lifecycle: The lifecycle state of the component.
        :type lifecycle: str, optional

        :param tier: An entity reference to the owner of the component.
        :type tier: str, optional
        """
        if components is not unset:
            kwargs["components"] = components
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if tier is not unset:
            kwargs["tier"] = tier
        super().__init__(kwargs)
