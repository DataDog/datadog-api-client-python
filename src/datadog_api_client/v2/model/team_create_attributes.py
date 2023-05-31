# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TeamCreateAttributes(ModelNormal):
    validations = {
        "handle": {
            "max_length": 195,
        },
        "name": {
            "max_length": 200,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "handle": "handle",
        "name": "name",
    }

    def __init__(self_, handle: str, name: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Team creation attributes

        :param description: Free-form markdown description/content for the team's homepage
        :type description: str, optional

        :param handle: The team's identifier
        :type handle: str

        :param name: The name of the team
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
