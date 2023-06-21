# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import (
        CIAppCreatePipelineEventRequestData,
    )
    from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes_resource import (
        CIAppCreatePipelineEventRequestAttributesResource,
    )
    from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline import CIAppPipelineEventPipeline
    from datadog_api_client.v2.model.ci_app_pipeline_event_stage import CIAppPipelineEventStage
    from datadog_api_client.v2.model.ci_app_pipeline_event_job import CIAppPipelineEventJob
    from datadog_api_client.v2.model.ci_app_pipeline_event_step import CIAppPipelineEventStep


@dataclass
class CIAppCreatePipelineEventRequestJSON:
    env: Union[str, UnsetType] = unset
    resource: Union[
        CIAppCreatePipelineEventRequestAttributesResource,
        CIAppPipelineEventPipeline,
        CIAppPipelineEventStage,
        CIAppPipelineEventJob,
        CIAppPipelineEventStep,
        UnsetType,
    ] = unset
    service: Union[str, UnsetType] = unset


class CIAppCreatePipelineEventRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import (
            CIAppCreatePipelineEventRequestData,
        )

        return {
            "data": (CIAppCreatePipelineEventRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = CIAppCreatePipelineEventRequestJSON

    def __init__(self_, data: Union[CIAppCreatePipelineEventRequestData, UnsetType] = unset, **kwargs):
        """
        Request object.

        :param data: Data of the pipeline event to create.
        :type data: CIAppCreatePipelineEventRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
