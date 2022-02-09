import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.
    body = SlackIntegrationChannel(
        display=SlackIntegrationChannelDisplay(
            message=True,
            notified=True,
            snapshot=True,
            tags=True,
        ),
        name="#general",
    )  # SlackIntegrationChannel | Payload describing Slack channel to be created

    # example passing only required values which don't have defaults set
    try:
        # Create a Slack integration channel
        api_response = api_instance.create_slack_integration_channel(account_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->create_slack_integration_channel: %s\n" % e)
