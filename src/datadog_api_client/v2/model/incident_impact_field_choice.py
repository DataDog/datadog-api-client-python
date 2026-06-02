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


class IncidentImpactFieldChoice(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "value": "value",
    }

    def __init__(self_, display_name: str, value: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        A choice option for a dropdown or multiselect impact field.

        :param description: The description of the choice.
        :type description: str, optional

        :param display_name: The display name of the choice.
        :type display_name: str

        :param value: The value of the choice.
        :type value: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.display_name = display_name
        self_.value = value
