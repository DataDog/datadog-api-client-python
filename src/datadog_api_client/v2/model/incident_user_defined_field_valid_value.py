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


class IncidentUserDefinedFieldValidValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "short_description": (str,),
            "value": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "short_description": "short_description",
        "value": "value",
    }

    def __init__(
        self_,
        description: str,
        display_name: str,
        value: str,
        short_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A valid value for an incident user-defined field.

        :param description: A detailed description of the valid value.
        :type description: str

        :param display_name: The human-readable display name for this value.
        :type display_name: str

        :param short_description: A short description of the valid value.
        :type short_description: str, optional

        :param value: The machine-readable value stored when this option is selected.
        :type value: str
        """
        if short_description is not unset:
            kwargs["short_description"] = short_description
        super().__init__(kwargs)

        self_.description = description
        self_.display_name = display_name
        self_.value = value
