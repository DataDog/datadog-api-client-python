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
    from datadog_api_client.v1.model.notebook_update_data import NotebookUpdateData
    from datadog_api_client.v1.model.notebook_update_cell import NotebookUpdateCell
    from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
    from datadog_api_client.v1.model.notebook_status import NotebookStatus
    from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
    from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
    from datadog_api_client.v1.model.notebook_cell_update_request import NotebookCellUpdateRequest
    from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
    from datadog_api_client.v1.model.notebook_absolute_time import NotebookAbsoluteTime


@dataclass
class NotebookUpdateRequestJSON:
    cells: Union[
        List[Union[NotebookUpdateCell, NotebookCellCreateRequest, NotebookCellUpdateRequest]], UnsetType
    ] = unset
    metadata: Union[NotebookMetadata, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    status: Union[NotebookStatus, UnsetType] = unset
    time: Union[NotebookGlobalTime, NotebookRelativeTime, NotebookAbsoluteTime, UnsetType] = unset


class NotebookUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_update_data import NotebookUpdateData

        return {
            "data": (NotebookUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = NotebookUpdateRequestJSON

    def __init__(self_, data: NotebookUpdateData, **kwargs):
        """
        The description of a notebook update request.

        :param data: The data for a notebook update request.
        :type data: NotebookUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
