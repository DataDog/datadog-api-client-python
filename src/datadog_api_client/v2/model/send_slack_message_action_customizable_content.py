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


class SendSlackMessageActionCustomizableContent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_description": (bool,),
            "include_source": (bool,),
            "mirror_replies": (bool,),
            "thread_timeline": (bool,),
        }

    attribute_map = {
        "include_description": "include_description",
        "include_source": "include_source",
        "mirror_replies": "mirror_replies",
        "thread_timeline": "thread_timeline",
    }

    def __init__(
        self_,
        include_description: Union[bool, UnsetType] = unset,
        include_source: Union[bool, UnsetType] = unset,
        mirror_replies: Union[bool, UnsetType] = unset,
        thread_timeline: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options that customize the content of the Slack message sent for a Page.

        :param include_description: Whether to include the Page description in the Slack message.
        :type include_description: bool, optional

        :param include_source: Whether to include the source that triggered the Page in the Slack message.
        :type include_source: bool, optional

        :param mirror_replies: Whether to mirror replies posted in the Slack message thread to the Page timeline.
        :type mirror_replies: bool, optional

        :param thread_timeline: Whether to post Page timeline updates as replies in the Slack message thread.
        :type thread_timeline: bool, optional
        """
        if include_description is not unset:
            kwargs["include_description"] = include_description
        if include_source is not unset:
            kwargs["include_source"] = include_source
        if mirror_replies is not unset:
            kwargs["mirror_replies"] = mirror_replies
        if thread_timeline is not unset:
            kwargs["thread_timeline"] = thread_timeline
        super().__init__(kwargs)
