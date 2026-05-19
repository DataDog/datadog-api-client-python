# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ModelLabArtifactObjectInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file_size": (int, none_type),
            "is_dir": (bool,),
            "path": (str,),
        }

    attribute_map = {
        "file_size": "file_size",
        "is_dir": "is_dir",
        "path": "path",
    }

    def __init__(self_, is_dir: bool, path: str, file_size: Union[int, none_type, UnsetType] = unset, **kwargs):
        """
        Information about an artifact file or directory within a run.

        :param file_size: The size of the file in bytes.
        :type file_size: int, none_type, optional

        :param is_dir: Whether this artifact entry is a directory.
        :type is_dir: bool

        :param path: The path of the artifact relative to the run's artifact root.
        :type path: str
        """
        if file_size is not unset:
            kwargs["file_size"] = file_size
        super().__init__(kwargs)

        self_.is_dir = is_dir
        self_.path = path
