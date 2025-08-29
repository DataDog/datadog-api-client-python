# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.datastore_item_conflict_mode import DatastoreItemConflictMode


class BulkPutAppsDatastoreItemsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datastore_item_conflict_mode import DatastoreItemConflictMode

        return {
            "conflict_mode": (DatastoreItemConflictMode,),
            "values": (
                [
                    {
                        str: (
                            bool,
                            date,
                            datetime,
                            dict,
                            float,
                            int,
                            list,
                            str,
                            UUID,
                            none_type,
                        )
                    }
                ],
            ),
        }

    attribute_map = {
        "conflict_mode": "conflict_mode",
        "values": "values",
    }

    def __init__(
        self_,
        values: List[Dict[str, Any]],
        conflict_mode: Union[DatastoreItemConflictMode, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``BulkPutAppsDatastoreItemsRequestDataAttributes`` object.

        :param conflict_mode: The definition of ``DatastoreItemConflictMode`` object.
        :type conflict_mode: DatastoreItemConflictMode, optional

        :param values: The ``attributes`` ``values``.
        :type values: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}]
        """
        if conflict_mode is not unset:
            kwargs["conflict_mode"] = conflict_mode
        super().__init__(kwargs)

        self_.values = values
