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
    from datadog_api_client.v2.model.tls import Tls
    from datadog_api_client.v2.model.datadog_agent_source_type import DatadogAgentSourceType


class DatadogAgentSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tls import Tls
        from datadog_api_client.v2.model.datadog_agent_source_type import DatadogAgentSourceType

        return {
            "id": (str,),
            "tls": (Tls,),
            "type": (DatadogAgentSourceType,),
        }

    attribute_map = {
        "id": "id",
        "tls": "tls",
        "type": "type",
    }

    def __init__(self_, id: str, type: DatadogAgentSourceType, tls: Union[Tls, UnsetType] = unset, **kwargs):
        """
        A Datadog Agent source component.

        :param id: The unique ID of the source.
        :type id: str

        :param tls: TLS settings
        :type tls: Tls, optional

        :param type: The type of source.
        :type type: DatadogAgentSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
