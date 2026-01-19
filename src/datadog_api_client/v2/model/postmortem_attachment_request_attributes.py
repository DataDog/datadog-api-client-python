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
    from datadog_api_client.v2.model.postmortem_cell import PostmortemCell


class PostmortemAttachmentRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_cell import PostmortemCell

        return {
            "cells": ([PostmortemCell],),
            "content": (str,),
            "postmortem_template_id": (str,),
            "title": (str,),
        }

    attribute_map = {
        "cells": "cells",
        "content": "content",
        "postmortem_template_id": "postmortem_template_id",
        "title": "title",
    }

    def __init__(
        self_,
        cells: Union[List[PostmortemCell], UnsetType] = unset,
        content: Union[str, UnsetType] = unset,
        postmortem_template_id: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Postmortem attachment attributes

        :param cells: The cells of the postmortem
        :type cells: [PostmortemCell], optional

        :param content: The content of the postmortem
        :type content: str, optional

        :param postmortem_template_id: The ID of the postmortem template
        :type postmortem_template_id: str, optional

        :param title: The title of the postmortem
        :type title: str, optional
        """
        if cells is not unset:
            kwargs["cells"] = cells
        if content is not unset:
            kwargs["content"] = content
        if postmortem_template_id is not unset:
            kwargs["postmortem_template_id"] = postmortem_template_id
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
