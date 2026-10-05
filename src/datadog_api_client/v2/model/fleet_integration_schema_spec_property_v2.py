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
    from datadog_api_client.v2.model.fleet_integration_schema_spec_value_v2 import FleetIntegrationSchemaSpecValueV2


class FleetIntegrationSchemaSpecPropertyV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_spec_value_v2 import FleetIntegrationSchemaSpecValueV2

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
            "items": (FleetIntegrationSchemaSpecValueV2,),
            "name": (str,),
            "properties": ([FleetIntegrationSchemaSpecPropertyV2],),
            "type": (str,),
        }

    attribute_map = {
        "additional_properties": "additionalProperties",
        "any_of": "anyOf",
        "items": "items",
        "name": "name",
        "properties": "properties",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        additional_properties: Union[Any, UnsetType] = unset,
        any_of: Union[List[FleetIntegrationSchemaSpecValueV2], UnsetType] = unset,
        items: Union[FleetIntegrationSchemaSpecValueV2, UnsetType] = unset,
        properties: Union[List[FleetIntegrationSchemaSpecPropertyV2], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A property of an object-typed configuration value. A ``oneOf`` keyword (an array of exclusive alternative value specifications this property can match) can appear directly on this object when alternatives apply.

        :param additional_properties: Whether, or which, additional properties are allowed on the object. Can be a boolean or a nested schema. Present only when ``type`` is ``object``.
        :type additional_properties: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param any_of: Alternative value specifications this property can match. Absent when none apply.
        :type any_of: [FleetIntegrationSchemaSpecValueV2], optional

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

        :param name: The property name.
        :type name: str

        :param properties: Nested properties. Present only when ``type`` is ``object`` and the object declares properties.
        :type properties: [FleetIntegrationSchemaSpecPropertyV2], optional

        :param type: The JSON Schema type of the property, such as ``string`` or ``boolean``. Absent when not set.
        :type type: str, optional
        """
        if additional_properties is not unset:
            kwargs["additional_properties"] = additional_properties
        if any_of is not unset:
            kwargs["any_of"] = any_of
        if items is not unset:
            kwargs["items"] = items
        if properties is not unset:
            kwargs["properties"] = properties
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
