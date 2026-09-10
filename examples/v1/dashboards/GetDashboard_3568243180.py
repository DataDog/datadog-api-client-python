"""
Get a dashboard with five team tags and two AI tags
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

# there is a valid "dashboard_with_team_and_ai_tags" in the system
DASHBOARD_WITH_TEAM_AND_AI_TAGS_ID = environ["DASHBOARD_WITH_TEAM_AND_AI_TAGS_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.get_dashboard(
        dashboard_id=DASHBOARD_WITH_TEAM_AND_AI_TAGS_ID,
    )

    print(response)
