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


class Library(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "name": "name",
        "version": "version",
    }

    def __init__(self_, name: str, version: Union[str, UnsetType] = unset, **kwargs):
        """
        Vulnerability library.

        :param name: Vulnerability library name.
        :type name: str

        :param version: Vulnerability library version.
        :type version: str, optional
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.name = name
