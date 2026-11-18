# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringAWSIdentityCenterAWSAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_config_id": (str,),
            "account_id": (str,),
            "account_name": (str,),
            "collecting_users": (bool,),
            "resource_collection_enabled": (bool,),
        }

    attribute_map = {
        "account_config_id": "account_config_id",
        "account_id": "account_id",
        "account_name": "account_name",
        "collecting_users": "collecting_users",
        "resource_collection_enabled": "resource_collection_enabled",
    }

    def __init__(
        self_,
        account_config_id: str,
        account_id: str,
        account_name: str,
        collecting_users: bool,
        resource_collection_enabled: bool,
        **kwargs,
    ):
        """
        An integrated AWS account the AWS IAM Identity Center integration reads users from.

        :param account_config_id: The ID of the AWS account integration configuration.
        :type account_config_id: str

        :param account_id: The AWS account ID.
        :type account_id: str

        :param account_name: The name of the AWS account integration.
        :type account_name: str

        :param collecting_users: Whether AWS IAM Identity Center users were collected from this AWS account.
        :type collecting_users: bool

        :param resource_collection_enabled: Whether resource collection is enabled for this AWS account.
        :type resource_collection_enabled: bool
        """
        super().__init__(kwargs)

        self_.account_config_id = account_config_id
        self_.account_id = account_id
        self_.account_name = account_name
        self_.collecting_users = collecting_users
        self_.resource_collection_enabled = resource_collection_enabled
