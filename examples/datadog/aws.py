"""
Example of using AWS authentication with the Datadog API client.

This example shows how to configure the client to use AWS credentials
for authentication instead of API keys.
"""

import os
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.aws import AWSAuth
from datadog_api_client.v2.api.teams_api import TeamsApi


def main():
    # Set up AWS credentials in environment variables
    # These would typically be set by your AWS environment (EC2 instance role, ECS task role, etc.)
    # or explicitly set in your environment:
    # os.environ["AWS_ACCESS_KEY_ID"] = "your-access-key-id"
    # os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret-access-key"
    # os.environ["AWS_SESSION_TOKEN"] = "your-session-token"

    # Verify AWS credentials are available
    if not all([os.getenv("AWS_ACCESS_KEY_ID"), os.getenv("AWS_SECRET_ACCESS_KEY"), os.getenv("AWS_SESSION_TOKEN")]):
        print("Error: AWS credentials not found in environment variables.")
        print("Please set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_SESSION_TOKEN")
        return

    org_uuid = os.getenv("DD_TEST_ORG_UUID")
    if not org_uuid:
        print("Error: DD_TEST_ORG_UUID environment variable not set.")
        print("Please set your Datadog organization UUID")
        return

    # Create AWS authentication provider
    # Optionally specify AWS region (defaults to us-east-1)
    aws_region = os.getenv("AWS_REGION", "us-east-1")
    aws_auth = AWSAuth(aws_region=aws_region)

    # Create configuration with AWS authentication
    configuration = Configuration(host="https://dd.datad0g.com")
    configuration.delegated_auth_provider = aws_auth
    configuration.delegated_auth_org_uuid = org_uuid

    # Create API client with the configuration
    with ApiClient(configuration) as api_client:
        # Create API instance - using TeamsApi as an example
        api_instance = TeamsApi(api_client)

        try:
            # Test the authentication by listing teams
            # The client will automatically use AWS authentication for this call
            api_response = api_instance.list_teams()
            print("Authentication successful!")
            print(f"Found {len(api_response.data)} teams")

        except Exception as e:
            print(f"Authentication failed: {e}")


if __name__ == "__main__":
    main()
