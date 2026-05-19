# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.model_lab_project_artifacts_attributes import ModelLabProjectArtifactsAttributes
    from datadog_api_client.v2.model.model_lab_project_artifacts_type import ModelLabProjectArtifactsType


class ModelLabProjectArtifactsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_project_artifacts_attributes import (
            ModelLabProjectArtifactsAttributes,
        )
        from datadog_api_client.v2.model.model_lab_project_artifacts_type import ModelLabProjectArtifactsType

        return {
            "attributes": (ModelLabProjectArtifactsAttributes,),
            "id": (str,),
            "type": (ModelLabProjectArtifactsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ModelLabProjectArtifactsAttributes, id: str, type: ModelLabProjectArtifactsType, **kwargs
    ):
        """
        A project artifacts JSON:API resource object.

        :param attributes: Artifact listing for a Model Lab project.
        :type attributes: ModelLabProjectArtifactsAttributes

        :param id: The unique identifier of the project artifacts resource.
        :type id: str

        :param type: The JSON:API type for a project artifacts resource.
        :type type: ModelLabProjectArtifactsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
