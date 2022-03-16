# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class RoleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
            "user_count": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
        "user_count": "user_count",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
        "user_count",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of the role.

        :param created_at: Creation time of the role.
        :type created_at: datetime, optional

        :param modified_at: Time of last role modification.
        :type modified_at: datetime, optional

        :param name: The name of the role. The name is neither unique nor a stable identifier of the role.
        :type name: str, optional

        :param user_count: Number of users with that role.
        :type user_count: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
