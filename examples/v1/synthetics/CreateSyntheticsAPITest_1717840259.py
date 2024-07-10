"""
Create a multi-step api test with every type of basicAuth returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
from datadog_api_client.v1.model.synthetics_api_test_step_subtype import SyntheticsAPITestStepSubtype
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_basic_auth_digest import SyntheticsBasicAuthDigest
from datadog_api_client.v1.model.synthetics_basic_auth_digest_type import SyntheticsBasicAuthDigestType
from datadog_api_client.v1.model.synthetics_basic_auth_ntlm import SyntheticsBasicAuthNTLM
from datadog_api_client.v1.model.synthetics_basic_auth_ntlm_type import SyntheticsBasicAuthNTLMType
from datadog_api_client.v1.model.synthetics_basic_auth_oauth_client import SyntheticsBasicAuthOauthClient
from datadog_api_client.v1.model.synthetics_basic_auth_oauth_client_type import SyntheticsBasicAuthOauthClientType
from datadog_api_client.v1.model.synthetics_basic_auth_oauth_rop import SyntheticsBasicAuthOauthROP
from datadog_api_client.v1.model.synthetics_basic_auth_oauth_rop_type import SyntheticsBasicAuthOauthROPType
from datadog_api_client.v1.model.synthetics_basic_auth_oauth_token_api_authentication import (
    SyntheticsBasicAuthOauthTokenApiAuthentication,
)
from datadog_api_client.v1.model.synthetics_basic_auth_sigv4 import SyntheticsBasicAuthSigv4
from datadog_api_client.v1.model.synthetics_basic_auth_sigv4_type import SyntheticsBasicAuthSigv4Type
from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        steps=[
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthWeb(
                        password="password",
                        username="username",
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthWeb(
                        password="password",
                        username="username",
                        type=SyntheticsBasicAuthWebType.WEB,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthSigv4(
                        access_key="accessKey",
                        secret_key="secretKey",
                        type=SyntheticsBasicAuthSigv4Type.SIGV4,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthNTLM(
                        type=SyntheticsBasicAuthNTLMType.NTLM,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthDigest(
                        password="password",
                        username="username",
                        type=SyntheticsBasicAuthDigestType.DIGEST,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthOauthClient(
                        access_token_url="accessTokenUrl",
                        token_api_authentication=SyntheticsBasicAuthOauthTokenApiAuthentication.HEADER,
                        client_id="clientId",
                        client_secret="clientSecret",
                        type=SyntheticsBasicAuthOauthClientType.OAUTH_CLIENT,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthOauthROP(
                        access_token_url="accessTokenUrl",
                        password="password",
                        token_api_authentication=SyntheticsBasicAuthOauthTokenApiAuthentication.HEADER,
                        username="username",
                        type=SyntheticsBasicAuthOauthROPType.OAUTH_ROP,
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
        ],
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_multi_step_with_every_type_of_basic_auth.json",
    name="Example-Synthetic",
    options=SyntheticsTestOptions(
        tick_every=60,
    ),
    subtype=SyntheticsTestDetailsSubType.MULTI,
    type=SyntheticsAPITestType.API,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_api_test(body=body)

    print(response)
