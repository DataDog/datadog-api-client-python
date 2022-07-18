# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringTriageUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "id": (int,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "id": "id",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(self, uuid, *args, **kwargs):
        """
        Object representing a given user entity.

        :param handle: The handle for this user account.
        :type handle: str, optional

        :param id: Numerical ID assigned by Datadog to this user account.
        :type id: int, optional

        :param name: The name for this user account.
        :type name: str, optional

        :param uuid: UUID assigned by Datadog to this user account.
        :type uuid: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.uuid = uuid

    @classmethod
    def _from_openapi_data(cls, uuid, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringTriageUser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.uuid = uuid
        return self
