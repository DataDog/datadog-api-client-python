# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.value_type import ValueType
    from datadog_api_client.v2.model.create_variant import CreateVariant


class CreateFeatureFlagAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.value_type import ValueType
        from datadog_api_client.v2.model.create_variant import CreateVariant

        return {
            "default_variant_key": (str, none_type),
            "description": (str,),
            "json_schema": (str, none_type),
            "key": (str,),
            "name": (str,),
            "value_type": (ValueType,),
            "variants": ([CreateVariant],),
        }

    attribute_map = {
        "default_variant_key": "default_variant_key",
        "description": "description",
        "json_schema": "json_schema",
        "key": "key",
        "name": "name",
        "value_type": "value_type",
        "variants": "variants",
    }

    def __init__(
        self_,
        description: str,
        key: str,
        name: str,
        value_type: ValueType,
        variants: List[CreateVariant],
        default_variant_key: Union[str, none_type, UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new feature flag.

        :param default_variant_key: The key of the default variant.
        :type default_variant_key: str, none_type, optional

        :param description: The description of the feature flag.
        :type description: str

        :param json_schema: JSON schema for validation when value_type is JSON.
        :type json_schema: str, none_type, optional

        :param key: The unique key of the feature flag.
        :type key: str

        :param name: The name of the feature flag.
        :type name: str

        :param value_type: The type of values for the feature flag variants.
        :type value_type: ValueType

        :param variants: The variants of the feature flag.
        :type variants: [CreateVariant]
        """
        if default_variant_key is not unset:
            kwargs["default_variant_key"] = default_variant_key
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        super().__init__(kwargs)

        self_.description = description
        self_.key = key
        self_.name = name
        self_.value_type = value_type
        self_.variants = variants
