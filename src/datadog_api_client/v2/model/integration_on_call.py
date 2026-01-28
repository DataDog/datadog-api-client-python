# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.integration_on_call_escalation_queries_items import (
        IntegrationOnCallEscalationQueriesItems,
    )


class IntegrationOnCall(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_on_call_escalation_queries_items import (
            IntegrationOnCallEscalationQueriesItems,
        )

        return {
            "auto_assign_on_call": (bool,),
            "enabled": (bool,),
            "escalation_queries": ([IntegrationOnCallEscalationQueriesItems],),
        }

    attribute_map = {
        "auto_assign_on_call": "auto_assign_on_call",
        "enabled": "enabled",
        "escalation_queries": "escalation_queries",
    }

    def __init__(
        self_,
        auto_assign_on_call: Union[bool, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        escalation_queries: Union[List[IntegrationOnCallEscalationQueriesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        On-Call integration settings

        :param auto_assign_on_call: Whether to auto-assign on-call
        :type auto_assign_on_call: bool, optional

        :param enabled: Whether On-Call integration is enabled
        :type enabled: bool, optional

        :param escalation_queries:
        :type escalation_queries: [IntegrationOnCallEscalationQueriesItems], optional
        """
        if auto_assign_on_call is not unset:
            kwargs["auto_assign_on_call"] = auto_assign_on_call
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if escalation_queries is not unset:
            kwargs["escalation_queries"] = escalation_queries
        super().__init__(kwargs)
