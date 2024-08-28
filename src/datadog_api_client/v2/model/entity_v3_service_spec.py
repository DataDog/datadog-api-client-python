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


class EntityV3ServiceSpec(ModelNormal):
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
            "depends_on": ([str],),
            "languages": ([str],),
            "lifecycle": (str,),
            "tier": (str,),
            "type": (str,),
        }

    attribute_map = {
        "depends_on": "dependsOn",
        "languages": "languages",
        "lifecycle": "lifecycle",
        "tier": "tier",
        "type": "type",
    }

    def __init__(
        self_,
        depends_on: Union[List[str], UnsetType] = unset,
        languages: Union[List[str], UnsetType] = unset,
        lifecycle: Union[str, UnsetType] = unset,
        tier: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 Service Spec object.

        :param depends_on: A list of components the service depends on
        :type depends_on: [str], optional

        :param languages: The service's programming language.
        :type languages: [str], optional

        :param lifecycle: The lifecycle state of the component.
        :type lifecycle: str, optional

        :param tier: The importance of the component
        :type tier: str, optional

        :param type: The type of service
        :type type: str, optional
        """
        if depends_on is not unset:
            kwargs["depends_on"] = depends_on
        if languages is not unset:
            kwargs["languages"] = languages
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if tier is not unset:
            kwargs["tier"] = tier
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
