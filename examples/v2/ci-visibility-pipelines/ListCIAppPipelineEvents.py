"""
Get a list of pipelines events returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.list_ci_app_pipeline_events(
        filter_query="@ci.provider.name:circleci",
        filter_from=(datetime.now() + relativedelta(minutes=-30)),
        filter_to=datetime.now(),
        page_limit=5,
    )

    print(response)
