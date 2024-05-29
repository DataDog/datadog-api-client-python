# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_query_payload_data import (
        SecurityMonitoringRuleQueryPayloadData,
    )


class SecurityMonitoringRuleQueryPayload(ModelNormal):
    validations = {
        "index": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_payload_data import (
            SecurityMonitoringRuleQueryPayloadData,
        )

        return {
            "expected_result": (bool,),
            "index": (int,),
            "payload": (SecurityMonitoringRuleQueryPayloadData,),
        }

    attribute_map = {
        "expected_result": "expectedResult",
        "index": "index",
        "payload": "payload",
    }

    def __init__(
        self_,
        expected_result: Union[bool, UnsetType] = unset,
        index: Union[int, UnsetType] = unset,
        payload: Union[SecurityMonitoringRuleQueryPayloadData, UnsetType] = unset,
        **kwargs,
    ):
        """
        Payload to test a rule query with the expected result.

        :param expected_result: Expected result of the test.
        :type expected_result: bool, optional

        :param index: Index of the query under test.
        :type index: int, optional

        :param payload: Payload used to test the rule query.
        :type payload: SecurityMonitoringRuleQueryPayloadData, optional
        """
        if expected_result is not unset:
            kwargs["expected_result"] = expected_result
        if index is not unset:
            kwargs["index"] = index
        if payload is not unset:
            kwargs["payload"] = payload
        super().__init__(kwargs)
