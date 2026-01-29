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
    from datadog_api_client.v2.model.integration_on_call_escalation_queries_items_target import (
        IntegrationOnCallEscalationQueriesItemsTarget,
    )


class IntegrationOnCallEscalationQueriesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_on_call_escalation_queries_items_target import (
            IntegrationOnCallEscalationQueriesItemsTarget,
        )

        return {
            "enabled": (bool,),
            "id": (str,),
            "query": (str,),
            "target": (IntegrationOnCallEscalationQueriesItemsTarget,),
        }

    attribute_map = {
        "enabled": "enabled",
        "id": "id",
        "query": "query",
        "target": "target",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        target: Union[IntegrationOnCallEscalationQueriesItemsTarget, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param enabled:
        :type enabled: bool, optional

        :param id:
        :type id: str, optional

        :param query:
        :type query: str, optional

        :param target:
        :type target: IntegrationOnCallEscalationQueriesItemsTarget, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if id is not unset:
            kwargs["id"] = id
        if query is not unset:
            kwargs["query"] = query
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)
