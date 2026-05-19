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
    from datadog_api_client.v2.model.model_lab_run_artifacts_data import ModelLabRunArtifactsData


class ModelLabRunArtifactsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_run_artifacts_data import ModelLabRunArtifactsData

        return {
            "data": (ModelLabRunArtifactsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ModelLabRunArtifactsData, **kwargs):
        """
        Response containing the artifact listing for a Model Lab run.

        :param data: A run artifacts JSON:API resource object.
        :type data: ModelLabRunArtifactsData
        """
        super().__init__(kwargs)

        self_.data = data
