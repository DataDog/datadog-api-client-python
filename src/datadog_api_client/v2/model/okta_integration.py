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
    from datadog_api_client.v2.model.okta_credentials import OktaCredentials
    from datadog_api_client.v2.model.okta_integration_type import OktaIntegrationType
    from datadog_api_client.v2.model.okta_api_token import OktaAPIToken


class OktaIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_credentials import OktaCredentials
        from datadog_api_client.v2.model.okta_integration_type import OktaIntegrationType

        return {
            "credentials": (OktaCredentials,),
            "type": (OktaIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[OktaCredentials, OktaAPIToken], type: OktaIntegrationType, **kwargs):
        """
        The definition of the ``OktaIntegration`` object.

        :param credentials: The definition of the ``OktaCredentials`` object.
        :type credentials: OktaCredentials

        :param type: The definition of the ``OktaIntegrationType`` object.
        :type type: OktaIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
