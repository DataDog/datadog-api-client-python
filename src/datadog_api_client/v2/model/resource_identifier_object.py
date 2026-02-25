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


class ResourceIdentifierObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "meta": (
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
                none_type,
            ),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(self_, id: str, type: str, meta: Union[Dict[str, Any], none_type, UnsetType] = unset, **kwargs):
        """
        A JSON:API "resource identifier object"
        See: https://jsonapi.org/format/#document-resource-identifier-objects

        :param id:
        :type id: str

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param type:
        :type type: str
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
