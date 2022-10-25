"""
Get a list of tests events returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_tests_api import CIVisibilityTestsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityTestsApi(api_client)
    response = api_instance.list_ci_app_test_events(
        filter_query="@test.service:web-ui-tests",
        filter_from=(datetime.now() + relativedelta(seconds=-30)),
        filter_to=datetime.now(),
        page_limit=5,
    )

    print(response)
