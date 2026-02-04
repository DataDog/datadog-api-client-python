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
    from datadog_api_client.v2.model.notebook_search_highlight import NotebookSearchHighlight
    from datadog_api_client.v2.model.notebook_search_attributes import NotebookSearchAttributes
    from datadog_api_client.v2.model.metric_notebook_type import MetricNotebookType


class NotebookSearchResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notebook_search_highlight import NotebookSearchHighlight
        from datadog_api_client.v2.model.notebook_search_attributes import NotebookSearchAttributes
        from datadog_api_client.v2.model.metric_notebook_type import MetricNotebookType

        return {
            "highlight": (NotebookSearchHighlight,),
            "id": (str,),
            "notebook_data": (NotebookSearchAttributes,),
            "type": (MetricNotebookType,),
        }

    attribute_map = {
        "highlight": "highlight",
        "id": "id",
        "notebook_data": "notebook_data",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        notebook_data: NotebookSearchAttributes,
        type: MetricNotebookType,
        highlight: Union[NotebookSearchHighlight, UnsetType] = unset,
        **kwargs,
    ):
        """
        A notebook search result.

        :param highlight: Highlighted fields from the notebook search.
        :type highlight: NotebookSearchHighlight, optional

        :param id: Notebook identifier.
        :type id: str

        :param notebook_data: Notebook search result attributes.
        :type notebook_data: NotebookSearchAttributes

        :param type: Notebook resource type.
        :type type: MetricNotebookType
        """
        if highlight is not unset:
            kwargs["highlight"] = highlight
        super().__init__(kwargs)

        self_.id = id
        self_.notebook_data = notebook_data
        self_.type = type
