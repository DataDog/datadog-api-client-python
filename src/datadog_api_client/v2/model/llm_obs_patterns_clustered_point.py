# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsPatternsClusteredPoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_id": (str,),
            "id": (str,),
            "input": (str,),
            "is_included": (bool,),
            "is_suggested": (bool,),
            "session_id": (str,),
            "span_id": (str,),
            "topic_id": (str,),
        }

    attribute_map = {
        "event_id": "event_id",
        "id": "id",
        "input": "input",
        "is_included": "is_included",
        "is_suggested": "is_suggested",
        "session_id": "session_id",
        "span_id": "span_id",
        "topic_id": "topic_id",
    }

    def __init__(
        self_,
        event_id: str,
        id: str,
        input: str,
        is_included: bool,
        is_suggested: bool,
        session_id: str,
        span_id: str,
        topic_id: str,
        **kwargs,
    ):
        """
        A single data point grouped into a topic.

        :param event_id: Identifier of the source event.
        :type event_id: str

        :param id: Unique identifier of the clustered point.
        :type id: str

        :param input: Input text of the source span.
        :type input: str

        :param is_included: Whether the point is included in the patterns dataset.
        :type is_included: bool

        :param is_suggested: Whether the point is suggested for inclusion in the patterns dataset.
        :type is_suggested: bool

        :param session_id: Identifier of the source session.
        :type session_id: str

        :param span_id: Identifier of the source span.
        :type span_id: str

        :param topic_id: Identifier of the topic the point belongs to.
        :type topic_id: str
        """
        super().__init__(kwargs)

        self_.event_id = event_id
        self_.id = id
        self_.input = input
        self_.is_included = is_included
        self_.is_suggested = is_suggested
        self_.session_id = session_id
        self_.span_id = span_id
        self_.topic_id = topic_id
