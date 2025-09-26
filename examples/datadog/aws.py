"""
Example of using AWS authentication with the Datadog API client.

This example shows how to configure the client to use AWS credentials
for authentication instead of API keys. This is ideal for environments
like AWS Ray where you want to use temporary credentials.
"""

import os
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.aws import AWSAuth
from datadog_api_client.delegated_auth import DelegatedTokenConfig
from datadog_api_client.v1.api.authentication_api import AuthenticationApi


def main():
    # Set up AWS credentials in environment variables
    # These would typically be set by your AWS environment (EC2 instance role, ECS task role, etc.)
    # or explicitly set in your environment:
    # os.environ["AWS_ACCESS_KEY_ID"] = "your-access-key-id"
    # os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret-access-key"
    # os.environ["AWS_SESSION_TOKEN"] = "your-session-token"
    
    # Verify AWS credentials are available
    if not all([
        os.getenv("AWS_ACCESS_KEY_ID"),
        os.getenv("AWS_SECRET_ACCESS_KEY"),
        os.getenv("AWS_SESSION_TOKEN")
    ]):
        print("Error: AWS credentials not found in environment variables.")
        print("Please set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_SESSION_TOKEN")
        return
    
    # Your Datadog organization UUID
    # This should be provided by your Datadog administrator
    org_uuid = os.getenv("DD_ORG_UUID")
    if not org_uuid:
        print("Error: DD_ORG_UUID environment variable not set.")
        print("Please set your Datadog organization UUID")
        return
    
    # Create AWS authentication provider
    # Optionally specify AWS region (defaults to us-east-1)
    aws_region = os.getenv("AWS_REGION", "us-east-1")
    aws_auth = AWSAuth(aws_region=aws_region)
    
    # Create delegated token configuration
    delegated_config = DelegatedTokenConfig(
        org_uuid=org_uuid,
        provider="aws",
        provider_auth=aws_auth
    )
    
    # Create configuration and set delegated token config
    configuration = Configuration()
    configuration.delegated_token_config = delegated_config
    
    # Optional: Set Datadog site if different from default
    site = os.getenv("DD_SITE", "datadoghq.com")
    configuration.server_variables["site"] = site
    
    # Create API client with cloud authentication
    with ApiClient(configuration) as api_client:
        # Create API instance
        api_instance = AuthenticationApi(api_client)
        
        try:
            # Test the authentication by validating the token
            response = api_instance.validate()
            print("✅ Authentication successful!")
            print(f"Valid: {response.valid}")
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")


if __name__ == "__main__":
    main()
