# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_integration_schema_spec_property_v2 import (
        FleetIntegrationSchemaSpecPropertyV2,
    )


class FleetIntegrationSchemaSpecValueV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_spec_property_v2 import (
            FleetIntegrationSchemaSpecPropertyV2,
        )

        return {
            "additional_properties": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "any_of": ([FleetIntegrationSchemaSpecValueV2],),
            "default": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "description": (str,),
            "display_default": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "example": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "exclusive_maximum": (float,),
            "exclusive_minimum": (float,),
            "items": (FleetIntegrationSchemaSpecValueV2,),
            "max_length": (int,),
            "maximum": (float,),
            "min_length": (int,),
            "minimum": (float,),
            "pattern": (str,),
            "properties": ([FleetIntegrationSchemaSpecPropertyV2],),
            "secret": (bool,),
            "type": (str,),
        }

    attribute_map = {
        "additional_properties": "additionalProperties",
        "any_of": "anyOf",
        "default": "default",
        "description": "description",
        "display_default": "display_default",
        "example": "example",
        "exclusive_maximum": "exclusiveMaximum",
        "exclusive_minimum": "exclusiveMinimum",
        "items": "items",
        "max_length": "maxLength",
        "maximum": "maximum",
        "min_length": "minLength",
        "minimum": "minimum",
        "pattern": "pattern",
        "properties": "properties",
        "secret": "secret",
        "type": "type",
    }

    def __init__(
        self_,
        additional_properties: Union[Any, UnsetType] = unset,
        any_of: Union[List[FleetIntegrationSchemaSpecValueV2], UnsetType] = unset,
        default: Union[Any, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        display_default: Union[Any, UnsetType] = unset,
        example: Union[Any, UnsetType] = unset,
        exclusive_maximum: Union[float, UnsetType] = unset,
        exclusive_minimum: Union[float, UnsetType] = unset,
        items: Union[FleetIntegrationSchemaSpecValueV2, UnsetType] = unset,
        max_length: Union[int, UnsetType] = unset,
        maximum: Union[float, UnsetType] = unset,
        min_length: Union[int, UnsetType] = unset,
        minimum: Union[float, UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        properties: Union[List[FleetIntegrationSchemaSpecPropertyV2], UnsetType] = unset,
        secret: Union[bool, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON Schema-like specification for a configuration value.

        Object-typed values always include a ``properties`` array, even when empty.
        Non-object-typed values never include ``properties``. Throughout this schema,
        an empty array is meaningfully different from an absent field.

        Three further JSON Schema keywords can appear directly on this object but are
        not listed among its properties below to avoid clashing with this document's
        own schema composition keywords: ``enum`` (an array of allowed values, present
        only when there are enum constraints), ``required`` (an array of required
        property names, present only when ``type`` is ``object`` ), and ``oneOf`` (an array
        of exclusive alternative value specifications this value can match, present
        only when there are alternatives).

        :param additional_properties: Whether, or which, additional properties are allowed on the object. Can be a boolean or a nested schema. Present only when ``type`` is ``object``.
        :type additional_properties: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param any_of: Alternative value specifications this value can match. Absent when none apply.
        :type any_of: [FleetIntegrationSchemaSpecValueV2], optional

        :param default: The default value. Can be any JSON type. Absent when not set.
        :type default: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param description: A human-readable description of the value. Absent when not set.
        :type description: str, optional

        :param display_default: A legacy, display-formatted representation of the default value. Can be any JSON type. Absent when not set.
        :type display_default: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param example: An example value. Can be any JSON type. Absent when not set.
        :type example: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param exclusive_maximum: The maximum allowed numeric value, exclusive. Absent when not set.
        :type exclusive_maximum: float, optional

        :param exclusive_minimum: The minimum allowed numeric value, exclusive. Absent when not set.
        :type exclusive_minimum: float, optional

        :param items: A JSON Schema-like specification for a configuration value.

            Object-typed values always include a ``properties`` array, even when empty.
            Non-object-typed values never include ``properties``. Throughout this schema,
            an empty array is meaningfully different from an absent field.

            Three further JSON Schema keywords can appear directly on this object but are
            not listed among its properties below to avoid clashing with this document's
            own schema composition keywords: ``enum`` (an array of allowed values, present
            only when there are enum constraints), ``required`` (an array of required
            property names, present only when ``type`` is ``object`` ), and ``oneOf`` (an array
            of exclusive alternative value specifications this value can match, present
            only when there are alternatives).
        :type items: FleetIntegrationSchemaSpecValueV2, optional

        :param max_length: The maximum allowed string length. Absent when not set.
        :type max_length: int, optional

        :param maximum: The maximum allowed numeric value, inclusive. Absent when not set.
        :type maximum: float, optional

        :param min_length: The minimum allowed string length. Absent when not set.
        :type min_length: int, optional

        :param minimum: The minimum allowed numeric value, inclusive. Absent when not set.
        :type minimum: float, optional

        :param pattern: A regular expression the string value must match. Absent when not set.
        :type pattern: str, optional

        :param properties: The object's declared properties. Present when ``type`` is ``object`` , including as an empty array when the object declares no properties. Absent for non-object types.
        :type properties: [FleetIntegrationSchemaSpecPropertyV2], optional

        :param secret: Whether the value is a secret that should be masked. Absent when not set.
        :type secret: bool, optional

        :param type: The JSON Schema type of the value, such as ``string`` or ``object``. Absent when not set.
        :type type: str, optional
        """
        if additional_properties is not unset:
            kwargs["additional_properties"] = additional_properties
        if any_of is not unset:
            kwargs["any_of"] = any_of
        if default is not unset:
            kwargs["default"] = default
        if description is not unset:
            kwargs["description"] = description
        if display_default is not unset:
            kwargs["display_default"] = display_default
        if example is not unset:
            kwargs["example"] = example
        if exclusive_maximum is not unset:
            kwargs["exclusive_maximum"] = exclusive_maximum
        if exclusive_minimum is not unset:
            kwargs["exclusive_minimum"] = exclusive_minimum
        if items is not unset:
            kwargs["items"] = items
        if max_length is not unset:
            kwargs["max_length"] = max_length
        if maximum is not unset:
            kwargs["maximum"] = maximum
        if min_length is not unset:
            kwargs["min_length"] = min_length
        if minimum is not unset:
            kwargs["minimum"] = minimum
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if properties is not unset:
            kwargs["properties"] = properties
        if secret is not unset:
            kwargs["secret"] = secret
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
