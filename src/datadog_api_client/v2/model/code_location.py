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


class CodeLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file_path": (str,),
            "location": (str,),
            "method": (str,),
        }

    attribute_map = {
        "file_path": "file_path",
        "location": "location",
        "method": "method",
    }

    def __init__(
        self_, location: str, file_path: Union[str, UnsetType] = unset, method: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Code vulnerability location.

        :param file_path: Vulnerability location file path.
        :type file_path: str, optional

        :param location: Vulnerability extracted location.
        :type location: str

        :param method: Vulnerability location method.
        :type method: str, optional
        """
        if file_path is not unset:
            kwargs["file_path"] = file_path
        if method is not unset:
            kwargs["method"] = method
        super().__init__(kwargs)

        self_.location = location
