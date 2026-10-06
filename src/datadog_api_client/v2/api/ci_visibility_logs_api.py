# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.ci_log_content_encoding import CILogContentEncoding
from datadog_api_client.v2.model.ci_log_item import CILogItem


class CIVisibilityLogsApi:
    """
    Send CI job logs over HTTP for CI Visibility.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._submit_ci_log_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/cilogs",
                "operation_id": "submit_ci_log",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "The regional site for CI Visibility customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": [
                                    "datadoghq.com",
                                    "us3.datadoghq.com",
                                    "us5.datadoghq.com",
                                    "ap1.datadoghq.com",
                                    "ap2.datadoghq.com",
                                    "uk1.datadoghq.com",
                                    "datadoghq.eu",
                                ],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "http-intake.logs",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "http-intake.logs.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "http-intake.logs",
                            },
                        },
                    },
                ],
            },
            params_map={
                "content_encoding": {
                    "openapi_types": (CILogContentEncoding,),
                    "attribute": "Content-Encoding",
                    "location": "header",
                },
                "body": {
                    "required": True,
                    "validation": {
                        "max_items": 1000,
                    },
                    "openapi_types": ([CILogItem],),
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def submit_ci_log(
        self,
        body: List[CILogItem],
        *,
        content_encoding: Union[CILogContentEncoding, UnsetType] = unset,
    ) -> dict:
        """Send CI job logs.

        Send log lines for a CI job over HTTP. See the `CI Visibility Pipelines
        API <https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/send-pipeline-event/>`_ for submitting the
        associated pipeline and job events.

        A request can contain one log object or an array of up to 1,000 log objects. The maximum uncompressed request
        body size is 5.1 MiB.

        You can stream log lines while a CI job runs or send them after it finishes. After you submit the completed job
        event, 20 seconds without a new log line marks the job's logs as complete. Lines sent after that may not appear.

        A job can have up to 128 additional attributes and 256 tags. Additional attributes are top-level fields with
        string, number, Boolean, or null values. Nested objects and arrays are rejected. Additional attributes and
        ``ddtags`` apply to all log lines in the job. If an additional attribute has different values on different lines,
        the first value received is used. Tags supplied on different lines are combined. A job can contain up to
        2,000,000 log records or 1 GiB of message bytes in total.

        To reduce request size, send gzip-compressed JSON with the ``Content-Encoding: gzip`` header. Retry requests after
        a 408, 429, 500, or 503 response.

        :param body: CI job log line or batch in JSON format.
        :type body: [CILogItem]
        :param content_encoding: HTTP header used to compress the JSON request body.
        :type content_encoding: CILogContentEncoding, optional
        :rtype: dict
        """
        kwargs: Dict[str, Any] = {}
        if content_encoding is not unset:
            kwargs["content_encoding"] = content_encoding

        kwargs["body"] = body

        return self._submit_ci_log_endpoint.call_with_http_info(**kwargs)
