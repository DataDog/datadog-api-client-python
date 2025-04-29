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
    from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData


class ObservabilityPipelineSpec(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_spec_data import ObservabilityPipelineSpecData

        return {
            "data": (ObservabilityPipelineSpecData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ObservabilityPipelineSpecData, **kwargs):
        """
        Input schema representing an observability pipeline configuration. Used in create and validate requests.

        :param data: Contains the the pipeline configuration.
        :type data: ObservabilityPipelineSpecData
        """
        super().__init__(kwargs)

        self_.data = data
