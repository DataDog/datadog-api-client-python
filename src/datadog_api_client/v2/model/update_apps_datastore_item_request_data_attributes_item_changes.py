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
            "ops_set": (
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
        "ops_set": "ops_set",
    }

    def __init__(self_, ops_set: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        Changes to apply to a datastore item using set operations.

        :param ops_set: Set operation that contains key-value pairs to set on the datastore item.
        :type ops_set: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if ops_set is not unset:
            kwargs["ops_set"] = ops_set
        super().__init__(kwargs)
