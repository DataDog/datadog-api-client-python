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


class PowerpackTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "defaults": ([str],),
            "name": (str,),
        }

    attribute_map = {
        "defaults": "defaults",
        "name": "name",
    }

    def __init__(self_, name: str, defaults: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Powerpack template variables.

        :param defaults: One or many template variable default values within the saved view, which are unioned together using ``OR`` if more than one is specified.
        :type defaults: [str], optional

        :param name: The name of the variable.
        :type name: str
        """
        if defaults is not unset:
            kwargs["defaults"] = defaults
        super().__init__(kwargs)

        self_.name = name
