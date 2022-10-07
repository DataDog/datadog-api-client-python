# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.notebook_response_data import NotebookResponseData


class NotebookResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_response_data import NotebookResponseData

        return {
            "data": (NotebookResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[NotebookResponseData, UnsetType] = unset, **kwargs):
        """
        The description of a notebook response.

        :param data: The data for a notebook.
        :type data: NotebookResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
