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


class EntityV3DatastoreSpec(ModelNormal):
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
            "lifecycle": (str,),
            "tier": (str,),
            "type": (str,),
        }

    attribute_map = {
        "lifecycle": "lifecycle",
        "tier": "tier",
        "type": "type",
    }

    def __init__(
        self_,
        lifecycle: Union[str, UnsetType] = unset,
        tier: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 Datastore Spec object.

        :param lifecycle: The lifecycle state of the datastore.
        :type lifecycle: str, optional

        :param tier: The importance of the datastore.
        :type tier: str, optional

        :param type: The type of datastore.
        :type type: str, optional
        """
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if tier is not unset:
            kwargs["tier"] = tier
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
