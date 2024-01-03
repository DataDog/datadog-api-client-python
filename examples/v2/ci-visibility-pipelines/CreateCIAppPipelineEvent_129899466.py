"""
Send pipeline job event returns "Request accepted for processing" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request import CIAppCreatePipelineEventRequest
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
    CIAppCreatePipelineEventRequestAttributes,
)
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import CIAppCreatePipelineEventRequestData
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
    CIAppCreatePipelineEventRequestDataType,
)
from datadog_api_client.v2.model.ci_app_pipeline_event_job import CIAppPipelineEventJob
from datadog_api_client.v2.model.ci_app_pipeline_event_job_level import CIAppPipelineEventJobLevel
from datadog_api_client.v2.model.ci_app_pipeline_event_job_status import CIAppPipelineEventJobStatus

body = CIAppCreatePipelineEventRequest(
    data=CIAppCreatePipelineEventRequestData(
        attributes=CIAppCreatePipelineEventRequestAttributes(
            resource=CIAppPipelineEventJob(
                end=(datetime.now() + relativedelta(seconds=-30)),
                level=CIAppPipelineEventJobLevel.JOB,
                name="Build image",
                start=(datetime.now() + relativedelta(seconds=-120)),
                status=CIAppPipelineEventJobStatus.ERROR,
                id="cf9456de-8b9e-4c27-aa79-27b1e78c1a33",
                pipeline_unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
                pipeline_name="Deploy to AWS",
                url="https://my-ci-provider.example/jobs/my-jobs/run/1",
            ),
        ),
        type=CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.create_ci_app_pipeline_event(body=body)

    print(response)
