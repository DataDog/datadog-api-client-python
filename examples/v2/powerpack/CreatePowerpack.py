"""
Create a new powerpack returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi
from datadog_api_client.v2.model.powerpack import Powerpack
from datadog_api_client.v2.model.powerpack_attributes import PowerpackAttributes
from datadog_api_client.v2.model.powerpack_data import PowerpackData
from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable

body = Powerpack(
    data=PowerpackData(
        attributes=PowerpackAttributes(
            description="Sample powerpack",
            group_widget=dict(
                [
                    (
                        "definition",
                        "{'layout_type': 'ordered', 'show_title': True, 'title': 'Sample Powerpack', 'type': 'group', 'widgets': [{'definition': {'content': 'test', 'type': 'note'}}]}",
                    ),
                    ("layout", "{'height': 3, 'width': 12, 'x': 0, 'y': 0}"),
                ]
            ),
            name="Sample Powerpack",
            tags=[
                "tag:sample",
            ],
            template_variables=[
                PowerpackTemplateVariable(
                    defaults=[
                        "*",
                    ],
                    name="sample",
                ),
            ],
        ),
        type="powerpack",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    response = api_instance.create_powerpack(body=body)

    print(response)
