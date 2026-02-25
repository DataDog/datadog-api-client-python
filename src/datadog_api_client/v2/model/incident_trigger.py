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
    from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit


class IncidentTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit

        return {
            "rate_limit": (TriggerRateLimit,),
            "version": (str,),
        }

    attribute_map = {
        "rate_limit": "rateLimit",
        "version": "version",
    }

    def __init__(
        self_, rate_limit: Union[TriggerRateLimit, UnsetType] = unset, version: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Trigger a workflow from an Incident. For automatic triggering a handle must be configured and the workflow must be published.

        :param rate_limit: Defines a rate limit for a trigger.
        :type rate_limit: TriggerRateLimit, optional

        :param version: Version of the incident trigger.
        :type version: str, optional
        """
        if rate_limit is not unset:
            kwargs["rate_limit"] = rate_limit
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
