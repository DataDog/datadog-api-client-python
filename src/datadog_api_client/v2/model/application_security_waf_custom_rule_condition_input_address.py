# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleConditionInputAddress(ModelSimple):
    """
    Input from the request on which the condition should apply.

    :param value: Must be one of ["server.db.statement", "server.io.fs.file", "server.io.net.url", "server.sys.shell.cmd", "server.request.method", "server.request.uri.raw", "server.request.path_params", "server.request.query", "server.request.headers", "server.request.headers.no_cookies", "server.request.custom-auth", "server.request.cookies", "server.request.trailers", "server.request.body", "server.request.body.filenames", "server.response.status", "server.response.headers.no_cookies", "server.response.trailers", "server.response.body", "grpc.server.request.metadata", "grpc.server.request.message", "grpc.server.method", "graphql.server.all_resolvers", "usr.id", "http.client_ip", "server.llm.event", "server.llm.guard.verdict", "_dd.appsec.fp.http.header", "_dd.appsec.fp.http.network", "_dd.appsec.fp.session", "_dd.appsec.fp.http.endpoint"].
    :type value: str
    """

    allowed_values = {
        "server.db.statement",
        "server.io.fs.file",
        "server.io.net.url",
        "server.sys.shell.cmd",
        "server.request.method",
        "server.request.uri.raw",
        "server.request.path_params",
        "server.request.query",
        "server.request.headers",
        "server.request.headers.no_cookies",
        "server.request.custom-auth",
        "server.request.cookies",
        "server.request.trailers",
        "server.request.body",
        "server.request.body.filenames",
        "server.response.status",
        "server.response.headers.no_cookies",
        "server.response.trailers",
        "server.response.body",
        "grpc.server.request.metadata",
        "grpc.server.request.message",
        "grpc.server.method",
        "graphql.server.all_resolvers",
        "usr.id",
        "http.client_ip",
        "server.llm.event",
        "server.llm.guard.verdict",
        "_dd.appsec.fp.http.header",
        "_dd.appsec.fp.http.network",
        "_dd.appsec.fp.session",
        "_dd.appsec.fp.http.endpoint",
    }
    SERVER_DB_STATEMENT: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_IO_FS_FILE: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_IO_NET_URL: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_SYS_SHELL_CMD: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_METHOD: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_URI_RAW: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_PATH_PARAMS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_QUERY: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_HEADERS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_HEADERS_NO_COOKIES: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_CUSTOM_AUTH: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_COOKIES: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_TRAILERS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_BODY: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_REQUEST_BODY_FILENAMES: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_RESPONSE_STATUS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_RESPONSE_HEADERS_NO_COOKIES: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_RESPONSE_TRAILERS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_RESPONSE_BODY: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    GRPC_SERVER_REQUEST_METADATA: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    GRPC_SERVER_REQUEST_MESSAGE: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    GRPC_SERVER_METHOD: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    GRAPHQL_SERVER_ALL_RESOLVERS: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    USR_ID: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    HTTP_CLIENT_IP: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_LLM_EVENT: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    SERVER_LLM_GUARD_VERDICT: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    DD_APPSEC_FP_HTTP_HEADER: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    DD_APPSEC_FP_HTTP_NETWORK: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    DD_APPSEC_FP_SESSION: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]
    DD_APPSEC_FP_HTTP_ENDPOINT: ClassVar["ApplicationSecurityWafCustomRuleConditionInputAddress"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_DB_STATEMENT = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.db.statement")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_IO_FS_FILE = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.io.fs.file")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_IO_NET_URL = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.io.net.url")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_SYS_SHELL_CMD = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.sys.shell.cmd")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_METHOD = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.method")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_URI_RAW = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.uri.raw")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_PATH_PARAMS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.path_params")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_QUERY = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.query")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_HEADERS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.headers")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_HEADERS_NO_COOKIES = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.headers.no_cookies")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_CUSTOM_AUTH = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.custom-auth")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_COOKIES = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.cookies")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_TRAILERS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.trailers")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_BODY = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.body")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_BODY_FILENAMES = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.request.body.filenames")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_RESPONSE_STATUS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.response.status")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_RESPONSE_HEADERS_NO_COOKIES = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.response.headers.no_cookies")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_RESPONSE_TRAILERS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.response.trailers")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_RESPONSE_BODY = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.response.body")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.GRPC_SERVER_REQUEST_METADATA = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("grpc.server.request.metadata")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.GRPC_SERVER_REQUEST_MESSAGE = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("grpc.server.request.message")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.GRPC_SERVER_METHOD = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("grpc.server.method")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.GRAPHQL_SERVER_ALL_RESOLVERS = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("graphql.server.all_resolvers")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.USR_ID = ApplicationSecurityWafCustomRuleConditionInputAddress(
    "usr.id"
)
ApplicationSecurityWafCustomRuleConditionInputAddress.HTTP_CLIENT_IP = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("http.client_ip")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_LLM_EVENT = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.llm.event")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_LLM_GUARD_VERDICT = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("server.llm.guard.verdict")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.DD_APPSEC_FP_HTTP_HEADER = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("_dd.appsec.fp.http.header")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.DD_APPSEC_FP_HTTP_NETWORK = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("_dd.appsec.fp.http.network")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.DD_APPSEC_FP_SESSION = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("_dd.appsec.fp.session")
)
ApplicationSecurityWafCustomRuleConditionInputAddress.DD_APPSEC_FP_HTTP_ENDPOINT = (
    ApplicationSecurityWafCustomRuleConditionInputAddress("_dd.appsec.fp.http.endpoint")
)
