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
    from datadog_api_client.v2.model.fleet_integration_schema_deprecation_v2 import FleetIntegrationSchemaDeprecationV2
    from datadog_api_client.v2.model.fleet_integration_schema_spec_value_v2 import FleetIntegrationSchemaSpecValueV2


class FleetIntegrationSchemaSpecOptionV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_deprecation_v2 import (
            FleetIntegrationSchemaDeprecationV2,
        )
        from datadog_api_client.v2.model.fleet_integration_schema_spec_value_v2 import FleetIntegrationSchemaSpecValueV2

        return {
            "deprecation": (FleetIntegrationSchemaDeprecationV2,),
            "description": (str,),
            "display_priority": (int,),
            "enabled": (bool,),
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
            "hidden": (bool,),
            "metadata_tags": ([str],),
            "multiple": (bool,),
            "multiple_instances_defined": (bool,),
            "name": (str,),
            "options": ([FleetIntegrationSchemaSpecOptionV2],),
            "prefill": (
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
            "required": (bool,),
            "secret": (bool,),
            "value": (FleetIntegrationSchemaSpecValueV2,),
        }

    attribute_map = {
        "deprecation": "deprecation",
        "description": "description",
        "display_priority": "display_priority",
        "enabled": "enabled",
        "example": "example",
        "hidden": "hidden",
        "metadata_tags": "metadata_tags",
        "multiple": "multiple",
        "multiple_instances_defined": "multiple_instances_defined",
        "name": "name",
        "options": "options",
        "prefill": "prefill",
        "required": "required",
        "secret": "secret",
        "value": "value",
    }

    def __init__(
        self_,
        deprecation: Union[FleetIntegrationSchemaDeprecationV2, none_type],
        description: str,
        display_priority: int,
        enabled: bool,
        hidden: bool,
        metadata_tags: List[str],
        multiple: bool,
        multiple_instances_defined: bool,
        name: str,
        required: bool,
        example: Union[Any, UnsetType] = unset,
        options: Union[List[FleetIntegrationSchemaSpecOptionV2], UnsetType] = unset,
        prefill: Union[Any, UnsetType] = unset,
        secret: Union[bool, UnsetType] = unset,
        value: Union[FleetIntegrationSchemaSpecValueV2, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single configuration option within an integration's configuration file.

        :param deprecation: Deprecation information for a configuration option. Currently carries no fields and is always emitted as an empty object or ``null``.
        :type deprecation: FleetIntegrationSchemaDeprecationV2, none_type

        :param description: A human-readable description of the option.
        :type description: str

        :param display_priority: The display order priority of the option relative to other options.
        :type display_priority: int

        :param enabled: Whether the option is enabled by default.
        :type enabled: bool

        :param example: An example value for the option. Can be any JSON type. Absent from the response when not set.
        :type example: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param hidden: Whether the option is hidden from the default configuration UI.
        :type hidden: bool

        :param metadata_tags: Metadata tags associated with the option. Returned as an empty array when the option has no tags.
        :type metadata_tags: [str]

        :param multiple: Whether the option accepts multiple values.
        :type multiple: bool

        :param multiple_instances_defined: Whether multiple instances of this option are defined in the configuration file.
        :type multiple_instances_defined: bool

        :param name: The option name.
        :type name: str

        :param options: Nested options. Absent from the response when the option has no nested options.
        :type options: [FleetIntegrationSchemaSpecOptionV2], optional

        :param prefill: A prefill value for the option. Can be any JSON type. Absent from the response when not set.
        :type prefill: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param required: Whether the option is required.
        :type required: bool

        :param secret: Whether the option is a secret that should be masked. Absent from the response when not set, distinct from being explicitly set to ``false``.
        :type secret: bool, optional

        :param value: A JSON Schema-like specification for a configuration value.

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
        :type value: FleetIntegrationSchemaSpecValueV2, optional
        """
        if example is not unset:
            kwargs["example"] = example
        if options is not unset:
            kwargs["options"] = options
        if prefill is not unset:
            kwargs["prefill"] = prefill
        if secret is not unset:
            kwargs["secret"] = secret
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.deprecation = deprecation
        self_.description = description
        self_.display_priority = display_priority
        self_.enabled = enabled
        self_.hidden = hidden
        self_.metadata_tags = metadata_tags
        self_.multiple = multiple
        self_.multiple_instances_defined = multiple_instances_defined
        self_.name = name
        self_.required = required
