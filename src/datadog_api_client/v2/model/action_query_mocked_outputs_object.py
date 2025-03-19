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
    from datadog_api_client.v2.model.action_query_mocked_outputs_enabled import ActionQueryMockedOutputsEnabled


class ActionQueryMockedOutputsObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_query_mocked_outputs_enabled import ActionQueryMockedOutputsEnabled

        return {
            "enabled": (ActionQueryMockedOutputsEnabled,),
            "outputs": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "outputs": "outputs",
    }

    def __init__(
        self_,
        enabled: Union[ActionQueryMockedOutputsEnabled, bool, str],
        outputs: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The mocked outputs of the action query.

        :param enabled: Whether to enable the mocked outputs for testing.
        :type enabled: ActionQueryMockedOutputsEnabled

        :param outputs: The mocked outputs of the action query, serialized as JSON.
        :type outputs: str, optional
        """
        if outputs is not unset:
            kwargs["outputs"] = outputs
        super().__init__(kwargs)

        self_.enabled = enabled
