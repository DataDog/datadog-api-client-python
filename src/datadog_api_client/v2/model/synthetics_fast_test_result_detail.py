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
    from datadog_api_client.v2.model.synthetics_test_result_certificate import SyntheticsTestResultCertificate
    from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
    from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
    from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
    from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
    from datadog_api_client.v2.model.synthetics_test_result_step import SyntheticsTestResultStep
    from datadog_api_client.v2.model.synthetics_test_result_traceroute_hop import SyntheticsTestResultTracerouteHop


class SyntheticsFastTestResultDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_assertion_result import (
            SyntheticsTestResultAssertionResult,
        )
        from datadog_api_client.v2.model.synthetics_test_result_certificate import SyntheticsTestResultCertificate
        from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
        from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
        from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
        from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
        from datadog_api_client.v2.model.synthetics_test_result_step import SyntheticsTestResultStep
        from datadog_api_client.v2.model.synthetics_test_result_traceroute_hop import SyntheticsTestResultTracerouteHop

        return {
            "assertions": ([SyntheticsTestResultAssertionResult],),
            "call_type": (str,),
            "cert": (SyntheticsTestResultCertificate,),
            "duration": (float,),
            "failure": (SyntheticsTestResultFailure,),
            "finished_at": (int,),
            "id": (str,),
            "is_fast_retry": (bool,),
            "request": (SyntheticsTestResultRequestInfo,),
            "resolved_ip": (str,),
            "response": (SyntheticsTestResultResponseInfo,),
            "run_type": (SyntheticsTestResultRunType,),
            "started_at": (int,),
            "status": (str,),
            "steps": ([SyntheticsTestResultStep],),
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
            "traceroute": ([SyntheticsTestResultTracerouteHop],),
            "triggered_at": (int,),
            "tunnel": (bool,),
        }

    attribute_map = {
        "assertions": "assertions",
        "call_type": "call_type",
        "cert": "cert",
        "duration": "duration",
        "failure": "failure",
        "finished_at": "finished_at",
        "id": "id",
        "is_fast_retry": "is_fast_retry",
        "request": "request",
        "resolved_ip": "resolved_ip",
        "response": "response",
        "run_type": "run_type",
        "started_at": "started_at",
        "status": "status",
        "steps": "steps",
        "timings": "timings",
        "traceroute": "traceroute",
        "triggered_at": "triggered_at",
        "tunnel": "tunnel",
    }

    def __init__(
        self_,
        assertions: Union[List[SyntheticsTestResultAssertionResult], UnsetType] = unset,
        call_type: Union[str, UnsetType] = unset,
        cert: Union[SyntheticsTestResultCertificate, UnsetType] = unset,
        duration: Union[float, UnsetType] = unset,
        failure: Union[SyntheticsTestResultFailure, UnsetType] = unset,
        finished_at: Union[int, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_fast_retry: Union[bool, UnsetType] = unset,
        request: Union[SyntheticsTestResultRequestInfo, UnsetType] = unset,
        resolved_ip: Union[str, UnsetType] = unset,
        response: Union[SyntheticsTestResultResponseInfo, UnsetType] = unset,
        run_type: Union[SyntheticsTestResultRunType, UnsetType] = unset,
        started_at: Union[int, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        steps: Union[List[SyntheticsTestResultStep], UnsetType] = unset,
        timings: Union[Dict[str, Any], UnsetType] = unset,
        traceroute: Union[List[SyntheticsTestResultTracerouteHop], UnsetType] = unset,
        triggered_at: Union[int, UnsetType] = unset,
        tunnel: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Detailed result data for the fast test run. The exact shape of nested fields
        ( ``request`` , ``response`` , ``assertions`` , etc.) depends on the test subtype.

        :param assertions: Results of each assertion evaluated during the test.
        :type assertions: [SyntheticsTestResultAssertionResult], optional

        :param call_type: gRPC call type (for example, ``unary`` , ``healthCheck`` , or ``reflection`` ).
        :type call_type: str, optional

        :param cert: SSL/TLS certificate information returned from an SSL test.
        :type cert: SyntheticsTestResultCertificate, optional

        :param duration: Total duration of the test in milliseconds.
        :type duration: float, optional

        :param failure: Details about the failure of a Synthetic test.
        :type failure: SyntheticsTestResultFailure, optional

        :param finished_at: Unix timestamp (ms) of when the test finished.
        :type finished_at: int, optional

        :param id: The result ID. Set to the fast test UUID because no persistent result ID exists for fast tests.
        :type id: str, optional

        :param is_fast_retry: Whether this result is from an automatic fast retry.
        :type is_fast_retry: bool, optional

        :param request: Details of the outgoing request made during the test execution.
        :type request: SyntheticsTestResultRequestInfo, optional

        :param resolved_ip: IP address resolved for the target host.
        :type resolved_ip: str, optional

        :param response: Details of the response received during the test execution.
        :type response: SyntheticsTestResultResponseInfo, optional

        :param run_type: The type of run for a Synthetic test result.
        :type run_type: SyntheticsTestResultRunType, optional

        :param started_at: Unix timestamp (ms) of when the test started.
        :type started_at: int, optional

        :param status: Status of the test result ( ``passed`` or ``failed`` ).
        :type status: str, optional

        :param steps: Step results for multistep API tests.
        :type steps: [SyntheticsTestResultStep], optional

        :param timings: Timing breakdown of the test request phases (for example, DNS, TCP, TLS, first byte).
        :type timings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param traceroute: Traceroute hop results, present for ICMP and TCP tests.
        :type traceroute: [SyntheticsTestResultTracerouteHop], optional

        :param triggered_at: Unix timestamp (ms) of when the test was triggered.
        :type triggered_at: int, optional

        :param tunnel: Whether the test was run through a Synthetics tunnel.
        :type tunnel: bool, optional
        """
        if assertions is not unset:
            kwargs["assertions"] = assertions
        if call_type is not unset:
            kwargs["call_type"] = call_type
        if cert is not unset:
            kwargs["cert"] = cert
        if duration is not unset:
            kwargs["duration"] = duration
        if failure is not unset:
            kwargs["failure"] = failure
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if id is not unset:
            kwargs["id"] = id
        if is_fast_retry is not unset:
            kwargs["is_fast_retry"] = is_fast_retry
        if request is not unset:
            kwargs["request"] = request
        if resolved_ip is not unset:
            kwargs["resolved_ip"] = resolved_ip
        if response is not unset:
            kwargs["response"] = response
        if run_type is not unset:
            kwargs["run_type"] = run_type
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        if steps is not unset:
            kwargs["steps"] = steps
        if timings is not unset:
            kwargs["timings"] = timings
        if traceroute is not unset:
            kwargs["traceroute"] = traceroute
        if triggered_at is not unset:
            kwargs["triggered_at"] = triggered_at
        if tunnel is not unset:
            kwargs["tunnel"] = tunnel
        super().__init__(kwargs)
