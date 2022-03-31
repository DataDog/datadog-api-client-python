# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSAccountDeleteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "access_key_id": (str,),
            "account_id": (str,),
            "role_name": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
        "account_id": "account_id",
        "role_name": "role_name",
    }

    def __init__(self, *args, **kwargs):
        """
        List of AWS accounts to delete.

        :param access_key_id: Your AWS access key ID. Only required if your AWS account is a GovCloud or China account.
        :type access_key_id: str, optional

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str, optional

        :param role_name: Your Datadog role delegation name.
        :type role_name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSAccountDeleteRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
