# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestRequest(ModelNormal):
    validations = {
        "dns_server_port": {
            "inclusive_maximum": 65535,
            "inclusive_minimum": 1,
        },
        "number_of_packets": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
        from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
        from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
        from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
        from datadog_api_client.v1.model.http_method import HTTPMethod
        from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy

        return {
            "allow_insecure": (bool,),
            "basic_auth": (SyntheticsBasicAuth,),
            "body": (str,),
            "certificate": (SyntheticsTestRequestCertificate,),
            "dns_server": (str,),
            "dns_server_port": (int,),
            "follow_redirects": (bool,),
            "headers": (SyntheticsTestHeaders,),
            "host": (str,),
            "message": (str,),
            "metadata": (SyntheticsTestMetadata,),
            "method": (HTTPMethod,),
            "no_saving_response_body": (bool,),
            "number_of_packets": (int,),
            "port": (int,),
            "proxy": (SyntheticsTestRequestProxy,),
            "query": (dict,),
            "servername": (str,),
            "service": (str,),
            "should_track_hops": (bool,),
            "timeout": (float,),
            "url": (str,),
        }

    attribute_map = {
        "allow_insecure": "allow_insecure",
        "basic_auth": "basicAuth",
        "body": "body",
        "certificate": "certificate",
        "dns_server": "dnsServer",
        "dns_server_port": "dnsServerPort",
        "follow_redirects": "follow_redirects",
        "headers": "headers",
        "host": "host",
        "message": "message",
        "metadata": "metadata",
        "method": "method",
        "no_saving_response_body": "noSavingResponseBody",
        "number_of_packets": "numberOfPackets",
        "port": "port",
        "proxy": "proxy",
        "query": "query",
        "servername": "servername",
        "service": "service",
        "should_track_hops": "shouldTrackHops",
        "timeout": "timeout",
        "url": "url",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the Synthetic test request.

        :param allow_insecure: Allows loading insecure content for an HTTP request in a multistep test step.
        :type allow_insecure: bool, optional

        :param basic_auth: Object to handle basic authentication when performing the test.
        :type basic_auth: SyntheticsBasicAuth, optional

        :param body: Body to include in the test.
        :type body: str, optional

        :param certificate: Client certificate to use when performing the test request.
        :type certificate: SyntheticsTestRequestCertificate, optional

        :param dns_server: DNS server to use for DNS tests.
        :type dns_server: str, optional

        :param dns_server_port: DNS server port to use for DNS tests.
        :type dns_server_port: int, optional

        :param follow_redirects: Specifies whether or not the request follows redirects.
        :type follow_redirects: bool, optional

        :param headers: Headers to include when performing the test.
        :type headers: SyntheticsTestHeaders, optional

        :param host: Host name to perform the test with.
        :type host: str, optional

        :param message: Message to send for UDP or WebSocket tests.
        :type message: str, optional

        :param metadata: Metadata to include when performing the gRPC test.
        :type metadata: SyntheticsTestMetadata, optional

        :param method: The HTTP method.
        :type method: HTTPMethod, optional

        :param no_saving_response_body: Determines whether or not to save the response body.
        :type no_saving_response_body: bool, optional

        :param number_of_packets: Number of pings to use per test.
        :type number_of_packets: int, optional

        :param port: Port to use when performing the test.
        :type port: int, optional

        :param proxy: The proxy to perform the test.
        :type proxy: SyntheticsTestRequestProxy, optional

        :param query: Query to use for the test.
        :type query: dict, optional

        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake,
            allowing the server to present one of multiple possible certificates on
            the same IP address and TCP port number.
        :type servername: str, optional

        :param service: gRPC service on which you want to perform the healthcheck.
        :type service: str, optional

        :param should_track_hops: Turns on a traceroute probe to discover all gateways along the path to the host destination.
        :type should_track_hops: bool, optional

        :param timeout: Timeout in seconds for the test.
        :type timeout: float, optional

        :param url: URL to perform the test with.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
