# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel


class LLMObsUpdatePromptVersionDataAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel

        return {
            "description": (str,),
            "env_ids": ([str],),
            "labels": ([LLMObsPromptVersionLabel],),
        }

    attribute_map = {
        "description": "description",
        "env_ids": "env_ids",
        "labels": "labels",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        env_ids: Union[List[str], UnsetType] = unset,
        labels: Union[List[LLMObsPromptVersionLabel], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an LLM Observability prompt version. At least one of ``description`` , ``labels`` , or ``env_ids`` must be provided; all three attributes are optional individually.

        :param description: Optional new description for this version.
        :type description: str, optional

        :param env_ids: Optional feature-flag environment UUIDs the service attempts to enable and configure to use this version as their default.
        :type env_ids: [str], optional

        :param labels: Optional new labels for this version. Do not use this attribute for new integrations. **Deprecated**.
        :type labels: [LLMObsPromptVersionLabel], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if env_ids is not unset:
            kwargs["env_ids"] = env_ids
        if labels is not unset:
            kwargs["labels"] = labels
        super().__init__(kwargs)
