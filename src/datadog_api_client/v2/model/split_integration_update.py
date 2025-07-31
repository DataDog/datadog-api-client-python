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
    from datadog_api_client.v2.model.split_credentials_update import SplitCredentialsUpdate
    from datadog_api_client.v2.model.split_integration_type import SplitIntegrationType
    from datadog_api_client.v2.model.split_api_key_update import SplitAPIKeyUpdate


class SplitIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.split_credentials_update import SplitCredentialsUpdate
        from datadog_api_client.v2.model.split_integration_type import SplitIntegrationType

        return {
            "credentials": (SplitCredentialsUpdate,),
            "type": (SplitIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: SplitIntegrationType,
        credentials: Union[SplitCredentialsUpdate, SplitAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``SplitIntegrationUpdate`` object.

        :param credentials: The definition of the ``SplitCredentialsUpdate`` object.
        :type credentials: SplitCredentialsUpdate, optional

        :param type: The definition of the ``SplitIntegrationType`` object.
        :type type: SplitIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
