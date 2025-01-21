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
    from datadog_api_client.v2.model.aws_credentials_update import AWSCredentialsUpdate
    from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
    from datadog_api_client.v2.model.aws_assume_role_update import AWSAssumeRoleUpdate


class AWSIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_credentials_update import AWSCredentialsUpdate
        from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType

        return {
            "credentials": (AWSCredentialsUpdate,),
            "type": (AWSIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSIntegrationType,
        credentials: Union[AWSCredentialsUpdate, AWSAssumeRoleUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AWSIntegrationUpdate`` object.

        :param credentials: The definition of ``AWSCredentialsUpdate`` object.
        :type credentials: AWSCredentialsUpdate, optional

        :param type: The definition of ``AWSIntegrationType`` object.
        :type type: AWSIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
