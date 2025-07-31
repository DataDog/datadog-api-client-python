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
    from datadog_api_client.v2.model.statsig_credentials_update import StatsigCredentialsUpdate
    from datadog_api_client.v2.model.statsig_integration_type import StatsigIntegrationType
    from datadog_api_client.v2.model.statsig_api_key_update import StatsigAPIKeyUpdate


class StatsigIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statsig_credentials_update import StatsigCredentialsUpdate
        from datadog_api_client.v2.model.statsig_integration_type import StatsigIntegrationType

        return {
            "credentials": (StatsigCredentialsUpdate,),
            "type": (StatsigIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: StatsigIntegrationType,
        credentials: Union[StatsigCredentialsUpdate, StatsigAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``StatsigIntegrationUpdate`` object.

        :param credentials: The definition of the ``StatsigCredentialsUpdate`` object.
        :type credentials: StatsigCredentialsUpdate, optional

        :param type: The definition of the ``StatsigIntegrationType`` object.
        :type type: StatsigIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
