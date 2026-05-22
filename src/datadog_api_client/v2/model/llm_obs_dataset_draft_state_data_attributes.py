# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_dataset_draft_state_user import LLMObsDatasetDraftStateUser


class LLMObsDatasetDraftStateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_draft_state_user import LLMObsDatasetDraftStateUser

        return {
            "drafting_since": (datetime,),
            "user": (LLMObsDatasetDraftStateUser,),
        }

    attribute_map = {
        "drafting_since": "drafting_since",
        "user": "user",
    }

    def __init__(self_, drafting_since: datetime, user: LLMObsDatasetDraftStateUser, **kwargs):
        """
        Attributes of an LLM Observability dataset draft state.

        :param drafting_since: Timestamp when the dataset draft session started.
        :type drafting_since: datetime

        :param user: User information associated with a dataset draft state.
        :type user: LLMObsDatasetDraftStateUser
        """
        super().__init__(kwargs)

        self_.drafting_since = drafting_since
        self_.user = user
