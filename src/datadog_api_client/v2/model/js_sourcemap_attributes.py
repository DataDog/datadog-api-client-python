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


class JSSourcemapAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "absolute_path": (str,),
            "blob_storage_sourcemap_path": (str,),
            "build_id": (str,),
            "created_at": (datetime,),
            "domain": (str,),
            "file_name": (str,),
            "mapkind": (str,),
            "service": (str,),
            "size": (int,),
            "variant": (str,),
            "version": (str,),
            "version_code": (str,),
        }

    attribute_map = {
        "absolute_path": "absolute_path",
        "blob_storage_sourcemap_path": "blob_storage_sourcemap_path",
        "build_id": "build_id",
        "created_at": "created_at",
        "domain": "domain",
        "file_name": "file_name",
        "mapkind": "mapkind",
        "service": "service",
        "size": "size",
        "variant": "variant",
        "version": "version",
        "version_code": "version_code",
    }

    def __init__(
        self_,
        created_at: datetime,
        mapkind: str,
        size: int,
        absolute_path: Union[str, UnsetType] = unset,
        blob_storage_sourcemap_path: Union[str, UnsetType] = unset,
        build_id: Union[str, UnsetType] = unset,
        domain: Union[str, UnsetType] = unset,
        file_name: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        variant: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        version_code: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a JavaScript source map.

        :param absolute_path: The absolute path to the minified JavaScript file.
        :type absolute_path: str, optional

        :param blob_storage_sourcemap_path: The path to the source map in blob storage.
        :type blob_storage_sourcemap_path: str, optional

        :param build_id: The build identifier.
        :type build_id: str, optional

        :param created_at: The timestamp when the source map was created.
        :type created_at: datetime

        :param domain: The domain associated with the source map.
        :type domain: str, optional

        :param file_name: The file name of the minified JavaScript file.
        :type file_name: str, optional

        :param mapkind: The type of source map.
        :type mapkind: str

        :param service: The service name associated with the source map.
        :type service: str, optional

        :param size: The size of the source map file in bytes.
        :type size: int

        :param variant: The source map variant.
        :type variant: str, optional

        :param version: The version of the service associated with the source map.
        :type version: str, optional

        :param version_code: The version code.
        :type version_code: str, optional
        """
        if absolute_path is not unset:
            kwargs["absolute_path"] = absolute_path
        if blob_storage_sourcemap_path is not unset:
            kwargs["blob_storage_sourcemap_path"] = blob_storage_sourcemap_path
        if build_id is not unset:
            kwargs["build_id"] = build_id
        if domain is not unset:
            kwargs["domain"] = domain
        if file_name is not unset:
            kwargs["file_name"] = file_name
        if service is not unset:
            kwargs["service"] = service
        if variant is not unset:
            kwargs["variant"] = variant
        if version is not unset:
            kwargs["version"] = version
        if version_code is not unset:
            kwargs["version_code"] = version_code
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.mapkind = mapkind
        self_.size = size
