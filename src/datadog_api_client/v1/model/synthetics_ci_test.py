# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCITest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
        from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
        from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata import SyntheticsCIBatchMetadata
        from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry

        return {
            "allow_insecure_certificates": (bool,),
            "basic_auth": (SyntheticsBasicAuth,),
            "body": (str,),
            "body_type": (str,),
            "cookies": (str,),
            "device_ids": ([SyntheticsDeviceID],),
            "follow_redirects": (bool,),
            "headers": (SyntheticsTestHeaders,),
            "locations": ([str],),
            "metadata": (SyntheticsCIBatchMetadata,),
            "public_id": (str,),
            "retry": (SyntheticsTestOptionsRetry,),
            "start_url": (str,),
            "variables": ({str: (str,)},),
        }

    attribute_map = {
        "allow_insecure_certificates": "allowInsecureCertificates",
        "basic_auth": "basicAuth",
        "body": "body",
        "body_type": "bodyType",
        "cookies": "cookies",
        "device_ids": "deviceIds",
        "follow_redirects": "followRedirects",
        "headers": "headers",
        "locations": "locations",
        "metadata": "metadata",
        "public_id": "public_id",
        "retry": "retry",
        "start_url": "startUrl",
        "variables": "variables",
    }

    def __init__(self, public_id, *args, **kwargs):
        """
        Test configuration for Synthetics CI

        :param allow_insecure_certificates: Disable certificate checks in API tests.
        :type allow_insecure_certificates: bool, optional

        :param basic_auth: Object to handle basic authentication when performing the test.
        :type basic_auth: SyntheticsBasicAuth, optional

        :param body: Body to include in the test.
        :type body: str, optional

        :param body_type: Type of the data sent in a synthetics API test.
        :type body_type: str, optional

        :param cookies: Cookies for the request.
        :type cookies: str, optional

        :param device_ids: For browser test, array with the different device IDs used to run the test.
        :type device_ids: [SyntheticsDeviceID], optional

        :param follow_redirects: For API HTTP test, whether or not the test should follow redirects.
        :type follow_redirects: bool, optional

        :param headers: Headers to include when performing the test.
        :type headers: SyntheticsTestHeaders, optional

        :param locations: Array of locations used to run the test.
        :type locations: [str], optional

        :param metadata: Metadata for the Synthetics tests run.
        :type metadata: SyntheticsCIBatchMetadata, optional

        :param public_id: The public ID of the Synthetics test to trigger.
        :type public_id: str

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param start_url: Starting URL for the browser test.
        :type start_url: str, optional

        :param variables: Variables to replace in the test.
        :type variables: {str: (str,)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id

    @classmethod
    def _from_openapi_data(cls, public_id, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsCITest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id
        return self
