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
    from datadog_api_client.v2.model.model_lab_run_artifacts_attributes import ModelLabRunArtifactsAttributes
    from datadog_api_client.v2.model.model_lab_run_artifacts_type import ModelLabRunArtifactsType


class ModelLabRunArtifactsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_run_artifacts_attributes import ModelLabRunArtifactsAttributes
        from datadog_api_client.v2.model.model_lab_run_artifacts_type import ModelLabRunArtifactsType

        return {
            "attributes": (ModelLabRunArtifactsAttributes,),
            "id": (str,),
            "type": (ModelLabRunArtifactsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ModelLabRunArtifactsAttributes, id: str, type: ModelLabRunArtifactsType, **kwargs):
        """
        A run artifacts JSON:API resource object.

        :param attributes: Artifact listing for a Model Lab run.
        :type attributes: ModelLabRunArtifactsAttributes

        :param id: The unique identifier of the artifacts resource.
        :type id: str

        :param type: The JSON:API type for a run artifacts resource.
        :type type: ModelLabRunArtifactsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
