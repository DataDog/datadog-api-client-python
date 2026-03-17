# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.web_integration_account_schema_response_settings_field import (
        WebIntegrationAccountSchemaResponseSettingsField,
    )


class WebIntegrationAccountSchemaResponseSettingsObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_schema_response_settings_field import (
            WebIntegrationAccountSchemaResponseSettingsField,
        )

        return {
            "additional_properties": (bool,),
            "properties": ({str: (WebIntegrationAccountSchemaResponseSettingsField,)},),
            "required": ([str],),
            "type": (str,),
        }

    attribute_map = {
        "additional_properties": "additionalProperties",
        "properties": "properties",
        "required": "required",
        "type": "type",
    }

    def __init__(
        self_,
        additional_properties: Union[bool, UnsetType] = unset,
        properties: Union[Dict[str, WebIntegrationAccountSchemaResponseSettingsField], UnsetType] = unset,
        required: Union[List[str], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON Schema definition for the settings object.
        Contains integration-specific configuration fields such as account identifiers,
        feature toggles, and non-sensitive configuration options.

        :param additional_properties: Whether additional properties are allowed (typically false).
        :type additional_properties: bool, optional

        :param properties: The individual setting fields for this integration.
            Field names and types vary by integration.
        :type properties: {str: (WebIntegrationAccountSchemaResponseSettingsField,)}, optional

        :param required: List of required setting field names.
        :type required: [str], optional

        :param type: Always "object" for the settings container.
        :type type: str, optional
        """
        if additional_properties is not unset:
            kwargs["additional_properties"] = additional_properties
        if properties is not unset:
            kwargs["properties"] = properties
        if required is not unset:
            kwargs["required"] = required
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
