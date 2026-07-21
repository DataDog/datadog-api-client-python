# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_prompt_dataset import LLMObsPromptDataset
    from datadog_api_client.v2.model.llm_obs_prompt_response_source import LLMObsPromptResponseSource


class LLMObsPromptDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_dataset import LLMObsPromptDataset
        from datadog_api_client.v2.model.llm_obs_prompt_response_source import LLMObsPromptResponseSource

        return {
            "author": (str,),
            "created_at": (datetime,),
            "created_from": (str,),
            "datasets": ([LLMObsPromptDataset],),
            "description": (str,),
            "extracted_from": (str,),
            "in_registry": (bool,),
            "last_seen_at": (datetime,),
            "last_version_created_at": (datetime,),
            "ml_app": (str,),
            "ml_apps": ([str],),
            "num_versions": (int,),
            "prompt_id": (str,),
            "source": (LLMObsPromptResponseSource,),
            "tags": ([str],),
            "title": (str,),
        }

    attribute_map = {
        "author": "author",
        "created_at": "created_at",
        "created_from": "created_from",
        "datasets": "datasets",
        "description": "description",
        "extracted_from": "extracted_from",
        "in_registry": "in_registry",
        "last_seen_at": "last_seen_at",
        "last_version_created_at": "last_version_created_at",
        "ml_app": "ml_app",
        "ml_apps": "ml_apps",
        "num_versions": "num_versions",
        "prompt_id": "prompt_id",
        "source": "source",
        "tags": "tags",
        "title": "title",
    }

    def __init__(
        self_,
        created_from: str,
        in_registry: bool,
        num_versions: int,
        prompt_id: str,
        source: LLMObsPromptResponseSource,
        author: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        datasets: Union[List[LLMObsPromptDataset], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        extracted_from: Union[str, UnsetType] = unset,
        last_seen_at: Union[datetime, UnsetType] = unset,
        last_version_created_at: Union[datetime, UnsetType] = unset,
        ml_app: Union[str, UnsetType] = unset,
        ml_apps: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability prompt registry entry.

        :param author: UUID of the user who authored the prompt.
        :type author: str, optional

        :param created_at: Timestamp when the prompt was created.
        :type created_at: datetime, optional

        :param created_from: Source that created the prompt, such as ``ui-registry`` , ``sdk-registry`` , or ``sdk-instrumentation``.
        :type created_from: str

        :param datasets: Datasets observed in runs associated with this prompt.
        :type datasets: [LLMObsPromptDataset], optional

        :param description: Description of the prompt.
        :type description: str, optional

        :param extracted_from: Source prompt from which this prompt was extracted, when applicable.
        :type extracted_from: str, optional

        :param in_registry: Whether the prompt is a registry entry (as opposed to a code-discovered prompt).
        :type in_registry: bool

        :param last_seen_at: Timestamp of the most recent observed run of this prompt.
        :type last_seen_at: datetime, optional

        :param last_version_created_at: Timestamp when the most recent version of the prompt was created.
        :type last_version_created_at: datetime, optional

        :param ml_app: The ML application this prompt is associated with.
        :type ml_app: str, optional

        :param ml_apps: ML applications observed running this prompt.
        :type ml_apps: [str], optional

        :param num_versions: Number of versions of the prompt.
        :type num_versions: int

        :param prompt_id: Customer-provided identifier of the prompt.
        :type prompt_id: str

        :param source: Whether the prompt was created from the registry or discovered from observed LLM calls.
        :type source: LLMObsPromptResponseSource

        :param tags: Tags observed on runs of this prompt.
        :type tags: [str], optional

        :param title: Title of the prompt.
        :type title: str, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if datasets is not unset:
            kwargs["datasets"] = datasets
        if description is not unset:
            kwargs["description"] = description
        if extracted_from is not unset:
            kwargs["extracted_from"] = extracted_from
        if last_seen_at is not unset:
            kwargs["last_seen_at"] = last_seen_at
        if last_version_created_at is not unset:
            kwargs["last_version_created_at"] = last_version_created_at
        if ml_app is not unset:
            kwargs["ml_app"] = ml_app
        if ml_apps is not unset:
            kwargs["ml_apps"] = ml_apps
        if tags is not unset:
            kwargs["tags"] = tags
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.created_from = created_from
        self_.in_registry = in_registry
        self_.num_versions = num_versions
        self_.prompt_id = prompt_id
        self_.source = source
