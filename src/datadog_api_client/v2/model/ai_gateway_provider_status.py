# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_provider_status_state import AiGatewayProviderStatusState


class AiGatewayProviderStatus(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_status_state import AiGatewayProviderStatusState

        return {
            "checked_at": (datetime,),
            "endpoint": (str,),
            "fix": (str,),
            "http_status": (int,),
            "label": (str,),
            "last_ok_at": (datetime,),
            "message": (str,),
            "reason": (str,),
            "state": (AiGatewayProviderStatusState,),
        }

    attribute_map = {
        "checked_at": "checked_at",
        "endpoint": "endpoint",
        "fix": "fix",
        "http_status": "http_status",
        "label": "label",
        "last_ok_at": "last_ok_at",
        "message": "message",
        "reason": "reason",
        "state": "state",
    }

    def __init__(
        self_,
        state: AiGatewayProviderStatusState,
        checked_at: Union[datetime, UnsetType] = unset,
        endpoint: Union[str, UnsetType] = unset,
        fix: Union[str, UnsetType] = unset,
        http_status: Union[int, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        last_ok_at: Union[datetime, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Read-only. Whether the provider is working, based on the model sync and live calls. Omitted for
        providers that are never checked, which include providers without an integration account, and
        Azure OpenAI and Gemini providers until live traffic records a status.

        :param checked_at: Time of the last observation.
        :type checked_at: datetime, optional

        :param endpoint: Address of the models endpoint that the gateway called, for custom providers.
        :type endpoint: str, optional

        :param fix: Display text saying how to fix the provider. Clients render it as-is.
        :type fix: str, optional

        :param http_status: HTTP status code that the provider returned.
        :type http_status: int, optional

        :param label: Display text for the reason. Clients render it as-is.
        :type label: str, optional

        :param last_ok_at: Time of the last observation in which the provider worked.
        :type last_ok_at: datetime, optional

        :param message: The provider's own error message, with credentials removed. Never set for custom providers.
        :type message: str, optional

        :param reason: Why the provider is invalid, as a stable code such as ``credentials_rejected``. Set only when ``state`` is ``invalid``.
        :type reason: str, optional

        :param state: Whether the provider is working. ``checking`` means no observation has been recorded yet, not that a
            check is running.
        :type state: AiGatewayProviderStatusState
        """
        if checked_at is not unset:
            kwargs["checked_at"] = checked_at
        if endpoint is not unset:
            kwargs["endpoint"] = endpoint
        if fix is not unset:
            kwargs["fix"] = fix
        if http_status is not unset:
            kwargs["http_status"] = http_status
        if label is not unset:
            kwargs["label"] = label
        if last_ok_at is not unset:
            kwargs["last_ok_at"] = last_ok_at
        if message is not unset:
            kwargs["message"] = message
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.state = state
