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


class EntityV3APISpecInterfaceDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "definition": (dict,),
        }

    attribute_map = {
        "definition": "definition",
    }

    def __init__(self_, definition: Union[dict, UnsetType] = unset, **kwargs):
        """
        The definition of ``EntityV3APISpecInterfaceDefinition`` object.

        :param definition: The API definition.
        :type definition: dict, optional
        """
        if definition is not unset:
            kwargs["definition"] = definition
        super().__init__(kwargs)
