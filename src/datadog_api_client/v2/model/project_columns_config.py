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
    from datadog_api_client.v2.model.project_columns_config_columns_items import ProjectColumnsConfigColumnsItems


class ProjectColumnsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_columns_config_columns_items import ProjectColumnsConfigColumnsItems

        return {
            "columns": ([ProjectColumnsConfigColumnsItems],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(self_, columns: Union[List[ProjectColumnsConfigColumnsItems], UnsetType] = unset, **kwargs):
        """
        Project columns configuration

        :param columns:
        :type columns: [ProjectColumnsConfigColumnsItems], optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        super().__init__(kwargs)
