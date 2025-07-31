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
    from datadog_api_client.v2.model.clickup_credentials_update import ClickupCredentialsUpdate
    from datadog_api_client.v2.model.clickup_integration_type import ClickupIntegrationType
    from datadog_api_client.v2.model.clickup_api_key_update import ClickupAPIKeyUpdate


class ClickupIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.clickup_credentials_update import ClickupCredentialsUpdate
        from datadog_api_client.v2.model.clickup_integration_type import ClickupIntegrationType

        return {
            "credentials": (ClickupCredentialsUpdate,),
            "type": (ClickupIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: ClickupIntegrationType,
        credentials: Union[ClickupCredentialsUpdate, ClickupAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ClickupIntegrationUpdate`` object.

        :param credentials: The definition of the ``ClickupCredentialsUpdate`` object.
        :type credentials: ClickupCredentialsUpdate, optional

        :param type: The definition of the ``ClickupIntegrationType`` object.
        :type type: ClickupIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
