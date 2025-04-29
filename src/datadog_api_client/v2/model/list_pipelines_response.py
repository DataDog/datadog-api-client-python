# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_data import ObservabilityPipelineData
    from datadog_api_client.v2.model.list_pipelines_response_meta import ListPipelinesResponseMeta


class ListPipelinesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_data import ObservabilityPipelineData
        from datadog_api_client.v2.model.list_pipelines_response_meta import ListPipelinesResponseMeta

        return {
            "data": ([ObservabilityPipelineData],),
            "meta": (ListPipelinesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ObservabilityPipelineData],
        meta: Union[ListPipelinesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the response payload containing a list of pipelines and associated metadata.

        :param data: The ``schema`` ``data``.
        :type data: [ObservabilityPipelineData]

        :param meta: Metadata about the response.
        :type meta: ListPipelinesResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
