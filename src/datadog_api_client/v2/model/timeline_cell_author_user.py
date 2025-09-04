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
    from datadog_api_client.v2.model.timeline_cell_author_user_content import TimelineCellAuthorUserContent
    from datadog_api_client.v2.model.timeline_cell_author_user_type import TimelineCellAuthorUserType


class TimelineCellAuthorUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeline_cell_author_user_content import TimelineCellAuthorUserContent
        from datadog_api_client.v2.model.timeline_cell_author_user_type import TimelineCellAuthorUserType

        return {
            "content": (TimelineCellAuthorUserContent,),
            "type": (TimelineCellAuthorUserType,),
        }

    attribute_map = {
        "content": "content",
        "type": "type",
    }

    def __init__(
        self_,
        content: Union[TimelineCellAuthorUserContent, UnsetType] = unset,
        type: Union[TimelineCellAuthorUserType, UnsetType] = unset,
        **kwargs,
    ):
        """
        timeline cell user author

        :param content: user author content.
        :type content: TimelineCellAuthorUserContent, optional

        :param type: user author type.
        :type type: TimelineCellAuthorUserType, optional
        """
        if content is not unset:
            kwargs["content"] = content
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
