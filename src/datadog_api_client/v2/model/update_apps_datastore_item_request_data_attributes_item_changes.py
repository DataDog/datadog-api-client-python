# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

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


class UpdateAppsDatastoreItemRequestDataAttributesItemChanges(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_set": (
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
                },
            ),
        }

    attribute_map = {
        "_set": "$set",
    }

    def __init__(self_, _set: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        The definition of ``UpdateAppsDatastoreItemRequestDataAttributesItemChanges`` object.

        :param _set: The ``item_changes`` ``$set``.
        :type _set: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if _set is not unset:
            kwargs["_set"] = _set
        super().__init__(kwargs)
