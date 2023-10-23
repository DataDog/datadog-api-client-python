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


class ContainerImageFlavor(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "built_at": (str,),
            "os_architecture": (str,),
            "os_name": (str,),
            "os_version": (str,),
            "size": (int,),
        }

    attribute_map = {
        "built_at": "built_at",
        "os_architecture": "os_architecture",
        "os_name": "os_name",
        "os_version": "os_version",
        "size": "size",
    }

    def __init__(
        self_,
        built_at: Union[str, UnsetType] = unset,
        os_architecture: Union[str, UnsetType] = unset,
        os_name: Union[str, UnsetType] = unset,
        os_version: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Container Image breakdown by supported platform.

        :param built_at: Time the platform-specific Container Image was built.
        :type built_at: str, optional

        :param os_architecture: Operating System architecture supported by the Container Image.
        :type os_architecture: str, optional

        :param os_name: Operating System name supported by the Container Image.
        :type os_name: str, optional

        :param os_version: Operating System version supported by the Container Image.
        :type os_version: str, optional

        :param size: Size of the platform-specific Container Image.
        :type size: int, optional
        """
        if built_at is not unset:
            kwargs["built_at"] = built_at
        if os_architecture is not unset:
            kwargs["os_architecture"] = os_architecture
        if os_name is not unset:
            kwargs["os_name"] = os_name
        if os_version is not unset:
            kwargs["os_version"] = os_version
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)
