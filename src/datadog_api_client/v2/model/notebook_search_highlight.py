# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class NotebookSearchHighlight(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cells_text": ([str],),
            "cells_title": ([str],),
            "name": ([str],),
        }

    attribute_map = {
        "cells_text": "cells.text",
        "cells_title": "cells.title",
        "name": "name",
    }

    def __init__(
        self_,
        cells_text: Union[List[str], UnsetType] = unset,
        cells_title: Union[List[str], UnsetType] = unset,
        name: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Highlighted fields from the notebook search.

        :param cells_text: Highlighted cell text matches.
        :type cells_text: [str], optional

        :param cells_title: Highlighted cell title matches.
        :type cells_title: [str], optional

        :param name: Highlighted notebook name matches.
        :type name: [str], optional
        """
        if cells_text is not unset:
            kwargs["cells_text"] = cells_text
        if cells_title is not unset:
            kwargs["cells_title"] = cells_title
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
