# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.error_errors_items_links import ErrorErrorsItemsLinks
    from datadog_api_client.v2.model.error_errors_items_source import ErrorErrorsItemsSource


class ErrorErrorsItems(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.error_errors_items_links import ErrorErrorsItemsLinks
        from datadog_api_client.v2.model.error_errors_items_source import ErrorErrorsItemsSource

        return {
            "code": (str,),
            "detail": (str,),
            "id": (str,),
            "links": (ErrorErrorsItemsLinks,),
            "meta": (
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
            ),
            "source": (ErrorErrorsItemsSource,),
            "status": (int, none_type),
            "title": (str,),
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
        code: Union[str, UnsetType] = unset,
        detail: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        links: Union[ErrorErrorsItemsLinks, none_type, UnsetType] = unset,
        meta: Union[Any, UnsetType] = unset,
        source: Union[ErrorErrorsItemsSource, none_type, UnsetType] = unset,
        status: Union[int, none_type, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ErrorErrorsItems`` object.

        :param code: The ``items`` ``code``.
        :type code: str, optional

        :param detail: The ``items`` ``detail``.
        :type detail: str, optional

        :param id: The ``items`` ``id``.
        :type id: str, optional

        :param links: The definition of ``ErrorErrorsItemsLinks`` object.
        :type links: ErrorErrorsItemsLinks, none_type, optional

        :param meta: The ``items`` ``meta``.
        :type meta: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param source: The definition of ``ErrorErrorsItemsSource`` object.
        :type source: ErrorErrorsItemsSource, none_type, optional

        :param status: The ``items`` ``status``.
        :type status: int, none_type, optional

        :param title: The ``items`` ``title``.
        :type title: str, optional
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
