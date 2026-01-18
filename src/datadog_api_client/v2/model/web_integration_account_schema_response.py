# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

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


class WebIntegrationAccountSchemaResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_schema": (str,),
            "properties": (
                {
                    str: (
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
                    )
                },
            ),
            "required": ([str],),
            "type": (str,),
        }

    attribute_map = {
        "_schema": "$schema",
        "properties": "properties",
        "required": "required",
        "type": "type",
    }

    def __init__(
        self_,
        _schema: Union[str, UnsetType] = unset,
        properties: Union[Dict[str, Any], UnsetType] = unset,
        required: Union[List[str], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
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
        :type _schema: str, optional

        :param properties: The schema properties definition containing ``settings`` and ``secrets`` objects.
            Each property includes type information, validation rules, and descriptions.
        :type properties: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param required: List of required top-level properties.
        :type required: [str], optional

        :param type: The root type of the schema (always "object").
        :type type: str, optional
        """
        if _schema is not unset:
            kwargs["_schema"] = _schema
        if properties is not unset:
            kwargs["properties"] = properties
        if required is not unset:
            kwargs["required"] = required
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
