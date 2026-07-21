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
    from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate
    from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage


class LLMObsPromptVersionDataAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_dataset import LLMObsPromptDataset
        from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate

        return {
            "author": (str,),
            "created_at": (datetime,),
            "datasets": ([LLMObsPromptDataset],),
            "description": (str,),
            "labels": ([str],),
            "last_seen_at": (datetime,),
            "ml_app": (str,),
            "ml_apps": ([str],),
            "prompt_id": (str,),
            "prompt_uuid": (str,),
            "tags": ([str],),
            "template": (LLMObsPromptTemplate,),
            "user_version": (str,),
            "version": (int,),
            "version_created_at": (datetime,),
        }

    attribute_map = {
        "author": "author",
        "created_at": "created_at",
        "datasets": "datasets",
        "description": "description",
        "labels": "labels",
        "last_seen_at": "last_seen_at",
        "ml_app": "ml_app",
        "ml_apps": "ml_apps",
        "prompt_id": "prompt_id",
        "prompt_uuid": "prompt_uuid",
        "tags": "tags",
        "template": "template",
        "user_version": "user_version",
        "version": "version",
        "version_created_at": "version_created_at",
    }

    def __init__(
        self_,
        prompt_id: str,
        prompt_uuid: str,
        template: Union[LLMObsPromptTemplate, str, List[LLMObsPromptChatMessage]],
        version: int,
        author: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        datasets: Union[List[LLMObsPromptDataset], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        labels: Union[List[str], UnsetType] = unset,
        last_seen_at: Union[datetime, UnsetType] = unset,
        ml_app: Union[str, UnsetType] = unset,
        ml_apps: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        user_version: Union[str, UnsetType] = unset,
        version_created_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a specific version of an LLM Observability prompt.

        :param author: UUID of the user who authored this version.
        :type author: str, optional

        :param created_at: Timestamp stored on this prompt version.
        :type created_at: datetime, optional

        :param datasets: Datasets observed in runs associated with this prompt version.
        :type datasets: [LLMObsPromptDataset], optional

        :param description: Description of this version.
        :type description: str, optional

        :param labels: Labels attached to this version (for example ``development`` , ``staging`` , ``production`` ). **Deprecated**.
        :type labels: [str], optional

        :param last_seen_at: Timestamp of the most recent observed run of this prompt version.
        :type last_seen_at: datetime, optional

        :param ml_app: The ML application this prompt is associated with.
        :type ml_app: str, optional

        :param ml_apps: ML applications observed running this prompt version.
        :type ml_apps: [str], optional

        :param prompt_id: Customer-provided identifier of the parent prompt.
        :type prompt_id: str

        :param prompt_uuid: Unique identifier of the parent prompt.
        :type prompt_uuid: str

        :param tags: Tags observed on runs of this prompt version.
        :type tags: [str], optional

        :param template: A text template or a list of chat messages.
        :type template: LLMObsPromptTemplate

        :param user_version: User-supplied identifier for this version.
        :type user_version: str, optional

        :param version: Sequential version number.
        :type version: int

        :param version_created_at: Timestamp when this version was created.
        :type version_created_at: datetime, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if datasets is not unset:
            kwargs["datasets"] = datasets
        if description is not unset:
            kwargs["description"] = description
        if labels is not unset:
            kwargs["labels"] = labels
        if last_seen_at is not unset:
            kwargs["last_seen_at"] = last_seen_at
        if ml_app is not unset:
            kwargs["ml_app"] = ml_app
        if ml_apps is not unset:
            kwargs["ml_apps"] = ml_apps
        if tags is not unset:
            kwargs["tags"] = tags
        if user_version is not unset:
            kwargs["user_version"] = user_version
        if version_created_at is not unset:
            kwargs["version_created_at"] = version_created_at
        super().__init__(kwargs)

        self_.prompt_id = prompt_id
        self_.prompt_uuid = prompt_uuid
        self_.template = template
        self_.version = version
