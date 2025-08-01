# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
    from datadog_api_client.v1.model.synthetics_test_request_body_type import SyntheticsTestRequestBodyType
    from datadog_api_client.v1.model.synthetics_test_call_type import SyntheticsTestCallType
    from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
    from datadog_api_client.v1.model.synthetics_test_request_dns_server_port import SyntheticsTestRequestDNSServerPort
    from datadog_api_client.v1.model.synthetics_test_request_body_file import SyntheticsTestRequestBodyFile
    from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
    from datadog_api_client.v1.model.synthetics_test_options_http_version import SyntheticsTestOptionsHTTPVersion
    from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
    from datadog_api_client.v1.model.synthetics_test_request_port import SyntheticsTestRequestPort
    from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy
    from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
    from datadog_api_client.v1.model.synthetics_basic_auth_sigv4 import SyntheticsBasicAuthSigv4
    from datadog_api_client.v1.model.synthetics_basic_auth_ntlm import SyntheticsBasicAuthNTLM
    from datadog_api_client.v1.model.synthetics_basic_auth_digest import SyntheticsBasicAuthDigest
    from datadog_api_client.v1.model.synthetics_basic_auth_oauth_client import SyntheticsBasicAuthOauthClient
    from datadog_api_client.v1.model.synthetics_basic_auth_oauth_rop import SyntheticsBasicAuthOauthROP


