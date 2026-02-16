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


class CycloneDXToolComponent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: Union[str, UnsetType] = unset, **kwargs):
        """
        Tool component that detected the vulnerabilities.

        :param name: The name of the tool.
        :type name: str

        :param type: The type of the tool.
        :type type: str, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
