# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ModelLabProjectArtifactsType(ModelSimple):
    """
    The JSON:API type for a project artifacts resource.

    :param value: If omitted defaults to "project_files". Must be one of ["project_files"].
    :type value: str
    """

    allowed_values = {
        "project_files",
    }
    PROJECT_FILES: ClassVar["ModelLabProjectArtifactsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ModelLabProjectArtifactsType.PROJECT_FILES = ModelLabProjectArtifactsType("project_files")
