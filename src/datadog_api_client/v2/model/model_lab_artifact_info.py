# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class ModelLabArtifactInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "artifact_path": (str,),
            "created_at": (datetime,),
            "file_size": (int, none_type),
            "filename": (str,),
        }

    attribute_map = {
        "artifact_path": "artifact_path",
        "created_at": "created_at",
        "file_size": "file_size",
        "filename": "filename",
    }

    def __init__(
        self_,
        artifact_path: str,
        created_at: datetime,
        filename: str,
        file_size: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about a project-level artifact file.

        :param artifact_path: The full artifact path relative to the project's artifact root.
        :type artifact_path: str

        :param created_at: The date and time the artifact was created.
        :type created_at: datetime

        :param file_size: The size of the file in bytes.
        :type file_size: int, none_type, optional

        :param filename: The filename of the artifact.
        :type filename: str
        """
        if file_size is not unset:
            kwargs["file_size"] = file_size
        super().__init__(kwargs)

        self_.artifact_path = artifact_path
        self_.created_at = created_at
        self_.filename = filename
