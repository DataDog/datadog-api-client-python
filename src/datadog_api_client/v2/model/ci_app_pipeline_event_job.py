# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CIAppPipelineEventJob(ModelComposed):
    def __init__(self, **kwargs):
        """
        Details of a CI job.

        :param dependencies: A list of job IDs that this job depends on.
        :type dependencies: [str], none_type, optional

        :param end: Time when the job run finished. The time format must be RFC3339.
        :type end: datetime

        :param error: Contains information of the CI error.
        :type error: CIAppCIError, none_type, optional

        :param git: If pipelines are triggered due to actions to a Git repository, then all payloads must contain this.
            Note that either `tag` or `branch` has to be provided, but not both.
        :type git: CIAppGitInfo, none_type, optional

        :param id: The UUID for the job. It has to be unique within each pipeline execution.
        :type id: str

        :param level: Used to distinguish between pipelines, stages, jobs, and steps.
        :type level: CIAppPipelineEventJobLevel

        :param metrics: A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.
        :type metrics: [str], none_type, optional

        :param name: The name for the job.
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

        :param stage_id: The parent stage UUID (if applicable).
        :type stage_id: str, none_type, optional

        :param stage_name: The parent stage name (if applicable).
        :type stage_name: str, none_type, optional

        :param start: Time when the job run instance started (it should not include any queue time).
            The time format must be RFC3339.
        :type start: datetime

        :param status: The final status of the job.
        :type status: CIAppPipelineEventJobStatus

        :param tags: A list of user-defined tags. The tags must follow the `key:value` pattern.
        :type tags: [str], none_type, optional

        :param url: The URL to look at the job in the CI provider UI.
        :type url: str
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
        from datadog_api_client.v2.model.ci_app_pipeline_event_finished_job import CIAppPipelineEventFinishedJob
        from datadog_api_client.v2.model.ci_app_pipeline_event_in_progress_job import CIAppPipelineEventInProgressJob

        return {
            "oneOf": [
                CIAppPipelineEventFinishedJob,
                CIAppPipelineEventInProgressJob,
            ],
        }
