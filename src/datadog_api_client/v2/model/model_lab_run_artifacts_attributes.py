# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.model_lab_artifact_object_info import ModelLabArtifactObjectInfo


class ModelLabRunArtifactsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_artifact_object_info import ModelLabArtifactObjectInfo

        return {
            "files": ([ModelLabArtifactObjectInfo],),
            "path_in_project": (str,),
        }

    attribute_map = {
        "files": "files",
        "path_in_project": "path_in_project",
    }

    def __init__(self_, files: List[ModelLabArtifactObjectInfo], path_in_project: str, **kwargs):
        """
        Artifact listing for a Model Lab run.

        :param files: The list of artifact files and directories.
        :type files: [ModelLabArtifactObjectInfo]

        :param path_in_project: The path of the run's artifacts relative to the project's artifact root.
        :type path_in_project: str
        """
        super().__init__(kwargs)

        self_.files = files
        self_.path_in_project = path_in_project
