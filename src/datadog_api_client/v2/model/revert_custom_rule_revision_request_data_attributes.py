# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RevertCustomRuleRevisionRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "current_revision_id": (str,),
            "revert_to_revision_id": (str,),
        }

    attribute_map = {
        "current_revision_id": "current_revision_id",
        "revert_to_revision_id": "revert_to_revision_id",
    }

    def __init__(
        self_,
        current_revision_id: Union[str, UnsetType] = unset,
        revert_to_revision_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param current_revision_id: Current revision ID
        :type current_revision_id: str, optional

        :param revert_to_revision_id: Target revision ID to revert to
        :type revert_to_revision_id: str, optional
        """
        if current_revision_id is not unset:
            kwargs["current_revision_id"] = current_revision_id
        if revert_to_revision_id is not unset:
            kwargs["revert_to_revision_id"] = revert_to_revision_id
        super().__init__(kwargs)
