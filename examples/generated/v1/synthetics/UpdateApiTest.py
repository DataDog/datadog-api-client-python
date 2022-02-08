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
    public_id = "public_id_example"  # str | The public ID of the test to get details from.
    body = SyntheticsAPITest(
        config=SyntheticsAPITestConfig(
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
            steps=[
                SyntheticsAPIStep(
                    allow_failure=True,
                    assertions=[
                        SyntheticsAssertion(),
                    ],
                    extracted_values=[
                        SyntheticsParsingOptions(
                            field="content-type",
                            name="name_example",
                            parser=SyntheticsVariableParser(
                                type=SyntheticsGlobalVariableParserType("raw"),
                                value="value_example",
                            ),
                            type=SyntheticsGlobalVariableParseTestOptionsType("http_body"),
                        ),
                    ],
                    is_critical=True,
                    name="Example step name",
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
                    retry=SyntheticsTestOptionsRetry(
                        count=1,
                        interval=3.14,
                    ),
                    subtype=SyntheticsAPIStepSubtype("http"),
                ),
            ],
        ),
        locations=["aws:eu-west-3"],
        message="Notification message",
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
        subtype=SyntheticsTestDetailsSubType("http"),
        tags=["env:production"],
        type=SyntheticsAPITestType("api"),
    )  # SyntheticsAPITest | New test details to be saved.

    # example passing only required values which don't have defaults set
    try:
        # Edit an API test
        api_response = api_instance.update_api_test(public_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->update_api_test: %s\n" % e)
