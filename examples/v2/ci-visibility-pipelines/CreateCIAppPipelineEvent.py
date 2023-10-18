"""
Send pipeline event returns "Request accepted for processing" response
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
from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline import CIAppPipelineEventPipeline
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_status import CIAppPipelineEventPipelineStatus

body = CIAppCreatePipelineEventRequest(
    data=CIAppCreatePipelineEventRequestData(
        attributes=CIAppCreatePipelineEventRequestAttributes(
            resource=CIAppPipelineEventPipeline(
                end=(datetime.now() + relativedelta(seconds=-30)),
                level=CIAppPipelineEventPipelineLevel.PIPELINE,
                name="Deploy to AWS",
                partial_retry=False,
                start=(datetime.now() + relativedelta(seconds=-120)),
                status=CIAppPipelineEventPipelineStatus.SUCCESS,
                unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
                url="https://my-ci-provider.example/pipelines/my-pipeline/run/1",
                git=CIAppGitInfo(
                    repository_url="https://github.com/DataDog/datadog-agent",
                    sha="7f263865994b76066c4612fd1965215e7dcb4cd2",
                    author_email="john.doe@email.com",
                ),
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
