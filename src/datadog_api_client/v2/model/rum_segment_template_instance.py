# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RumSegmentTemplateInstance(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "parameters": ({str: (str,)},),
            "template_id": (str,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "parameters": "parameters",
        "template_id": "template_id",
        "to": "to",
    }

    def __init__(
        self_,
        template_id: str,
        _from: Union[int, UnsetType] = unset,
        parameters: Union[Dict[str, str], UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A template-based query block within a segment data query.

        :param _from: The start of the time range in milliseconds since epoch.
        :type _from: int, optional

        :param parameters: The template parameters as key-value pairs.
        :type parameters: {str: (str,)}, optional

        :param template_id: The identifier of the template.
        :type template_id: str

        :param to: The end of the time range in milliseconds since epoch.
        :type to: int, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if parameters is not unset:
            kwargs["parameters"] = parameters
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)

        self_.template_id = template_id
