# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

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


class LinkObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "describedby": (str, none_type),
            "href": (str,),
            "hreflang": ([str], none_type),
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
            "rel": (str, none_type),
            "title": (str, none_type),
            "type": (str, none_type),
        }

    attribute_map = {
        "describedby": "describedby",
        "href": "href",
        "hreflang": "hreflang",
        "meta": "meta",
        "rel": "rel",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        href: str,
        describedby: Union[str, none_type, UnsetType] = unset,
        hreflang: Union[List[str], none_type, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        rel: Union[str, none_type, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        type: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API "link object"
        See: https://jsonapi.org/format/#auto-id--link-objects

        :param describedby:
        :type describedby: str, none_type, optional

        :param href:
        :type href: str

        :param hreflang:
        :type hreflang: [str], none_type, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param rel:
        :type rel: str, none_type, optional

        :param title:
        :type title: str, none_type, optional

        :param type:
        :type type: str, none_type, optional
        """
        if describedby is not unset:
            kwargs["describedby"] = describedby
        if hreflang is not unset:
            kwargs["hreflang"] = hreflang
        if meta is not unset:
            kwargs["meta"] = meta
        if rel is not unset:
            kwargs["rel"] = rel
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.href = href
