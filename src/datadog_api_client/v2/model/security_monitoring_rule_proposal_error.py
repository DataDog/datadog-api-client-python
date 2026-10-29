# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringRuleProposalError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "kind": (str,),
            "message": (str,),
            "type": (str,),
        }

    attribute_map = {
        "kind": "kind",
        "message": "message",
        "type": "type",
    }

    def __init__(
        self_, kind: str, message: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The reason no rule could be generated. Only present when the status is ``failed``.

        :param kind: The kind of failure.

            * ``translation_error`` : no rule could be generated from the input. Reword the input
              or add details, then start a new rule proposal.
            * ``internal_error`` : the proposal failed because of an internal error. Start a new
              rule proposal to try again.
        :type kind: str

        :param message: A human-readable explanation of why no rule could be generated, when available.
        :type message: str, optional

        :param type: The type of failure within its kind, such as ``NoRuleProduced``.
        :type type: str, optional
        """
        if message is not unset:
            kwargs["message"] = message
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.kind = kind
