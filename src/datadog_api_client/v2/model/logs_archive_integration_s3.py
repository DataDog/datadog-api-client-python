# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveIntegrationS3(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "role_name": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "role_name": "role_name",
    }

    def __init__(self, account_id, role_name, *args, **kwargs):
        """
        The S3 Archive's integration destination.

        :param account_id: The account ID for the integration.
        :type account_id: str

        :param role_name: The path of the integration.
        :type role_name: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.role_name = role_name

    @classmethod
    def _from_openapi_data(cls, account_id, role_name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveIntegrationS3, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.role_name = role_name
        return self
