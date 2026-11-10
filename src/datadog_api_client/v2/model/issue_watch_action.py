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
    from datadog_api_client.v2.model.issue_state import IssueState
    from datadog_api_client.v2.model.issue_watch_action_kind import IssueWatchActionKind


class IssueWatchAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_state import IssueState
        from datadog_api_client.v2.model.issue_watch_action_kind import IssueWatchActionKind

        return {
            "_from": (IssueState,),
            "kind": (IssueWatchActionKind,),
            "to": (IssueState,),
        }

    attribute_map = {
        "_from": "from",
        "kind": "kind",
        "to": "to",
    }

    def __init__(
        self_,
        kind: IssueWatchActionKind,
        _from: Union[IssueState, UnsetType] = unset,
        to: Union[IssueState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Action applied to the issue when the watch condition is met.

        :param _from: State of the issue
        :type _from: IssueState, optional

        :param kind: Kind of watch action.
        :type kind: IssueWatchActionKind

        :param to: State of the issue
        :type to: IssueState, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)

        self_.kind = kind
