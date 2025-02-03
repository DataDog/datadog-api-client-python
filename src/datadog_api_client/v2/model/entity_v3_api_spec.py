# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_v3_api_spec_interface import EntityV3APISpecInterface
    from datadog_api_client.v2.model.entity_v3_api_spec_interface_file_ref import EntityV3APISpecInterfaceFileRef
    from datadog_api_client.v2.model.entity_v3_api_spec_interface_definition import EntityV3APISpecInterfaceDefinition


class EntityV3APISpec(ModelNormal):
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
        from datadog_api_client.v2.model.entity_v3_api_spec_interface import EntityV3APISpecInterface

        return {
            "implemented_by": ([str],),
            "interface": (EntityV3APISpecInterface,),
            "lifecycle": (str,),
            "tier": (str,),
            "type": (str,),
        }

    attribute_map = {
        "implemented_by": "implementedBy",
        "interface": "interface",
        "lifecycle": "lifecycle",
        "tier": "tier",
        "type": "type",
    }

    def __init__(
        self_,
        implemented_by: Union[List[str], UnsetType] = unset,
        interface: Union[
            EntityV3APISpecInterface, EntityV3APISpecInterfaceFileRef, EntityV3APISpecInterfaceDefinition, UnsetType
        ] = unset,
        lifecycle: Union[str, UnsetType] = unset,
        tier: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 API Spec object.

        :param implemented_by: Services which implemented the API.
        :type implemented_by: [str], optional

        :param interface: The API definition.
        :type interface: EntityV3APISpecInterface, optional

        :param lifecycle: The lifecycle state of the component.
        :type lifecycle: str, optional

        :param tier: The importance of the component.
        :type tier: str, optional

        :param type: The type of API.
        :type type: str, optional
        """
        if implemented_by is not unset:
            kwargs["implemented_by"] = implemented_by
        if interface is not unset:
            kwargs["interface"] = interface
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if tier is not unset:
            kwargs["tier"] = tier
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
