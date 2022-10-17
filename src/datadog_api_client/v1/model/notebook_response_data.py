# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v1.model.notebook_author import NotebookAuthor
from datadog_api_client.v1.model.notebook_cell_response import NotebookCellResponse
from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
from datadog_api_client.v1.model.notebook_response_data_attributes import NotebookResponseDataAttributes
from datadog_api_client.v1.model.notebook_author import NotebookAuthor
from datadog_api_client.v1.model.notebook_cell_response import NotebookCellResponse
from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.notebook_absolute_time import NotebookAbsoluteTime

if TYPE_CHECKING:
    from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType


@dataclass
class NotebookResponseDataJSON:
    id: str
    author: Union[NotebookAuthor, UnsetType] = unset
    cells: Union[List[NotebookCellResponse], UnsetType] = unset
    created: Union[datetime, UnsetType] = unset
    metadata: Union[NotebookMetadata, UnsetType] = unset
    modified: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    status: Union[NotebookStatus, UnsetType] = unset
    time: Union[NotebookGlobalTime, NotebookRelativeTime, NotebookAbsoluteTime, UnsetType] = unset


class NotebookResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType

        return {
            "attributes": (NotebookResponseDataAttributes,),
            "id": (int,),
            "type": (NotebookResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }
    json_api_model = NotebookResponseDataJSON

    def __init__(self_, attributes: NotebookResponseDataAttributes, id: int, type: NotebookResourceType, **kwargs):
        """
        The data for a notebook.

        :param attributes: The attributes of a notebook.
        :type attributes: NotebookResponseDataAttributes

        :param id: Unique notebook ID, assigned when you create the notebook.
        :type id: int

        :param type: Type of the Notebook resource.
        :type type: NotebookResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
