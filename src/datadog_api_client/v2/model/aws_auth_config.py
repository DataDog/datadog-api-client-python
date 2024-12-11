# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class AWSAuthConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        AWS Authentication config.

        :param access_key_id: AWS Access Key ID.
        :type access_key_id: str

        :param secret_access_key: AWS Secret Access Key.
        :type secret_access_key: str, optional

        :param external_id: AWS IAM External ID for associated role.
        :type external_id: str, optional

        :param role_name: AWS IAM Role name.
        :type role_name: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.aws_auth_config_keys import AWSAuthConfigKeys
        from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole

        return {
            "oneOf": [
                AWSAuthConfigKeys,
                AWSAuthConfigRole,
            ],
        }
