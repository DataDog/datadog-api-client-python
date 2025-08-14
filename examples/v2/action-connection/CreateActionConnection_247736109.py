"""
Create a new Action Connection with HTTPMtlsAuth returns "Successfully created Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.http_integration import HTTPIntegration
from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
from datadog_api_client.v2.model.http_mtls_auth import HTTPMtlsAuth
from datadog_api_client.v2.model.http_mtls_auth_type import HTTPMtlsAuthType

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="HTTP mTLS Connection exampleactionconnection",
            integration=HTTPIntegration(
                type=HTTPIntegrationType.HTTP,
                base_url="https://api.example.com",
                credentials=HTTPMtlsAuth(
                    type=HTTPMtlsAuthType.HTTPMTLSAUTH,
                    certificate="-----BEGIN CERTIFICATE-----\nMIICXjCCAUYCCQDOGcCfCHfhPzANBgkqhkiG9w0BAQsFADAzMQswCQYDVQQGEwJV\nUzELMAkGA1UECAwCQ0ExFTATBgNVBAoMDERhdGFkb2cgSW5jLjAeFw0yNDA1MTQw\nMDA1NThaFw0yNTA1MTQwMDA1NThaMDMxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJD\nQTEVMBMGA1UECgwMRGF0YWRvZyBJbmMuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A\nMIIBCgKCAQEAwQDTmLqWv2L6YhzBcjKgPEzd3kE+9dZ4hBXBCjK6HgF/3aOKOSYq\nM9KPFHgJj6SjUJ+8TqX4sV6yW5xGX8dKjOpTYQfExEjGYcVrqKoOGg2k6dGkHyGm\n2VzL4zKyK1C3zJ4KpJnMYK8dPPcgzJvO7jGxGKMgLVU3VNdxKGTrqKmC6RbZLQOz\nM3fLp7bF2VcJ6VkGKW+yBK6vVMbQKMvjTbGqr3vIRd8SZzKRTsyIzXQDKgOv2vPn\nSqYJjKFJ8vJ7JeH6zGyLjQ1cGVy9jJ3+TjJoJhCGOyGzJpBGIcXfYjFDLcSRh7KE\nQIDAQABo1MwUTAdBgNVHQ4EFgQU/V8vJkPJ8b9yQnC/9bJ2kJGJ5MjoyEwHwYDVR0j\nBBgwFoAU/V8vJkPJ8b9yQnC/9bJ2kJGJ5Mjo\n-----END CERTIFICATE-----",
                    private_key="-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDBaNOMV7V8T7gR\nOmNcNfqGHxPrLLo1w2J7J8h6S8bVD9yCH2JKV8J5G2J8J0V8J3Jg8b3Jg8LxJgV\nV8J6JgV8J9JgJg8LJg8VJgV5JgLLJgVVJg8V4Jg8VLJg8V6JgV8JqJgVV8J3JgV\nV8J7JgVV8J5JgVV8J8JgVVJg8LJgJVLJgLVJgVVJgLJgVVJgVVJgVVJgLVJgVV\nJgVVJgVVJgLJgVVJgLVJgLLJgVVJgVLJgVVJgVLJgVVJgVVJgVVJgVVJgVVJg\nVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJ\nAgMBAAECggEBAKoJkJJJJkJJkJ\n-----END PRIVATE KEY-----",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.create_action_connection(body=body)

    print(response)
