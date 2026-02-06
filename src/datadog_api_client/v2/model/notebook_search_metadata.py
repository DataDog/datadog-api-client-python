# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notebook_search_user import NotebookSearchUser


class NotebookSearchMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notebook_search_user import NotebookSearchUser

        return {
            "author": (NotebookSearchUser,),
            "cell_count": (int,),
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "experience_type": (str, none_type),
            "has_computational_cells": (bool,),
            "is_favorited": (bool,),
            "is_template": (bool,),
            "modified_at": (datetime,),
            "status": (str,),
            "take_snapshots": (bool,),
            "type": (str,),
        }

    attribute_map = {
        "author": "author",
        "cell_count": "cell_count",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "experience_type": "experience_type",
        "has_computational_cells": "has_computational_cells",
        "is_favorited": "is_favorited",
        "is_template": "is_template",
        "modified_at": "modified_at",
        "status": "status",
        "take_snapshots": "take_snapshots",
        "type": "type",
    }

    def __init__(
        self_,
        author: NotebookSearchUser,
        cell_count: int,
        created_at: datetime,
        deleted_at: Union[datetime, none_type],
        experience_type: Union[str, none_type],
        has_computational_cells: bool,
        is_favorited: bool,
        is_template: bool,
        modified_at: datetime,
        status: str,
        take_snapshots: bool,
        type: str,
        **kwargs,
    ):
        """
        Metadata about the notebook.

        :param author: User information.
        :type author: NotebookSearchUser

        :param cell_count: Number of cells in the notebook.
        :type cell_count: int

        :param created_at: Time at which the notebook was created.
        :type created_at: datetime

        :param deleted_at: Time at which the notebook was deleted, or null if not deleted.
        :type deleted_at: datetime, none_type

        :param experience_type: Experience type of the notebook.
        :type experience_type: str, none_type

        :param has_computational_cells: Whether the notebook has computational cells.
        :type has_computational_cells: bool

        :param is_favorited: Whether the notebook is favorited by the user.
        :type is_favorited: bool

        :param is_template: Whether the notebook is a template.
        :type is_template: bool

        :param modified_at: Time at which the notebook was last updated.
        :type modified_at: datetime

        :param status: Status of the notebook.
        :type status: str

        :param take_snapshots: Whether the notebook can take a snapshot.
        :type take_snapshots: bool

        :param type: Notebook type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.author = author
        self_.cell_count = cell_count
        self_.created_at = created_at
        self_.deleted_at = deleted_at
        self_.experience_type = experience_type
        self_.has_computational_cells = has_computational_cells
        self_.is_favorited = is_favorited
        self_.is_template = is_template
        self_.modified_at = modified_at
        self_.status = status
        self_.take_snapshots = take_snapshots
        self_.type = type
