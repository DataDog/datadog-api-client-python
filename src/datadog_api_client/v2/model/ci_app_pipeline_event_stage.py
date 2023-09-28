# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_ci_error import CIAppCIError
    from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
    from datadog_api_client.v2.model.ci_app_pipeline_event_stage_level import CIAppPipelineEventStageLevel
    from datadog_api_client.v2.model.ci_app_host_info import CIAppHostInfo
    from datadog_api_client.v2.model.ci_app_pipeline_event_parameters import CIAppPipelineEventParameters
    from datadog_api_client.v2.model.ci_app_pipeline_event_stage_status import CIAppPipelineEventStageStatus


class CIAppPipelineEventStage(ModelNormal):
    validations = {
        "queue_time": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_ci_error import CIAppCIError
        from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
        from datadog_api_client.v2.model.ci_app_pipeline_event_stage_level import CIAppPipelineEventStageLevel
        from datadog_api_client.v2.model.ci_app_host_info import CIAppHostInfo
        from datadog_api_client.v2.model.ci_app_pipeline_event_parameters import CIAppPipelineEventParameters
        from datadog_api_client.v2.model.ci_app_pipeline_event_stage_status import CIAppPipelineEventStageStatus

        return {
            "dependencies": ([str], none_type),
            "end": (datetime,),
            "error": (CIAppCIError,),
            "git": (CIAppGitInfo,),
            "id": (str,),
            "level": (CIAppPipelineEventStageLevel,),
            "metrics": ([str],),
            "name": (str,),
            "node": (CIAppHostInfo,),
            "parameters": (CIAppPipelineEventParameters,),
            "pipeline_name": (str,),
            "pipeline_unique_id": (str,),
            "queue_time": (int, none_type),
            "start": (datetime,),
            "status": (CIAppPipelineEventStageStatus,),
            "tags": ([str],),
        }

    attribute_map = {
        "dependencies": "dependencies",
        "end": "end",
        "error": "error",
        "git": "git",
        "id": "id",
        "level": "level",
        "metrics": "metrics",
        "name": "name",
        "node": "node",
        "parameters": "parameters",
        "pipeline_name": "pipeline_name",
        "pipeline_unique_id": "pipeline_unique_id",
        "queue_time": "queue_time",
        "start": "start",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        end: datetime,
        id: str,
        level: CIAppPipelineEventStageLevel,
        name: str,
        pipeline_name: str,
        pipeline_unique_id: str,
        start: datetime,
        status: CIAppPipelineEventStageStatus,
        dependencies: Union[List[str], none_type, UnsetType] = unset,
        error: Union[CIAppCIError, none_type, UnsetType] = unset,
        git: Union[CIAppGitInfo, none_type, UnsetType] = unset,
        metrics: Union[List[str], none_type, UnsetType] = unset,
        node: Union[CIAppHostInfo, none_type, UnsetType] = unset,
        parameters: Union[CIAppPipelineEventParameters, none_type, UnsetType] = unset,
        queue_time: Union[int, none_type, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of a CI stage.

        :param dependencies: A list of stage IDs that this stage depends on.
        :type dependencies: [str], none_type, optional

        :param end: Time when the stage run finished. The time format must be RFC3339.
        :type end: datetime

        :param error: Contains information of the CI error.
        :type error: CIAppCIError, none_type, optional

        :param git: If pipelines are triggered due to actions to a Git repository, then all payloads must contain this.
            Note that either ``tag`` or ``branch`` has to be provided, but not both.
        :type git: CIAppGitInfo, none_type, optional

        :param id: UUID for the stage. It has to be unique at least in the pipeline scope.
        :type id: str

        :param level: Used to distinguish between pipelines, stages, jobs and steps.
        :type level: CIAppPipelineEventStageLevel

        :param metrics: A list of user-defined metrics. The metrics must follow the ``key:value`` pattern and the value must be numeric.
        :type metrics: [str], none_type, optional

        :param name: The name for the stage.
        :type name: str

        :param node: Contains information of the host running the pipeline, stage, job, or step.
        :type node: CIAppHostInfo, none_type, optional

        :param parameters: A map of key-value parameters or environment variables that were defined for the pipeline.
        :type parameters: CIAppPipelineEventParameters, none_type, optional

        :param pipeline_name: The parent pipeline name.
        :type pipeline_name: str

        :param pipeline_unique_id: The parent pipeline UUID.
        :type pipeline_unique_id: str

        :param queue_time: The queue time in milliseconds, if applicable.
        :type queue_time: int, none_type, optional

        :param start: Time when the stage run started (it should not include any queue time). The time format must be RFC3339.
        :type start: datetime

        :param status: The final status of the stage.
        :type status: CIAppPipelineEventStageStatus

        :param tags: A list of user-defined tags. The tags must follow the ``key:value`` pattern.
        :type tags: [str], none_type, optional
        """
        if dependencies is not unset:
            kwargs["dependencies"] = dependencies
        if error is not unset:
            kwargs["error"] = error
        if git is not unset:
            kwargs["git"] = git
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if node is not unset:
            kwargs["node"] = node
        if parameters is not unset:
            kwargs["parameters"] = parameters
        if queue_time is not unset:
            kwargs["queue_time"] = queue_time
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.end = end
        self_.id = id
        self_.level = level
        self_.name = name
        self_.pipeline_name = pipeline_name
        self_.pipeline_unique_id = pipeline_unique_id
        self_.start = start
        self_.status = status
