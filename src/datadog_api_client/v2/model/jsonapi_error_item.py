# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.jsonapi_error_item_source import JSONAPIErrorItemSource


class JSONAPIErrorItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jsonapi_error_item_source import JSONAPIErrorItemSource

        return {
            "detail": (str,),
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
            ),
            "source": (JSONAPIErrorItemSource,),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "detail": "detail",
        "meta": "meta",
        "source": "source",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        detail: Union[str, UnsetType] = unset,
        meta: Union[Dict[str, Any], UnsetType] = unset,
        source: Union[JSONAPIErrorItemSource, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        API error response body

        :param detail: A human-readable explanation specific to this occurrence of the error.
        :type detail: str, optional

        :param meta: Non-standard meta-information about the error
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param source: References to the source of the error.
        :type source: JSONAPIErrorItemSource, optional

        :param status: Status code of the response.
        :type status: str, optional

        :param title: Short human-readable summary of the error.
        :type title: str, optional
        """
        if detail is not unset:
            kwargs["detail"] = detail
        if meta is not unset:
            kwargs["meta"] = meta
        if source is not unset:
            kwargs["source"] = source
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
