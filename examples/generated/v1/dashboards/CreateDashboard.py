import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import dashboards_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    body = Dashboard(
        description="description_example",
        is_read_only=False,
        layout_type=DashboardLayoutType("ordered"),
        notify_list=[
            "notify_list_example",
        ],
        reflow_type=DashboardReflowType("auto"),
        restricted_roles=[
            "restricted_roles_example",
        ],
        template_variable_presets=[
            DashboardTemplateVariablePreset(
                name="name_example",
                template_variables=[
                    DashboardTemplateVariablePresetValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
        template_variables=[
            DashboardTemplateVariable(
                available_values=["my-host","host1","host2"],
                default="my-host",
                name="host1",
                prefix="host",
            ),
        ],
        title="",
        widgets=[
            Widget(
                definition=WidgetDefinition(),
                id=1,
                layout=WidgetLayout(
                    height=0,
                    is_column_break=True,
                    width=0,
                    x=0,
                    y=0,
                ),
            ),
        ],
    )  # Dashboard | Create a dashboard request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
