# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experimentation_content_preview import LLMObsExperimentationContentPreview
    from datadog_api_client.v2.model.llm_obs_experimentation_filter import LLMObsExperimentationFilter
    from datadog_api_client.v2.model.llm_obs_experimentation_include import LLMObsExperimentationInclude
    from datadog_api_client.v2.model.llm_obs_experimentation_cursor_page import LLMObsExperimentationCursorPage


class LLMObsExperimentationSearchDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_content_preview import (
            LLMObsExperimentationContentPreview,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_filter import LLMObsExperimentationFilter
        from datadog_api_client.v2.model.llm_obs_experimentation_include import LLMObsExperimentationInclude
        from datadog_api_client.v2.model.llm_obs_experimentation_cursor_page import LLMObsExperimentationCursorPage

        return {
            "content_preview": (LLMObsExperimentationContentPreview,),
            "filter": (LLMObsExperimentationFilter,),
            "include": (LLMObsExperimentationInclude,),
            "page": (LLMObsExperimentationCursorPage,),
        }

    attribute_map = {
        "content_preview": "content_preview",
        "filter": "filter",
        "include": "include",
        "page": "page",
    }

    def __init__(
        self_,
        filter: LLMObsExperimentationFilter,
        content_preview: Union[LLMObsExperimentationContentPreview, UnsetType] = unset,
        include: Union[LLMObsExperimentationInclude, UnsetType] = unset,
        page: Union[LLMObsExperimentationCursorPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an experimentation search request.

        :param content_preview: Options to control content preview truncation.
        :type content_preview: LLMObsExperimentationContentPreview, optional

        :param filter: Filter criteria for an experimentation search request.
        :type filter: LLMObsExperimentationFilter

        :param include: Additional data to include in the response.
        :type include: LLMObsExperimentationInclude, optional

        :param page: Cursor-based pagination parameters.
        :type page: LLMObsExperimentationCursorPage, optional
        """
        if content_preview is not unset:
            kwargs["content_preview"] = content_preview
        if include is not unset:
            kwargs["include"] = include
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)

        self_.filter = filter
