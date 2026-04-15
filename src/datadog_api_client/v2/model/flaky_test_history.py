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
    from datadog_api_client.v2.model.flaky_test_history_policy_id import FlakyTestHistoryPolicyId
    from datadog_api_client.v2.model.flaky_test_history_policy_meta import FlakyTestHistoryPolicyMeta


class FlakyTestHistory(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_test_history_policy_id import FlakyTestHistoryPolicyId
        from datadog_api_client.v2.model.flaky_test_history_policy_meta import FlakyTestHistoryPolicyMeta

        return {
            "commit_sha": (str,),
            "policy_id": (FlakyTestHistoryPolicyId,),
            "policy_meta": (FlakyTestHistoryPolicyMeta,),
            "status": (str,),
            "timestamp": (int,),
        }

    attribute_map = {
        "commit_sha": "commit_sha",
        "policy_id": "policy_id",
        "policy_meta": "policy_meta",
        "status": "status",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        commit_sha: str,
        status: str,
        timestamp: int,
        policy_id: Union[FlakyTestHistoryPolicyId, UnsetType] = unset,
        policy_meta: Union[FlakyTestHistoryPolicyMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single history entry representing a status change for a flaky test.

        :param commit_sha: The commit SHA associated with this status change. Will be an empty string if the commit SHA is not available.
        :type commit_sha: str

        :param policy_id: The policy that triggered this status change.
        :type policy_id: FlakyTestHistoryPolicyId, optional

        :param policy_meta: Metadata about the policy that triggered this status change.
        :type policy_meta: FlakyTestHistoryPolicyMeta, optional

        :param status: The test status at this point in history.
        :type status: str

        :param timestamp: Unix timestamp in milliseconds when this status change occurred.
        :type timestamp: int
        """
        if policy_id is not unset:
            kwargs["policy_id"] = policy_id
        if policy_meta is not unset:
            kwargs["policy_meta"] = policy_meta
        super().__init__(kwargs)

        self_.commit_sha = commit_sha
        self_.status = status
        self_.timestamp = timestamp
