# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CIAppCreatePipelineEventRequestAttributesResource(ModelComposed):
    def __init__(self, **kwargs):
        """
        Details of the CI pipeline event.

        :param end: Time when the pipeline run finished. It cannot be older than 18 hours in the past from the current time. The time format must be RFC3339.
        :type end: datetime

        :param error: Contains information of the CI error.
        :type error: CIAppCIError, none_type, optional

        :param git: If pipelines are triggered due to actions to a Git repository, then all payloads must contain this.
            Note that either `tag` or `branch` has to be provided, but not both.
        :type git: CIAppGitInfo, none_type, optional

        :param is_manual: Whether or not the pipeline was triggered manually by the user.
        :type is_manual: bool, none_type, optional

        :param is_resumed: Whether or not the pipeline was resumed after being blocked.
        :type is_resumed: bool, none_type, optional

        :param level: Used to distinguish between pipelines, stages, jobs, and steps.
        :type level: CIAppPipelineEventPipelineLevel

        :param metrics: A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.
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
            If the `pipeline_id` is unique, then both `unique_id` and `pipeline_id` can be set to the same value.
        :type pipeline_id: str, optional

        :param previous_attempt: If the pipeline is a retry, this should contain the details of the previous attempt.
        :type previous_attempt: CIAppPipelineEventPreviousPipeline, none_type, optional

        :param queue_time: The queue time in milliseconds, if applicable.
        :type queue_time: int, none_type, optional

        :param start: Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.
        :type start: datetime

        :param status: The final status of the pipeline.
        :type status: CIAppPipelineEventPipelineStatus

        :param tags: A list of user-defined tags. The tags must follow the `key:value` pattern.
        :type tags: [str], none_type, optional

        :param unique_id: UUID of the pipeline run. The ID has to be unique across retries and pipelines,
            including partial retries.
        :type unique_id: str

        :param url: The URL to look at the pipeline in the CI provider UI.
        :type url: str

        :param dependencies: A list of stage IDs that this stage depends on.
        :type dependencies: [str], none_type, optional

        :param id: UUID for the stage. It has to be unique at least in the pipeline scope.
        :type id: str

        :param pipeline_name: The parent pipeline name.
        :type pipeline_name: str

        :param pipeline_unique_id: The parent pipeline UUID.
        :type pipeline_unique_id: str

        :param stage_id: The parent stage UUID (if applicable).
        :type stage_id: str, none_type, optional

        :param stage_name: The parent stage name (if applicable).
        :type stage_name: str, none_type, optional

        :param job_id: The parent job UUID (if applicable).
        :type job_id: str, none_type, optional

        :param job_name: The parent job name (if applicable).
        :type job_name: str, none_type, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline import CIAppPipelineEventPipeline
        from datadog_api_client.v2.model.ci_app_pipeline_event_stage import CIAppPipelineEventStage
        from datadog_api_client.v2.model.ci_app_pipeline_event_job import CIAppPipelineEventJob
        from datadog_api_client.v2.model.ci_app_pipeline_event_step import CIAppPipelineEventStep

        return {
            "oneOf": [
                CIAppPipelineEventPipeline,
                CIAppPipelineEventStage,
                CIAppPipelineEventJob,
                CIAppPipelineEventStep,
            ],
        }
