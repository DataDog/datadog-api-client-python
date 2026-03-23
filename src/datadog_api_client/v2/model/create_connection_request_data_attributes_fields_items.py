# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CreateConnectionRequestDataAttributesFieldsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "groups": ([str],),
            "id": (str,),
            "source_name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "groups": "groups",
        "id": "id",
        "source_name": "source_name",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        source_name: str,
        type: str,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        groups: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Definition of a custom attribute field to import from a data source connection.

        :param description: Human-readable explanation of what the field represents.
        :type description: str, optional

        :param display_name: The human-readable label for the field shown in the UI.
        :type display_name: str, optional

        :param groups: List of group labels used to categorize the field.
        :type groups: [str], optional

        :param id: The unique identifier for the field within the connection.
        :type id: str

        :param source_name: The name of the column or attribute in the source data system that maps to this field.
        :type source_name: str

        :param type: The data type of the field (for example, string or number).
        :type type: str
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if groups is not unset:
            kwargs["groups"] = groups
        super().__init__(kwargs)

        self_.id = id
        self_.source_name = source_name
        self_.type = type
