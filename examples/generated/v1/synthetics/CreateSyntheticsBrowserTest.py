import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = synthetics_api.SyntheticsApi(api_client)
    body = SyntheticsBrowserTest(
        config=SyntheticsBrowserTestConfig(
            assertions=[
                SyntheticsAssertion(),
            ],
            config_variables=[
                SyntheticsConfigVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsConfigVariableType("text"),
                ),
            ],
            request=SyntheticsTestRequest(
                allow_insecure=True,
                basic_auth=SyntheticsBasicAuth(),
                body="body_example",
                certificate=SyntheticsTestRequestCertificate(
                    cert=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                    key=SyntheticsTestRequestCertificateItem(
                        content="content_example",
                        filename="filename_example",
                        updated_at="updated_at_example",
                    ),
                ),
                dns_server="dns_server_example",
                dns_server_port=1,
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                host="host_example",
                message="message_example",
                method=HTTPMethod("GET"),
                no_saving_response_body=True,
                number_of_packets=0,
                port=1,
                proxy=SyntheticsTestRequestProxy(
                    headers=SyntheticsTestHeaders(
                        key="key_example",
                    ),
                    url="https://example.com",
                ),
                query={},
                servername="servername_example",
                should_track_hops=True,
                timeout=3.14,
                url="https://example.com",
            ),
            set_cookie="set_cookie_example",
            variables=[
                SyntheticsBrowserVariable(
                    example="example_example",
                    id="id_example",
                    name="VARIABLE_NAME",
                    pattern="pattern_example",
                    type=SyntheticsBrowserVariableType("text"),
                ),
            ],
        ),
        locations=["example-location"],
        message="",
        name="Example test name",
        options=SyntheticsTestOptions(
            accept_self_signed=True,
            allow_insecure=True,
            device_ids=[
                SyntheticsDeviceID("laptop_large"),
            ],
            disable_cors=True,
            follow_redirects=True,
            min_failure_duration=1,
            min_location_failed=1,
            monitor_name="monitor_name_example",
            monitor_options=SyntheticsTestOptionsMonitorOptions(
                renotify_interval=0,
            ),
            monitor_priority=1,
            no_screenshot=True,
            retry=SyntheticsTestOptionsRetry(
                count=1,
                interval=3.14,
            ),
            tick_every=30,
        ),
        status=SyntheticsTestPauseStatus("live"),
        steps=[
            SyntheticsStep(
                allow_failure=True,
                name="name_example",
                params={},
                timeout=1,
                type=SyntheticsStepType("assertElementContent"),
            ),
        ],
        tags=[
            "tags_example",
        ],
        type=SyntheticsBrowserTestType("browser"),
    )  # SyntheticsBrowserTest | Details of the test to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a browser test
        api_response = api_instance.create_synthetics_browser_test(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->create_synthetics_browser_test: %s\n" % e)
