# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes_resource import (
        CIAppCreatePipelineEventRequestAttributesResource,
    )
    from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline import CIAppPipelineEventPipeline
    from datadog_api_client.v2.model.ci_app_pipeline_event_stage import CIAppPipelineEventStage
    from datadog_api_client.v2.model.ci_app_pipeline_event_job import CIAppPipelineEventJob
    from datadog_api_client.v2.model.ci_app_pipeline_event_step import CIAppPipelineEventStep


class CIAppCreatePipelineEventRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes_resource import (
            CIAppCreatePipelineEventRequestAttributesResource,
        )

        return {
            "env": (str,),
            "resource": (CIAppCreatePipelineEventRequestAttributesResource,),
            "service": (str,),
        }

    attribute_map = {
        "env": "env",
        "resource": "resource",
        "service": "service",
    }

    def __init__(
        self_,
        resource: Union[
            CIAppCreatePipelineEventRequestAttributesResource,
            CIAppPipelineEventPipeline,
            CIAppPipelineEventStage,
            CIAppPipelineEventJob,
            CIAppPipelineEventStep,
        ],
        env: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the pipeline event to create.

        :param env: The Datadog environment.
        :type env: str, optional

        :param resource: Details of the CI pipeline event.
        :type resource: CIAppCreatePipelineEventRequestAttributesResource

        :param service: If the CI provider is SaaS, use this to differentiate between instances.
        :type service: str, optional
        """
        if env is not unset:
            kwargs["env"] = env
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)

        self_.resource = resource
