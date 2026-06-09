# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.form_data_definition_type import FormDataDefinitionType


class FormDataDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_definition_type import FormDataDefinitionType

        return {
            "description": (str,),
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
            "title": (str,),
            "type": (FormDataDefinitionType,),
        }

    attribute_map = {
        "description": "description",
        "properties": "properties",
        "required": "required",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        properties: Union[Dict[str, Any], UnsetType] = unset,
        required: Union[List[str], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        type: Union[FormDataDefinitionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON Schema definition that describes the form's data fields.

        :param description: A description shown to form respondents.
        :type description: str, optional

        :param properties: A map of field names to their JSON Schema definitions.
        :type properties: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param required: List of field names that must be answered.
        :type required: [str], optional

        :param title: The title of the form schema.
        :type title: str, optional

        :param type: The root schema type.
        :type type: FormDataDefinitionType, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if properties is not unset:
            kwargs["properties"] = properties
        if required is not unset:
            kwargs["required"] = required
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
