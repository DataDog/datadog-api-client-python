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
    from datadog_api_client.v2.model.web_integration_account_schema_response_properties import (
        WebIntegrationAccountSchemaResponseProperties,
    )


class WebIntegrationAccountSchemaResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_schema_response_properties import (
            WebIntegrationAccountSchemaResponseProperties,
        )

        return {
            "_schema": (str,),
            "additional_properties": (bool,),
            "properties": (WebIntegrationAccountSchemaResponseProperties,),
            "required": ([str],),
            "type": (str,),
        }

    attribute_map = {
        "_schema": "$schema",
        "additional_properties": "additionalProperties",
        "properties": "properties",
        "required": "required",
        "type": "type",
    }

    def __init__(
        self_,
        _schema: str,
        properties: WebIntegrationAccountSchemaResponseProperties,
        required: List[str],
        type: str,
        additional_properties: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing the JSON schema for an integration's account configuration.
        This schema defines the required and optional fields for both settings and secrets,
        including field types, validation rules, and descriptions.

        The response is a standard `JSON Schema (draft-07) <https://json-schema.org/draft-07/schema#>`_ document describing the account
        configuration structure. Since this is a dynamic JSON Schema, the exact properties
        will vary by integration.

        :param _schema: The JSON Schema version URI.
        :type _schema: str

        :param additional_properties: Whether additional properties are allowed at the root level (typically false).
        :type additional_properties: bool, optional

        :param properties: The properties object containing settings and secrets schema definitions.
            Both are always present in every integration schema.
        :type properties: WebIntegrationAccountSchemaResponseProperties

        :param required: List of required top-level properties.
        :type required: [str]

        :param type: The root type of the schema (always "object").
        :type type: str
        """
        if additional_properties is not unset:
            kwargs["additional_properties"] = additional_properties
        super().__init__(kwargs)

        self_._schema = _schema
        self_.properties = properties
        self_.required = required
        self_.type = type
