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


class CustomFrameworkDataHandleAndVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "id": (str,),
            "version": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "id": "id",
        "version": "version",
    }

    def __init__(
        self_,
        handle: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Framework Handle and Version.

        :param handle: Framework Handle
        :type handle: str, optional

        :param id: Framework ID
        :type id: str, optional

        :param version: Framework Version
        :type version: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if id is not unset:
            kwargs["id"] = id
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