class SyntheticsTestRequest(ModelNormal):
    validations = {
        "number_of_packets": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
        from datadog_api_client.v1.model.synthetics_test_request_body_type import SyntheticsTestRequestBodyType
        from datadog_api_client.v1.model.synthetics_test_call_type import SyntheticsTestCallType
        from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
        from datadog_api_client.v1.model.synthetics_test_request_dns_server_port import (
            SyntheticsTestRequestDNSServerPort,
        )
        from datadog_api_client.v1.model.synthetics_test_request_body_file import SyntheticsTestRequestBodyFile
        from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
        from datadog_api_client.v1.model.synthetics_test_options_http_version import SyntheticsTestOptionsHTTPVersion
        from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
        from datadog_api_client.v1.model.synthetics_test_request_port import SyntheticsTestRequestPort
        from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy

        return {
            "allow_insecure": (bool,),
            "basic_auth": (SyntheticsBasicAuth,),
            "body": (str,),
            "body_type": (SyntheticsTestRequestBodyType,),
            "call_type": (SyntheticsTestCallType,),
            "certificate": (SyntheticsTestRequestCertificate,),
            "certificate_domains": ([str],),
            "check_certificate_revocation": (bool,),
            "compressed_json_descriptor": (str,),
            "compressed_proto_file": (str,),
            "disable_aia_intermediate_fetching": (bool,),
            "dns_server": (str,),
            "dns_server_port": (SyntheticsTestRequestDNSServerPort,),
            "files": ([SyntheticsTestRequestBodyFile],),
            "follow_redirects": (bool,),
            "form": ({str: (str,)},),
            "headers": (SyntheticsTestHeaders,),
            "host": (str,),
            "http_version": (SyntheticsTestOptionsHTTPVersion,),
            "is_message_base64_encoded": (bool,),
            "message": (str,),
            "metadata": (SyntheticsTestMetadata,),
            "method": (str,),
            "no_saving_response_body": (bool,),
            "number_of_packets": (int,),
            "persist_cookies": (bool,),
            "port": (SyntheticsTestRequestPort,),
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
        "body_type": "bodyType",
        "call_type": "callType",
        "certificate": "certificate",
        "certificate_domains": "certificateDomains",
        "check_certificate_revocation": "checkCertificateRevocation",
        "compressed_json_descriptor": "compressedJsonDescriptor",
        "compressed_proto_file": "compressedProtoFile",
        "disable_aia_intermediate_fetching": "disableAiaIntermediateFetching",
        "dns_server": "dnsServer",
        "dns_server_port": "dnsServerPort",
        "files": "files",
        "follow_redirects": "follow_redirects",
        "form": "form",
        "headers": "headers",
        "host": "host",
        "http_version": "httpVersion",
        "is_message_base64_encoded": "isMessageBase64Encoded",
        "message": "message",
        "metadata": "metadata",
        "method": "method",
        "no_saving_response_body": "noSavingResponseBody",
        "number_of_packets": "numberOfPackets",
        "persist_cookies": "persistCookies",
        "port": "port",
        "proxy": "proxy",
        "query": "query",
        "servername": "servername",
        "service": "service",
        "should_track_hops": "shouldTrackHops",
        "timeout": "timeout",
        "url": "url",
    }

    def __init__(
        self_,
        allow_insecure: Union[bool, UnsetType] = unset,
        basic_auth: Union[
            SyntheticsBasicAuth,
            SyntheticsBasicAuthWeb,
            SyntheticsBasicAuthSigv4,
            SyntheticsBasicAuthNTLM,
            SyntheticsBasicAuthDigest,
            SyntheticsBasicAuthOauthClient,
            SyntheticsBasicAuthOauthROP,
            UnsetType,
        ] = unset,
        body: Union[str, UnsetType] = unset,
        body_type: Union[SyntheticsTestRequestBodyType, UnsetType] = unset,
        call_type: Union[SyntheticsTestCallType, UnsetType] = unset,
        certificate: Union[SyntheticsTestRequestCertificate, UnsetType] = unset,
        certificate_domains: Union[List[str], UnsetType] = unset,
        check_certificate_revocation: Union[bool, UnsetType] = unset,
        compressed_json_descriptor: Union[str, UnsetType] = unset,
        compressed_proto_file: Union[str, UnsetType] = unset,
        disable_aia_intermediate_fetching: Union[bool, UnsetType] = unset,
        dns_server: Union[str, UnsetType] = unset,
        dns_server_port: Union[SyntheticsTestRequestDNSServerPort, int, str, UnsetType] = unset,
        files: Union[List[SyntheticsTestRequestBodyFile], UnsetType] = unset,
        follow_redirects: Union[bool, UnsetType] = unset,
        form: Union[Dict[str, str], UnsetType] = unset,
        headers: Union[SyntheticsTestHeaders, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        http_version: Union[SyntheticsTestOptionsHTTPVersion, UnsetType] = unset,
        is_message_base64_encoded: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        metadata: Union[SyntheticsTestMetadata, UnsetType] = unset,
        method: Union[str, UnsetType] = unset,
        no_saving_response_body: Union[bool, UnsetType] = unset,
        number_of_packets: Union[int, UnsetType] = unset,
        persist_cookies: Union[bool, UnsetType] = unset,
        port: Union[SyntheticsTestRequestPort, int, str, UnsetType] = unset,
        proxy: Union[SyntheticsTestRequestProxy, UnsetType] = unset,
        query: Union[dict, UnsetType] = unset,
        servername: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        should_track_hops: Union[bool, UnsetType] = unset,
        timeout: Union[float, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the Synthetic test request.

        :param allow_insecure: Allows loading insecure content for an HTTP request in a multistep test step.
        :type allow_insecure: bool, optional

        :param basic_auth: Object to handle basic authentication when performing the test.
        :type basic_auth: SyntheticsBasicAuth, optional

        :param body: Body to include in the test.
        :type body: str, optional

        :param body_type: Type of the request body.
        :type body_type: SyntheticsTestRequestBodyType, optional

        :param call_type: The type of gRPC call to perform.
        :type call_type: SyntheticsTestCallType, optional

        :param certificate: Client certificate to use when performing the test request.
        :type certificate: SyntheticsTestRequestCertificate, optional

        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificateDomains``.
        :type certificate_domains: [str], optional

        :param check_certificate_revocation: Check for certificate revocation.
        :type check_certificate_revocation: bool, optional

        :param compressed_json_descriptor: A protobuf JSON descriptor that needs to be gzipped first then base64 encoded.
        :type compressed_json_descriptor: str, optional

        :param compressed_proto_file: A protobuf file that needs to be gzipped first then base64 encoded.
        :type compressed_proto_file: str, optional

        :param disable_aia_intermediate_fetching: Disable fetching intermediate certificates from AIA.
        :type disable_aia_intermediate_fetching: bool, optional

        :param dns_server: DNS server to use for DNS tests.
        :type dns_server: str, optional

        :param dns_server_port: DNS server port to use for DNS tests.
        :type dns_server_port: SyntheticsTestRequestDNSServerPort, optional

        :param files: Files to be used as part of the request in the test. Only valid if ``bodyType`` is ``multipart/form-data``.
        :type files: [SyntheticsTestRequestBodyFile], optional

        :param follow_redirects: Specifies whether or not the request follows redirects.
        :type follow_redirects: bool, optional

        :param form: Form to be used as part of the request in the test. Only valid if ``bodyType`` is ``multipart/form-data``.
        :type form: {str: (str,)}, optional

        :param headers: Headers to include when performing the test.
        :type headers: SyntheticsTestHeaders, optional

        :param host: Host name to perform the test with.
        :type host: str, optional

        :param http_version: HTTP version to use for a Synthetic test.
        :type http_version: SyntheticsTestOptionsHTTPVersion, optional

        :param is_message_base64_encoded: Whether the message is base64 encoded.
        :type is_message_base64_encoded: bool, optional

        :param message: Message to send for UDP or WebSocket tests.
        :type message: str, optional

        :param metadata: Metadata to include when performing the gRPC test.
        :type metadata: SyntheticsTestMetadata, optional

        :param method: Either the HTTP method/verb to use or a gRPC method available on the service set in the ``service`` field. Required if ``subtype`` is ``HTTP`` or if ``subtype`` is ``grpc`` and ``callType`` is ``unary``.
        :type method: str, optional

        :param no_saving_response_body: Determines whether or not to save the response body.
        :type no_saving_response_body: bool, optional

        :param number_of_packets: Number of pings to use per test.
        :type number_of_packets: int, optional

        :param persist_cookies: Persist cookies across redirects.
        :type persist_cookies: bool, optional

        :param port: Port to use when performing the test.
        :type port: SyntheticsTestRequestPort, optional

        :param proxy: The proxy to perform the test.
        :type proxy: SyntheticsTestRequestProxy, optional

        :param query: Query to use for the test.
        :type query: dict, optional

        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake,
            allowing the server to present one of multiple possible certificates on
            the same IP address and TCP port number.
        :type servername: str, optional

        :param service: The gRPC service on which you want to perform the gRPC call.
        :type service: str, optional

        :param should_track_hops: Turns on a traceroute probe to discover all gateways along the path to the host destination.
        :type should_track_hops: bool, optional

        :param timeout: Timeout in seconds for the test.
        :type timeout: float, optional

        :param url: URL to perform the test with.
        :type url: str, optional
        """
        if allow_insecure is not unset:
            kwargs["allow_insecure"] = allow_insecure
        if basic_auth is not unset:
            kwargs["basic_auth"] = basic_auth
        if body is not unset:
            kwargs["body"] = body
        if body_type is not unset:
            kwargs["body_type"] = body_type
        if call_type is not unset:
            kwargs["call_type"] = call_type
        if certificate is not unset:
            kwargs["certificate"] = certificate
        if certificate_domains is not unset:
            kwargs["certificate_domains"] = certificate_domains
        if check_certificate_revocation is not unset:
            kwargs["check_certificate_revocation"] = check_certificate_revocation
        if compressed_json_descriptor is not unset:
            kwargs["compressed_json_descriptor"] = compressed_json_descriptor
        if compressed_proto_file is not unset:
            kwargs["compressed_proto_file"] = compressed_proto_file
        if disable_aia_intermediate_fetching is not unset:
            kwargs["disable_aia_intermediate_fetching"] = disable_aia_intermediate_fetching
        if dns_server is not unset:
            kwargs["dns_server"] = dns_server
        if dns_server_port is not unset:
            kwargs["dns_server_port"] = dns_server_port
        if files is not unset:
            kwargs["files"] = files
        if follow_redirects is not unset:
            kwargs["follow_redirects"] = follow_redirects
        if form is not unset:
            kwargs["form"] = form
        if headers is not unset:
            kwargs["headers"] = headers
        if host is not unset:
            kwargs["host"] = host
        if http_version is not unset:
            kwargs["http_version"] = http_version
        if is_message_base64_encoded is not unset:
            kwargs["is_message_base64_encoded"] = is_message_base64_encoded
        if message is not unset:
            kwargs["message"] = message
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if method is not unset:
            kwargs["method"] = method
        if no_saving_response_body is not unset:
            kwargs["no_saving_response_body"] = no_saving_response_body
        if number_of_packets is not unset:
            kwargs["number_of_packets"] = number_of_packets
        if persist_cookies is not unset:
            kwargs["persist_cookies"] = persist_cookies
        if port is not unset:
            kwargs["port"] = port
        if proxy is not unset:
            kwargs["proxy"] = proxy
        if query is not unset:
            kwargs["query"] = query
        if servername is not unset:
            kwargs["servername"] = servername
        if service is not unset:
            kwargs["service"] = service
        if should_track_hops is not unset:
            kwargs["should_track_hops"] = should_track_hops
        if timeout is not unset:
            kwargs["timeout"] = timeout
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
