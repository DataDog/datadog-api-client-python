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
    body = SyntheticsTriggerBody(
        tests=[
            SyntheticsTriggerTest(
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
            ),
        ],
    )  # SyntheticsTriggerBody | The identifiers of the tests to trigger.

    # example passing only required values which don't have defaults set
    try:
        # Trigger Synthetics tests
        api_response = api_instance.trigger_tests(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SyntheticsApi->trigger_tests: %s\n" % e)
