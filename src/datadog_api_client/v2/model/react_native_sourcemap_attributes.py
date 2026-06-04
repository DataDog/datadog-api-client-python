# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ReactNativeSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "build_number": (str,),
            "bundle_name": (str,),
            "bundle_version": (str,),
            "created_at": (datetime,),
            "debug_id": (str,),
            "mapkind": (str,),
            "platform": (str,),
            "service": (str,),
            "size": (int,),
            "version": (str,),
        }

    attribute_map = {
        "build_number": "build_number",
        "bundle_name": "bundle_name",
        "bundle_version": "bundle_version",
        "created_at": "created_at",
        "debug_id": "debug_id",
        "mapkind": "mapkind",
        "platform": "platform",
        "service": "service",
        "size": "size",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: str,
        size: int,
        build_number: Union[str, UnsetType] = unset,
        bundle_name: Union[str, UnsetType] = unset,
        bundle_version: Union[str, UnsetType] = unset,
        debug_id: Union[str, UnsetType] = unset,
        platform: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a React Native source map.

        :param build_number: The build number.
        :type build_number: str, optional

        :param bundle_name: The bundle name.
        :type bundle_name: str, optional

        :param bundle_version: The bundle version.
        :type bundle_version: str, optional

        :param created_at: The timestamp when the source map was created.
        :type created_at: datetime

        :param debug_id: The debug identifier (UUID format).
        :type debug_id: str, optional

        :param mapkind: The type of source map.
        :type mapkind: str

        :param platform: The platform the source map was built for (e.g., ``ios`` , ``android`` ).
        :type platform: str, optional

        :param service: The service name associated with the source map.
        :type service: str, optional

        :param size: The size of the source map file in bytes.
        :type size: int

        :param version: The version of the service associated with the source map.
        :type version: str, optional
        """
        if build_number is not unset:
            kwargs["build_number"] = build_number
        if bundle_name is not unset:
            kwargs["bundle_name"] = bundle_name
        if bundle_version is not unset:
            kwargs["bundle_version"] = bundle_version
        if debug_id is not unset:
            kwargs["debug_id"] = debug_id
        if platform is not unset:
            kwargs["platform"] = platform
        if service is not unset:
            kwargs["service"] = service
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size
