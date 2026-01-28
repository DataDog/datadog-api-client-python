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
    from datadog_api_client.v2.model.project_columns_config_columns_items_sort import (
        ProjectColumnsConfigColumnsItemsSort,
    )


class ProjectColumnsConfigColumnsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_columns_config_columns_items_sort import (
            ProjectColumnsConfigColumnsItemsSort,
        )

        return {
            "sort": (ProjectColumnsConfigColumnsItemsSort,),
            "sort_field": (str,),
            "type": (str,),
        }

    attribute_map = {
        "sort": "sort",
        "sort_field": "sort_field",
        "type": "type",
    }

    def __init__(
        self_,
        sort: Union[ProjectColumnsConfigColumnsItemsSort, UnsetType] = unset,
        sort_field: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param sort:
        :type sort: ProjectColumnsConfigColumnsItemsSort, optional

        :param sort_field:
        :type sort_field: str, optional

        :param type:
        :type type: str, optional
        """
        if sort is not unset:
            kwargs["sort"] = sort
        if sort_field is not unset:
            kwargs["sort_field"] = sort_field
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
