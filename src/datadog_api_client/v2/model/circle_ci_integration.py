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
    from datadog_api_client.v2.model.circle_ci_credentials import CircleCICredentials
    from datadog_api_client.v2.model.circle_ci_integration_type import CircleCIIntegrationType
    from datadog_api_client.v2.model.circle_ciapi_key import CircleCIAPIKey


class CircleCIIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.circle_ci_credentials import CircleCICredentials
        from datadog_api_client.v2.model.circle_ci_integration_type import CircleCIIntegrationType

        return {
            "credentials": (CircleCICredentials,),
            "type": (CircleCIIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, credentials: Union[CircleCICredentials, CircleCIAPIKey], type: CircleCIIntegrationType, **kwargs
    ):
        """
        The definition of the ``CircleCIIntegration`` object.

        :param credentials: The definition of the ``CircleCICredentials`` object.
        :type credentials: CircleCICredentials

        :param type: The definition of the ``CircleCIIntegrationType`` object.
        :type type: CircleCIIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
