"""
Update a monitor user template to a new version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_user_template_request_attributes import MonitorUserTemplateRequestAttributes
from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType
from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
    MonitorUserTemplateTemplateVariablesItems,
)
from datadog_api_client.v2.model.monitor_user_template_update_data import MonitorUserTemplateUpdateData
from datadog_api_client.v2.model.monitor_user_template_update_request import MonitorUserTemplateUpdateRequest

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = environ["MONITOR_USER_TEMPLATE_DATA_ID"]

body = MonitorUserTemplateUpdateRequest(
    data=MonitorUserTemplateUpdateData(
        attributes=MonitorUserTemplateRequestAttributes(
            description="A description.",
            monitor_definition=dict(
                [
                    ("message", "A msg."),
                    ("name", "A name example-monitor"),
                    ("query", "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                    ("type", "query alert"),
                ]
            ),
            tags=[
                "integration:Azure",
            ],
            template_variables=[
                MonitorUserTemplateTemplateVariablesItems(
                    available_values=[
                        "value1",
                        "value2",
                    ],
                    defaults=[
                        "defaultValue",
                    ],
                    name="regionName",
                    tag_key="datacenter",
                ),
            ],
            title="Postgres DB example-monitor",
        ),
        id=MONITOR_USER_TEMPLATE_DATA_ID,
        type=MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_user_template(template_id=MONITOR_USER_TEMPLATE_DATA_ID, body=body)

    print(response)
