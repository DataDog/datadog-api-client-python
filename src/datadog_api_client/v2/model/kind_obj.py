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


class KindObj(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "kind": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "displayName",
        "kind": "kind",
    }

    def __init__(
        self_,
        kind: str,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for kind.

        :param description: Short description of the kind.
        :type description: str, optional

        :param display_name: The display name of the kind. Automatically generated if not provided.
        :type display_name: str, optional

        :param kind: The name of the kind to create or update. This must be in kebab-case format.
        :type kind: str
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.kind = kind
