# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.replay_summary_chapter import ReplaySummaryChapter


class ReplaySummaryDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_summary_chapter import ReplaySummaryChapter

        return {
            "chapters": ([ReplaySummaryChapter],),
            "has_enough_activity": (bool,),
            "has_too_many_events": (bool,),
            "summary": (str,),
            "version": (str,),
        }

    attribute_map = {
        "chapters": "chapters",
        "has_enough_activity": "has_enough_activity",
        "has_too_many_events": "has_too_many_events",
        "summary": "summary",
        "version": "version",
    }

    def __init__(
        self_,
        chapters: List[ReplaySummaryChapter],
        has_enough_activity: bool,
        has_too_many_events: bool,
        summary: str,
        version: str,
        **kwargs,
    ):
        """
        Attributes of a RUM replay summary response.

        :param chapters: List of chapters breaking down the session into distinct activity segments.
        :type chapters: [ReplaySummaryChapter]

        :param has_enough_activity: Whether the session contained sufficient user activity to generate a summary.
        :type has_enough_activity: bool

        :param has_too_many_events: Whether the session exceeded the event count limit for summary generation.
        :type has_too_many_events: bool

        :param summary: AI-generated summary of the replay session.
        :type summary: str

        :param version: Version of the prompt used to generate the summary.
        :type version: str
        """
        super().__init__(kwargs)

        self_.chapters = chapters
        self_.has_enough_activity = has_enough_activity
        self_.has_too_many_events = has_too_many_events
        self_.summary = summary
        self_.version = version
