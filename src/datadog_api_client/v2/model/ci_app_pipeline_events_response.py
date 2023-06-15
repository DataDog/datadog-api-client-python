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


from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute
from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute

if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_pipeline_event import CIAppPipelineEvent
    from datadog_api_client.v2.model.ci_app_response_links import CIAppResponseLinks
    from datadog_api_client.v2.model.ci_app_response_metadata_with_pagination import CIAppResponseMetadataWithPagination


@dataclass
class CIAppPipelineEventsResponseJSON:
    id: str
    attributes: Union[Dict[str, Any], UnsetType] = unset
    service: Union[str, UnsetType] = unset
    tags: Union[TagsEventAttribute, UnsetType] = unset
    timestamp: Union[datetime, UnsetType] = unset


class CIAppPipelineEventsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_pipeline_event import CIAppPipelineEvent
        from datadog_api_client.v2.model.ci_app_response_links import CIAppResponseLinks
        from datadog_api_client.v2.model.ci_app_response_metadata_with_pagination import (
            CIAppResponseMetadataWithPagination,
        )

        return {
            "data": ([CIAppPipelineEvent],),
            "links": (CIAppResponseLinks,),
            "meta": (CIAppResponseMetadataWithPagination,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }
    json_api_model = CIAppPipelineEventsResponseJSON

    def __init__(
        self_,
        data: Union[List[CIAppPipelineEvent], UnsetType] = unset,
        links: Union[CIAppResponseLinks, UnsetType] = unset,
        meta: Union[CIAppResponseMetadataWithPagination, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object with all pipeline events matching the request and pagination information.

        :param data: Array of events matching the request.
        :type data: [CIAppPipelineEvent], optional

        :param links: Links attributes.
        :type links: CIAppResponseLinks, optional

        :param meta: The metadata associated with a request.
        :type meta: CIAppResponseMetadataWithPagination, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
