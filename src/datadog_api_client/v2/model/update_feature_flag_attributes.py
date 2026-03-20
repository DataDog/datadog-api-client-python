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


class UpdateFeatureFlagAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "json_schema": (str, none_type),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "json_schema": "json_schema",
        "name": "name",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a feature flag.

        :param description: The description of the feature flag.
        :type description: str, optional

        :param json_schema: JSON schema for validation when value_type is JSON.
        :type json_schema: str, none_type, optional

        :param name: The name of the feature flag.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
