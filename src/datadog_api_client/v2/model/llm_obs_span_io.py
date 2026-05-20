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
    from datadog_api_client.v2.model.llm_obs_span_message import LLMObsSpanMessage


class LLMObsSpanIO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_message import LLMObsSpanMessage

        return {
            "messages": ([LLMObsSpanMessage],),
            "value": (str,),
        }

    attribute_map = {
        "messages": "messages",
        "value": "value",
    }

    def __init__(
        self_,
        messages: Union[List[LLMObsSpanMessage], UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Input or output content of an LLM Observability span.

        :param messages: List of messages in the input or output.
        :type messages: [LLMObsSpanMessage], optional

        :param value: Plain-text value of the input or output.
        :type value: str, optional
        """
        if messages is not unset:
            kwargs["messages"] = messages
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
