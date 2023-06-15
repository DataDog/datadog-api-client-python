# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.log import Log
    from datadog_api_client.v2.model.logs_list_response_links import LogsListResponseLinks
    from datadog_api_client.v2.model.logs_response_metadata import LogsResponseMetadata


@dataclass
class LogsListResponseJSON:
    id: str
    attributes: Union[Dict[str, Any], UnsetType] = unset
    host: Union[str, UnsetType] = unset
    message: Union[str, UnsetType] = unset
    service: Union[str, UnsetType] = unset
    status: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset
    timestamp: Union[datetime, UnsetType] = unset


class LogsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.log import Log
        from datadog_api_client.v2.model.logs_list_response_links import LogsListResponseLinks
        from datadog_api_client.v2.model.logs_response_metadata import LogsResponseMetadata

        return {
            "data": ([Log],),
            "links": (LogsListResponseLinks,),
            "meta": (LogsResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }
    json_api_model = LogsListResponseJSON

    def __init__(
        self_,
        data: Union[List[Log], UnsetType] = unset,
        links: Union[LogsListResponseLinks, UnsetType] = unset,
        meta: Union[LogsResponseMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object with all logs matching the request and pagination information.

        :param data: Array of logs matching the request.
        :type data: [Log], optional

        :param links: Links attributes.
        :type links: LogsListResponseLinks, optional

        :param meta: The metadata associated with a request
        :type meta: LogsResponseMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
