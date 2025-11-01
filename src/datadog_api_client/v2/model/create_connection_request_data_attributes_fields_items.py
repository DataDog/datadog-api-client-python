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


        :param description:
        :type description: str, optional

        :param display_name:
        :type display_name: str, optional

        :param groups:
        :type groups: [str], optional

        :param id:
        :type id: str

        :param source_name:
        :type source_name: str

        :param type:
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
