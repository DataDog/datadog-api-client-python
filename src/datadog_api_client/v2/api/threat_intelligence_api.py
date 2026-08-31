# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.stix_ingest_response import STIXIngestResponse
from datadog_api_client.v2.model.stix_content_encoding import STIXContentEncoding
from datadog_api_client.v2.model.stix_bundle_request import STIXBundleRequest


class ThreatIntelligenceApi:
    """
    Ingest and manage threat intelligence data for security enrichment and investigation.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._add_stix_threat_intel_endpoint = _Endpoint(
            settings={
                "response_type": (STIXIngestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/threat-intel/stix",
                "operation_id": "add_stix_threat_intel",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "ti_vendor": {
                    "required": True,
                    "validation": {
                        "max_length": 10,
                        "min_length": 1,
                    },
                    "openapi_types": (str,),
                    "attribute": "ti_vendor",
                    "location": "header",
                },
                "content_encoding": {
                    "openapi_types": (STIXContentEncoding,),
                    "attribute": "Content-Encoding",
                    "location": "header",
                },
                "body": {
                    "required": True,
                    "openapi_types": (STIXBundleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_stix_threat_intel(
        self,
        ti_vendor: str,
        body: STIXBundleRequest,
        *,
        content_encoding: Union[STIXContentEncoding, UnsetType] = unset,
    ) -> STIXIngestResponse:
        """Ingest STIX threat intelligence.

        Ingest a STIX 2.1 bundle containing threat intelligence indicators. Only indicator objects are processed. Supported indicator patterns contain IPv4 addresses, IPv6 addresses, domain names, or SHA-256 file hashes.

        Non-indicator objects are ignored and are not included in the response counters. Indicator objects with unsupported STIX versions or patterns that produce no supported observable values increment the ``unsupported`` counter. Patterns that cannot be parsed increment the ``invalid`` counter. Processing is best effort, so valid supported indicators in the same bundle are still added.

        A successful response means ingestion has completed. Reference-table materialization and enrichment happen asynchronously. Requests are limited to 50 MB as received, 100 MB after decompression, and 10 requests per second per API key. Gzip-compressed request bodies are supported.

        :param ti_vendor: Vendor identifier for the feed. The value must not exceed 10 characters. Datadog normalizes the accepted value to lowercase, converts non-alphanumeric characters to underscores, and trims leading and trailing underscores.
        :type ti_vendor: str
        :param body: A STIX 2.1 bundle containing indicator objects. The request body must not exceed 50 MB as received or 100 MB after decompression.
        :type body: STIXBundleRequest
        :param content_encoding: Content encoding for the request body. Use gzip for a compressed STIX bundle.
        :type content_encoding: STIXContentEncoding, optional
        :rtype: STIXIngestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ti_vendor"] = ti_vendor

        if content_encoding is not unset:
            kwargs["content_encoding"] = content_encoding

        kwargs["body"] = body

        return self._add_stix_threat_intel_endpoint.call_with_http_info(**kwargs)
