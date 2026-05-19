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
    from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_meta_page import (
        LLMObsExperimentationSimpleSearchMetaPage,
    )


class LLMObsExperimentationSimpleSearchMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_meta_page import (
            LLMObsExperimentationSimpleSearchMetaPage,
        )

        return {
            "page": (LLMObsExperimentationSimpleSearchMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[LLMObsExperimentationSimpleSearchMetaPage, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for a simple search response.

        :param page: Page metadata.
        :type page: LLMObsExperimentationSimpleSearchMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
