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
    from datadog_api_client.v2.model.error_links import ErrorLinks
    from datadog_api_client.v2.model.error_source import ErrorSource


class WidgetErrorInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.error_links import ErrorLinks
        from datadog_api_client.v2.model.error_source import ErrorSource

        return {
            "code": (str, none_type),
            "detail": (str, none_type),
            "id": (str, none_type),
            "links": (ErrorLinks,),
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
            "source": (ErrorSource,),
            "status": (str, none_type),
            "title": (str, none_type),
        }

    attribute_map = {
        "code": "code",
        "detail": "detail",
        "id": "id",
        "links": "links",
        "meta": "meta",
        "source": "source",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        code: Union[str, none_type, UnsetType] = unset,
        detail: Union[str, none_type, UnsetType] = unset,
        id: Union[str, none_type, UnsetType] = unset,
        links: Union[ErrorLinks, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        source: Union[ErrorSource, UnsetType] = unset,
        status: Union[str, none_type, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API "error object".
        See: https://jsonapi.org/format/1.0/#error-objects

        :param code:
        :type code: str, none_type, optional

        :param detail:
        :type detail: str, none_type, optional

        :param id:
        :type id: str, none_type, optional

        :param links:
        :type links: ErrorLinks, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param source: An object containing references to the primary source of the error.
            See: https://jsonapi.org/format/#error-objects
        :type source: ErrorSource, optional

        :param status:
        :type status: str, none_type, optional

        :param title:
        :type title: str, none_type, optional
        """
        if code is not unset:
            kwargs["code"] = code
        if detail is not unset:
            kwargs["detail"] = detail
        if id is not unset:
            kwargs["id"] = id
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        if source is not unset:
            kwargs["source"] = source
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
