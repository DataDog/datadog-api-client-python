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


class LLMObsInferenceFunction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "parameters": (
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
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "parameters": "parameters",
    }

    def __init__(self_, name: str, parameters: Dict[str, Any], description: Union[str, UnsetType] = unset, **kwargs):
        """
        A function definition for a tool available to the model.

        :param description: A description of what the function does.
        :type description: str, optional

        :param name: The name of the function.
        :type name: str

        :param parameters: JSON schema describing the function parameters.
        :type parameters: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.name = name
        self_.parameters = parameters
