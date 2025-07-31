# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.statsig_credentials import StatsigCredentials
    from datadog_api_client.v2.model.statsig_integration_type import StatsigIntegrationType
    from datadog_api_client.v2.model.statsig_api_key import StatsigAPIKey


class StatsigIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statsig_credentials import StatsigCredentials
        from datadog_api_client.v2.model.statsig_integration_type import StatsigIntegrationType

        return {
            "credentials": (StatsigCredentials,),
            "type": (StatsigIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[StatsigCredentials, StatsigAPIKey], type: StatsigIntegrationType, **kwargs):
        """
        The definition of the ``StatsigIntegration`` object.

        :param credentials: The definition of the ``StatsigCredentials`` object.
        :type credentials: StatsigCredentials

        :param type: The definition of the ``StatsigIntegrationType`` object.
        :type type: StatsigIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
