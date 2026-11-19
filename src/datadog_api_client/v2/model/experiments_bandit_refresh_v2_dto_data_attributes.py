# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ExperimentsBanditRefreshV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bandit_id": (UUID,),
        }

    attribute_map = {
        "bandit_id": "bandit_id",
    }

    def __init__(self_, bandit_id: UUID, **kwargs):
        """
        The bandit being refreshed.

        :param bandit_id: The ID of the bandit being refreshed.
        :type bandit_id: UUID
        """
        super().__init__(kwargs)

        self_.bandit_id = bandit_id
