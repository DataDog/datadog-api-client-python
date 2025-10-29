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


class SankeyRequestDataAttributesSearchOccurrences(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "meta": ({str: (str,)},),
            "operator": (str,),
            "value": (str,),
        }

    attribute_map = {
        "meta": "meta",
        "operator": "operator",
        "value": "value",
    }

    def __init__(self_, operator: str, value: str, meta: Union[Dict[str, str], UnsetType] = unset, **kwargs):
        """


        :param meta:
        :type meta: {str: (str,)}, optional

        :param operator:
        :type operator: str

        :param value:
        :type value: str
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.operator = operator
        self_.value = value
