# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DnsMetricKey(ModelSimple):
    """
    The metric key for DNS metrics.

    :param value: Must be one of ["dns_total_requests", "dns_failures", "dns_successful_responses", "dns_failed_responses", "dns_timeouts", "dns_responses.nxdomain", "dns_responses.servfail", "dns_responses.other", "dns_success_latency_percentile", "dns_failure_latency_percentile"].
    :type value: str
    """

    allowed_values = {
        "dns_total_requests",
        "dns_failures",
        "dns_successful_responses",
        "dns_failed_responses",
        "dns_timeouts",
        "dns_responses.nxdomain",
        "dns_responses.servfail",
        "dns_responses.other",
        "dns_success_latency_percentile",
        "dns_failure_latency_percentile",
    }
    DNS_TOTAL_REQUESTS: ClassVar["DnsMetricKey"]
    DNS_FAILURES: ClassVar["DnsMetricKey"]
    DNS_SUCCESSFUL_RESPONSES: ClassVar["DnsMetricKey"]
    DNS_FAILED_RESPONSES: ClassVar["DnsMetricKey"]
    DNS_TIMEOUTS: ClassVar["DnsMetricKey"]
    DNS_RESPONSES_NXDOMAIN: ClassVar["DnsMetricKey"]
    DNS_RESPONSES_SERVFAIL: ClassVar["DnsMetricKey"]
    DNS_RESPONSES_OTHER: ClassVar["DnsMetricKey"]
    DNS_SUCCESS_LATENCY_PERCENTILE: ClassVar["DnsMetricKey"]
    DNS_FAILURE_LATENCY_PERCENTILE: ClassVar["DnsMetricKey"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DnsMetricKey.DNS_TOTAL_REQUESTS = DnsMetricKey("dns_total_requests")
DnsMetricKey.DNS_FAILURES = DnsMetricKey("dns_failures")
DnsMetricKey.DNS_SUCCESSFUL_RESPONSES = DnsMetricKey("dns_successful_responses")
DnsMetricKey.DNS_FAILED_RESPONSES = DnsMetricKey("dns_failed_responses")
DnsMetricKey.DNS_TIMEOUTS = DnsMetricKey("dns_timeouts")
DnsMetricKey.DNS_RESPONSES_NXDOMAIN = DnsMetricKey("dns_responses.nxdomain")
DnsMetricKey.DNS_RESPONSES_SERVFAIL = DnsMetricKey("dns_responses.servfail")
DnsMetricKey.DNS_RESPONSES_OTHER = DnsMetricKey("dns_responses.other")
DnsMetricKey.DNS_SUCCESS_LATENCY_PERCENTILE = DnsMetricKey("dns_success_latency_percentile")
DnsMetricKey.DNS_FAILURE_LATENCY_PERCENTILE = DnsMetricKey("dns_failure_latency_percentile")
