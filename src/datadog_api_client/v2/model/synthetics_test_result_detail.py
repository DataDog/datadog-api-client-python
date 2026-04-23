# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_assertion_result import SyntheticsTestResultAssertionResult
    from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
    from datadog_api_client.v2.model.synthetics_test_result_certificate import SyntheticsTestResultCertificate
    from datadog_api_client.v2.model.synthetics_test_result_dns_resolution import SyntheticsTestResultDnsResolution
    from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
    from datadog_api_client.v2.model.synthetics_test_result_handshake import SyntheticsTestResultHandshake
    from datadog_api_client.v2.model.synthetics_test_result_netpath import SyntheticsTestResultNetpath
    from datadog_api_client.v2.model.synthetics_test_result_netstats import SyntheticsTestResultNetstats
    from datadog_api_client.v2.model.synthetics_test_result_ocsp_response import SyntheticsTestResultOCSPResponse
    from datadog_api_client.v2.model.synthetics_test_result_traceroute_hop import SyntheticsTestResultTracerouteHop
    from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
    from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
    from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
    from datadog_api_client.v2.model.synthetics_test_result_status import SyntheticsTestResultStatus
    from datadog_api_client.v2.model.synthetics_test_result_step import SyntheticsTestResultStep
    from datadog_api_client.v2.model.synthetics_test_result_trace import SyntheticsTestResultTrace
    from datadog_api_client.v2.model.synthetics_test_result_turn import SyntheticsTestResultTurn
    from datadog_api_client.v2.model.synthetics_test_result_variables import SyntheticsTestResultVariables


class SyntheticsTestResultDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_assertion_result import (
            SyntheticsTestResultAssertionResult,
        )
        from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
        from datadog_api_client.v2.model.synthetics_test_result_certificate import SyntheticsTestResultCertificate
        from datadog_api_client.v2.model.synthetics_test_result_dns_resolution import SyntheticsTestResultDnsResolution
        from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
        from datadog_api_client.v2.model.synthetics_test_result_handshake import SyntheticsTestResultHandshake
        from datadog_api_client.v2.model.synthetics_test_result_netpath import SyntheticsTestResultNetpath
        from datadog_api_client.v2.model.synthetics_test_result_netstats import SyntheticsTestResultNetstats
        from datadog_api_client.v2.model.synthetics_test_result_ocsp_response import SyntheticsTestResultOCSPResponse
        from datadog_api_client.v2.model.synthetics_test_result_traceroute_hop import SyntheticsTestResultTracerouteHop
        from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
        from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
        from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
        from datadog_api_client.v2.model.synthetics_test_result_status import SyntheticsTestResultStatus
        from datadog_api_client.v2.model.synthetics_test_result_step import SyntheticsTestResultStep
        from datadog_api_client.v2.model.synthetics_test_result_trace import SyntheticsTestResultTrace
        from datadog_api_client.v2.model.synthetics_test_result_turn import SyntheticsTestResultTurn
        from datadog_api_client.v2.model.synthetics_test_result_variables import SyntheticsTestResultVariables

        return {
            "assertions": ([SyntheticsTestResultAssertionResult],),
            "bucket_keys": (SyntheticsTestResultBucketKeys,),
            "call_type": (str,),
            "cert": (SyntheticsTestResultCertificate,),
            "compressed_json_descriptor": (str,),
            "compressed_steps": (str,),
            "connection_outcome": (str,),
            "dns_resolution": (SyntheticsTestResultDnsResolution,),
            "duration": (float,),
            "exited_on_step_success": (bool,),
            "failure": (SyntheticsTestResultFailure,),
            "finished_at": (int,),
            "handshake": (SyntheticsTestResultHandshake,),
            "id": (str,),
            "initial_id": (str,),
            "is_fast_retry": (bool,),
            "is_last_retry": (bool,),
            "netpath": (SyntheticsTestResultNetpath,),
            "netstats": (SyntheticsTestResultNetstats,),
            "ocsp": (SyntheticsTestResultOCSPResponse,),
            "ping": (SyntheticsTestResultTracerouteHop,),
            "received_email_count": (int,),
            "received_message": (str,),
            "request": (SyntheticsTestResultRequestInfo,),
            "resolved_ip": (str,),
            "response": (SyntheticsTestResultResponseInfo,),
            "run_type": (SyntheticsTestResultRunType,),
            "sent_message": (str,),
            "start_url": (str,),
            "started_at": (int,),
            "status": (SyntheticsTestResultStatus,),
            "steps": ([SyntheticsTestResultStep],),
            "time_to_interactive": (int,),
            "timings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "trace": (SyntheticsTestResultTrace,),
            "traceroute": ([SyntheticsTestResultTracerouteHop],),
            "triggered_at": (int,),
            "tunnel": (bool,),
            "turns": ([SyntheticsTestResultTurn],),
            "unhealthy": (bool,),
            "variables": (SyntheticsTestResultVariables,),
        }

    attribute_map = {
        "assertions": "assertions",
        "bucket_keys": "bucket_keys",
        "call_type": "call_type",
        "cert": "cert",
        "compressed_json_descriptor": "compressed_json_descriptor",
        "compressed_steps": "compressed_steps",
        "connection_outcome": "connection_outcome",
        "dns_resolution": "dns_resolution",
        "duration": "duration",
        "exited_on_step_success": "exited_on_step_success",
        "failure": "failure",
        "finished_at": "finished_at",
        "handshake": "handshake",
        "id": "id",
        "initial_id": "initial_id",
        "is_fast_retry": "is_fast_retry",
        "is_last_retry": "is_last_retry",
        "netpath": "netpath",
        "netstats": "netstats",
        "ocsp": "ocsp",
        "ping": "ping",
        "received_email_count": "received_email_count",
        "received_message": "received_message",
        "request": "request",
        "resolved_ip": "resolved_ip",
        "response": "response",
        "run_type": "run_type",
        "sent_message": "sent_message",
        "start_url": "start_url",
        "started_at": "started_at",
        "status": "status",
        "steps": "steps",
        "time_to_interactive": "time_to_interactive",
        "timings": "timings",
        "trace": "trace",
        "traceroute": "traceroute",
        "triggered_at": "triggered_at",
        "tunnel": "tunnel",
        "turns": "turns",
        "unhealthy": "unhealthy",
        "variables": "variables",
    }

    def __init__(
        self_,
        assertions: Union[List[SyntheticsTestResultAssertionResult], UnsetType] = unset,
        bucket_keys: Union[SyntheticsTestResultBucketKeys, UnsetType] = unset,
        call_type: Union[str, UnsetType] = unset,
        cert: Union[SyntheticsTestResultCertificate, UnsetType] = unset,
        compressed_json_descriptor: Union[str, UnsetType] = unset,
        compressed_steps: Union[str, UnsetType] = unset,
        connection_outcome: Union[str, UnsetType] = unset,
        dns_resolution: Union[SyntheticsTestResultDnsResolution, UnsetType] = unset,
        duration: Union[float, UnsetType] = unset,
        exited_on_step_success: Union[bool, UnsetType] = unset,
        failure: Union[SyntheticsTestResultFailure, UnsetType] = unset,
        finished_at: Union[int, UnsetType] = unset,
        handshake: Union[SyntheticsTestResultHandshake, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        initial_id: Union[str, UnsetType] = unset,
        is_fast_retry: Union[bool, UnsetType] = unset,
        is_last_retry: Union[bool, UnsetType] = unset,
        netpath: Union[SyntheticsTestResultNetpath, UnsetType] = unset,
        netstats: Union[SyntheticsTestResultNetstats, UnsetType] = unset,
        ocsp: Union[SyntheticsTestResultOCSPResponse, UnsetType] = unset,
        ping: Union[SyntheticsTestResultTracerouteHop, UnsetType] = unset,
        received_email_count: Union[int, UnsetType] = unset,
        received_message: Union[str, UnsetType] = unset,
        request: Union[SyntheticsTestResultRequestInfo, UnsetType] = unset,
        resolved_ip: Union[str, UnsetType] = unset,
        response: Union[SyntheticsTestResultResponseInfo, UnsetType] = unset,
        run_type: Union[SyntheticsTestResultRunType, UnsetType] = unset,
        sent_message: Union[str, UnsetType] = unset,
        start_url: Union[str, UnsetType] = unset,
        started_at: Union[int, UnsetType] = unset,
        status: Union[SyntheticsTestResultStatus, UnsetType] = unset,
        steps: Union[List[SyntheticsTestResultStep], UnsetType] = unset,
        time_to_interactive: Union[int, UnsetType] = unset,
        timings: Union[Dict[str, Any], UnsetType] = unset,
        trace: Union[SyntheticsTestResultTrace, UnsetType] = unset,
        traceroute: Union[List[SyntheticsTestResultTracerouteHop], UnsetType] = unset,
        triggered_at: Union[int, UnsetType] = unset,
        tunnel: Union[bool, UnsetType] = unset,
        turns: Union[List[SyntheticsTestResultTurn], UnsetType] = unset,
        unhealthy: Union[bool, UnsetType] = unset,
        variables: Union[SyntheticsTestResultVariables, UnsetType] = unset,
        **kwargs,
    ):
        """
        Full result details for a Synthetic test execution.

        :param assertions: Assertion results produced by the test.
        :type assertions: [SyntheticsTestResultAssertionResult], optional

        :param bucket_keys: Storage bucket keys for artifacts produced during a step or test.
        :type bucket_keys: SyntheticsTestResultBucketKeys, optional

        :param call_type: gRPC call type (for example, ``unary`` , ``healthCheck`` , or ``reflection`` ).
        :type call_type: str, optional

        :param cert: SSL/TLS certificate information returned from an SSL test.
        :type cert: SyntheticsTestResultCertificate, optional

        :param compressed_json_descriptor: Compressed JSON descriptor for the test (internal format).
        :type compressed_json_descriptor: str, optional

        :param compressed_steps: Compressed representation of the test steps (internal format).
        :type compressed_steps: str, optional

        :param connection_outcome: Outcome of the connection attempt (for example, ``established`` , ``refused`` ).
        :type connection_outcome: str, optional

        :param dns_resolution: DNS resolution details recorded during the test execution.
        :type dns_resolution: SyntheticsTestResultDnsResolution, optional

        :param duration: Duration of the test execution (in milliseconds).
        :type duration: float, optional

        :param exited_on_step_success: Whether the test exited early because a step marked with ``exitIfSucceed`` passed.
        :type exited_on_step_success: bool, optional

        :param failure: Details about the failure of a Synthetic test.
        :type failure: SyntheticsTestResultFailure, optional

        :param finished_at: Timestamp of when the test finished (in milliseconds).
        :type finished_at: int, optional

        :param handshake: Handshake request and response for protocol-level tests.
        :type handshake: SyntheticsTestResultHandshake, optional

        :param id: The unique identifier for this result.
        :type id: str, optional

        :param initial_id: The initial result ID before any retries.
        :type initial_id: str, optional

        :param is_fast_retry: Whether this result is from a fast retry.
        :type is_fast_retry: bool, optional

        :param is_last_retry: Whether this result is from the last retry.
        :type is_last_retry: bool, optional

        :param netpath: Network Path test result capturing the path between source and destination.
        :type netpath: SyntheticsTestResultNetpath, optional

        :param netstats: Aggregated network statistics from the test execution.
        :type netstats: SyntheticsTestResultNetstats, optional

        :param ocsp: OCSP response received while validating a certificate.
        :type ocsp: SyntheticsTestResultOCSPResponse, optional

        :param ping: A network probe result, used for traceroute hops and ping summaries.
        :type ping: SyntheticsTestResultTracerouteHop, optional

        :param received_email_count: Number of emails received during the test (email tests).
        :type received_email_count: int, optional

        :param received_message: Message received from the target (for WebSocket/TCP/UDP tests).
        :type received_message: str, optional

        :param request: Details of the outgoing request made during the test execution.
        :type request: SyntheticsTestResultRequestInfo, optional

        :param resolved_ip: IP address resolved for the target host.
        :type resolved_ip: str, optional

        :param response: Details of the response received during the test execution.
        :type response: SyntheticsTestResultResponseInfo, optional

        :param run_type: The type of run for a Synthetic test result.
        :type run_type: SyntheticsTestResultRunType, optional

        :param sent_message: Message sent to the target (for WebSocket/TCP/UDP tests).
        :type sent_message: str, optional

        :param start_url: Start URL for the test (browser tests).
        :type start_url: str, optional

        :param started_at: Timestamp of when the test started (in milliseconds).
        :type started_at: int, optional

        :param status: Status of a Synthetic test result.
        :type status: SyntheticsTestResultStatus, optional

        :param steps: Step results (for browser, mobile, and multistep API tests).
        :type steps: [SyntheticsTestResultStep], optional

        :param time_to_interactive: Time to interactive in milliseconds (browser tests).
        :type time_to_interactive: int, optional

        :param timings: Timing breakdown of the test request phases (for example, DNS, TCP, TLS, first byte).
        :type timings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param trace: Trace identifiers associated with a Synthetic test result.
        :type trace: SyntheticsTestResultTrace, optional

        :param traceroute: Traceroute hop results (for network tests).
        :type traceroute: [SyntheticsTestResultTracerouteHop], optional

        :param triggered_at: Timestamp of when the test was triggered (in milliseconds).
        :type triggered_at: int, optional

        :param tunnel: Whether the test was executed through a tunnel.
        :type tunnel: bool, optional

        :param turns: Turns executed by a goal-based browser test.
        :type turns: [SyntheticsTestResultTurn], optional

        :param unhealthy: Whether the test runner was unhealthy at the time of execution.
        :type unhealthy: bool, optional

        :param variables: Variables captured during a test step.
        :type variables: SyntheticsTestResultVariables, optional
        """
        if assertions is not unset:
            kwargs["assertions"] = assertions
        if bucket_keys is not unset:
            kwargs["bucket_keys"] = bucket_keys
        if call_type is not unset:
            kwargs["call_type"] = call_type
        if cert is not unset:
            kwargs["cert"] = cert
        if compressed_json_descriptor is not unset:
            kwargs["compressed_json_descriptor"] = compressed_json_descriptor
        if compressed_steps is not unset:
            kwargs["compressed_steps"] = compressed_steps
        if connection_outcome is not unset:
            kwargs["connection_outcome"] = connection_outcome
        if dns_resolution is not unset:
            kwargs["dns_resolution"] = dns_resolution
        if duration is not unset:
            kwargs["duration"] = duration
        if exited_on_step_success is not unset:
            kwargs["exited_on_step_success"] = exited_on_step_success
        if failure is not unset:
            kwargs["failure"] = failure
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if handshake is not unset:
            kwargs["handshake"] = handshake
        if id is not unset:
            kwargs["id"] = id
        if initial_id is not unset:
            kwargs["initial_id"] = initial_id
        if is_fast_retry is not unset:
            kwargs["is_fast_retry"] = is_fast_retry
        if is_last_retry is not unset:
            kwargs["is_last_retry"] = is_last_retry
        if netpath is not unset:
            kwargs["netpath"] = netpath
        if netstats is not unset:
            kwargs["netstats"] = netstats
        if ocsp is not unset:
            kwargs["ocsp"] = ocsp
        if ping is not unset:
            kwargs["ping"] = ping
        if received_email_count is not unset:
            kwargs["received_email_count"] = received_email_count
        if received_message is not unset:
            kwargs["received_message"] = received_message
        if request is not unset:
            kwargs["request"] = request
        if resolved_ip is not unset:
            kwargs["resolved_ip"] = resolved_ip
        if response is not unset:
            kwargs["response"] = response
        if run_type is not unset:
            kwargs["run_type"] = run_type
        if sent_message is not unset:
            kwargs["sent_message"] = sent_message
        if start_url is not unset:
            kwargs["start_url"] = start_url
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        if steps is not unset:
            kwargs["steps"] = steps
        if time_to_interactive is not unset:
            kwargs["time_to_interactive"] = time_to_interactive
        if timings is not unset:
            kwargs["timings"] = timings
        if trace is not unset:
            kwargs["trace"] = trace
        if traceroute is not unset:
            kwargs["traceroute"] = traceroute
        if triggered_at is not unset:
            kwargs["triggered_at"] = triggered_at
        if tunnel is not unset:
            kwargs["tunnel"] = tunnel
        if turns is not unset:
            kwargs["turns"] = turns
        if unhealthy is not unset:
            kwargs["unhealthy"] = unhealthy
        if variables is not unset:
            kwargs["variables"] = variables
        super().__init__(kwargs)
