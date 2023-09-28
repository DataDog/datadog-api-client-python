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
    from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel
    from datadog_api_client.v2.model.ci_app_host_info import CIAppHostInfo
    from datadog_api_client.v2.model.ci_app_pipeline_event_parameters import CIAppPipelineEventParameters
    from datadog_api_client.v2.model.ci_app_pipeline_event_parent_pipeline import CIAppPipelineEventParentPipeline
    from datadog_api_client.v2.model.ci_app_pipeline_event_previous_pipeline import CIAppPipelineEventPreviousPipeline
    from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_status import CIAppPipelineEventPipelineStatus


class CIAppPipelineEventPipeline(ModelNormal):
    validations = {
        "queue_time": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_ci_error import CIAppCIError
        from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
        from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel
        from datadog_api_client.v2.model.ci_app_host_info import CIAppHostInfo
        from datadog_api_client.v2.model.ci_app_pipeline_event_parameters import CIAppPipelineEventParameters
        from datadog_api_client.v2.model.ci_app_pipeline_event_parent_pipeline import CIAppPipelineEventParentPipeline
        from datadog_api_client.v2.model.ci_app_pipeline_event_previous_pipeline import (
            CIAppPipelineEventPreviousPipeline,
        )
        from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_status import CIAppPipelineEventPipelineStatus

        return {
            "end": (datetime,),
            "error": (CIAppCIError,),
            "git": (CIAppGitInfo,),
            "is_manual": (bool, none_type),
            "is_resumed": (bool, none_type),
            "level": (CIAppPipelineEventPipelineLevel,),
            "metrics": ([str],),
            "name": (str,),
            "node": (CIAppHostInfo,),
            "parameters": (CIAppPipelineEventParameters,),
            "parent_pipeline": (CIAppPipelineEventParentPipeline,),
            "partial_retry": (bool,),
            "pipeline_id": (str,),
            "previous_attempt": (CIAppPipelineEventPreviousPipeline,),
            "queue_time": (int, none_type),
            "start": (datetime,),
            "status": (CIAppPipelineEventPipelineStatus,),
            "tags": ([str],),
            "unique_id": (str,),
            "url": (str,),
        }

    attribute_map = {
        "end": "end",
        "error": "error",
        "git": "git",
        "is_manual": "is_manual",
        "is_resumed": "is_resumed",
        "level": "level",
        "metrics": "metrics",
        "name": "name",
        "node": "node",
        "parameters": "parameters",
        "parent_pipeline": "parent_pipeline",
        "partial_retry": "partial_retry",
        "pipeline_id": "pipeline_id",
        "previous_attempt": "previous_attempt",
        "queue_time": "queue_time",
        "start": "start",
        "status": "status",
        "tags": "tags",
        "unique_id": "unique_id",
        "url": "url",
    }

    def __init__(
        self_,
        end: datetime,
        level: CIAppPipelineEventPipelineLevel,
        name: str,
        partial_retry: bool,
        start: datetime,
        status: CIAppPipelineEventPipelineStatus,
        unique_id: str,
        url: str,
        error: Union[CIAppCIError, none_type, UnsetType] = unset,
        git: Union[CIAppGitInfo, none_type, UnsetType] = unset,
        is_manual: Union[bool, none_type, UnsetType] = unset,
        is_resumed: Union[bool, none_type, UnsetType] = unset,
        metrics: Union[List[str], none_type, UnsetType] = unset,
        node: Union[CIAppHostInfo, none_type, UnsetType] = unset,
        parameters: Union[CIAppPipelineEventParameters, none_type, UnsetType] = unset,
        parent_pipeline: Union[CIAppPipelineEventParentPipeline, none_type, UnsetType] = unset,
        pipeline_id: Union[str, UnsetType] = unset,
        previous_attempt: Union[CIAppPipelineEventPreviousPipeline, none_type, UnsetType] = unset,
        queue_time: Union[int, none_type, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the top level pipeline, build, or workflow of your CI.

        :param end: Time when the pipeline run finished. It cannot be older than 18 hours in the past from the current time. The time format must be RFC3339.
        :type end: datetime

        :param error: Contains information of the CI error.
        :type error: CIAppCIError, none_type, optional

        :param git: If pipelines are triggered due to actions to a Git repository, then all payloads must contain this.
            Note that either ``tag`` or ``branch`` has to be provided, but not both.
        :type git: CIAppGitInfo, none_type, optional

        :param is_manual: Whether or not the pipeline was triggered manually by the user.
        :type is_manual: bool, none_type, optional

        :param is_resumed: Whether or not the pipeline was resumed after being blocked.
        :type is_resumed: bool, none_type, optional

        :param level: Used to distinguish between pipelines, stages, jobs, and steps.
        :type level: CIAppPipelineEventPipelineLevel

        :param metrics: A list of user-defined metrics. The metrics must follow the ``key:value`` pattern and the value must be numeric.
        :type metrics: [str], none_type, optional

        :param name: Name of the pipeline. All pipeline runs for the builds should have the same name.
        :type name: str

        :param node: Contains information of the host running the pipeline, stage, job, or step.
        :type node: CIAppHostInfo, none_type, optional

        :param parameters: A map of key-value parameters or environment variables that were defined for the pipeline.
        :type parameters: CIAppPipelineEventParameters, none_type, optional

        :param parent_pipeline: If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.
        :type parent_pipeline: CIAppPipelineEventParentPipeline, none_type, optional

        :param partial_retry: Whether or not the pipeline was a partial retry of a previous attempt. A partial retry is one
            which only runs a subset of the original jobs.
        :type partial_retry: bool

        :param pipeline_id: Any ID used in the provider to identify the pipeline run even if it is not unique across retries.
            If the ``pipeline_id`` is unique, then both ``unique_id`` and ``pipeline_id`` can be set to the same value.
        :type pipeline_id: str, optional

        :param previous_attempt: If the pipeline is a retry, this should contain the details of the previous attempt.
        :type previous_attempt: CIAppPipelineEventPreviousPipeline, none_type, optional

        :param queue_time: The queue time in milliseconds, if applicable.
        :type queue_time: int, none_type, optional

        :param start: Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.
        :type start: datetime

        :param status: The final status of the pipeline.
        :type status: CIAppPipelineEventPipelineStatus

        :param tags: A list of user-defined tags. The tags must follow the ``key:value`` pattern.
        :type tags: [str], none_type, optional

        :param unique_id: UUID of the pipeline run. The ID has to be unique across retries and pipelines,
            including partial retries.
        :type unique_id: str

        :param url: The URL to look at the pipeline in the CI provider UI.
        :type url: str
        """
        if error is not unset:
            kwargs["error"] = error
        if git is not unset:
            kwargs["git"] = git
        if is_manual is not unset:
            kwargs["is_manual"] = is_manual
        if is_resumed is not unset:
            kwargs["is_resumed"] = is_resumed
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if node is not unset:
            kwargs["node"] = node
        if parameters is not unset:
            kwargs["parameters"] = parameters
        if parent_pipeline is not unset:
            kwargs["parent_pipeline"] = parent_pipeline
        if pipeline_id is not unset:
            kwargs["pipeline_id"] = pipeline_id
        if previous_attempt is not unset:
            kwargs["previous_attempt"] = previous_attempt
        if queue_time is not unset:
            kwargs["queue_time"] = queue_time
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.end = end
        self_.level = level
        self_.name = name
        self_.partial_retry = partial_retry
        self_.start = start
        self_.status = status
        self_.unique_id = unique_id
        self_.url = url
