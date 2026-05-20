# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

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


class LLMObsSpanToolDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "schema": (
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
            "version": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "schema": "schema",
        "version": "version",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        schema: Union[Dict[str, Any], UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tool definition available to an LLM span.

        :param description: Description of what the tool does.
        :type description: str, optional

        :param name: Name of the tool.
        :type name: str, optional

        :param schema: JSON schema describing the tool's input parameters.
        :type schema: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param version: Version of the tool definition.
        :type version: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if schema is not unset:
            kwargs["schema"] = schema
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
