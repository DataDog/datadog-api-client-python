# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.notebook_create_data import NotebookCreateData
    from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
    from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
    from datadog_api_client.v1.model.notebook_status import NotebookStatus
    from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
    from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
    from datadog_api_client.v1.model.notebook_absolute_time import NotebookAbsoluteTime


@dataclass
class NotebookCreateRequestJSON:
    cells: Union[List[NotebookCellCreateRequest], UnsetType] = unset
    metadata: Union[NotebookMetadata, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    status: Union[NotebookStatus, UnsetType] = unset
    time: Union[NotebookGlobalTime, NotebookRelativeTime, NotebookAbsoluteTime, UnsetType] = unset


class NotebookCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_create_data import NotebookCreateData

        return {
            "data": (NotebookCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = NotebookCreateRequestJSON

    def __init__(self_, data: NotebookCreateData, **kwargs):
        """
        The description of a notebook create request.

        :param data: The data for a notebook create request.
        :type data: NotebookCreateData
        """
        super().__init__(kwargs)

        self_.data = data
