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
    body = SyntheticsCITestBody(
        tests=[
            SyntheticsCITest(
                allow_insecure_certificates=True,
                basic_auth=SyntheticsBasicAuth(),
                body="body_example",
                body_type="body_type_example",
                cookies="cookies_example",
                device_ids=[
                    SyntheticsDeviceID("laptop_large"),
                ],
                follow_redirects=True,
                headers=SyntheticsTestHeaders(
                    key="key_example",
                ),
                locations=[
                    "locations_example",
                ],
                metadata=SyntheticsCIBatchMetadata(
                    ci=SyntheticsCIBatchMetadataCI(
                        pipeline=SyntheticsCIBatchMetadataPipeline(
                            url="url_example",
                        ),
                        provider=SyntheticsCIBatchMetadataProvider(
                            name="name_example",
                        ),
                    ),
                    git=SyntheticsCIBatchMetadataGit(
                        branch="branch_example",
                        commit_sha="commit_sha_example",
                    ),
                ),
                public_id="aaa-aaa-aaa",
                retry=SyntheticsTestOptionsRetry(
                    count=1,
                    interval=3.14,
                ),
                start_url="start_url_example",
                variables={
                    "key": "key_example",
                },
            ),
        ],
    )  # SyntheticsCITestBody | Details of the test to trigger.

    # example passing only required values which don't have defaults set
    try:
        # Trigger tests from CI/CD pipelines
        api_response = api_instance.trigger_ci_tests(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->trigger_ci_tests: %s\n" % e)
