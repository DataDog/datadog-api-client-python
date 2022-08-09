# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMApplicationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "created_at": (int,),
            "created_by_handle": (str,),
            "hash": (str,),
            "name": (str,),
            "org_id": (int,),
            "type": (str,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "hash": "hash",
        "name": "name",
        "org_id": "org_id",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self,
        application_id,
        created_at,
        created_by_handle,
        name,
        org_id,
        type,
        updated_at,
        updated_by_handle,
        *args,
        **kwargs
    ):
        """
        RUM application attributes.

        :param application_id: ID of the RUM application.
        :type application_id: str

        :param created_at: Timestamp in ms of the creation date.
        :type created_at: int

        :param created_by_handle: Handle of the creator user.
        :type created_by_handle: str

        :param hash: Client token of the RUM application.
        :type hash: str, optional

        :param name: Name of the RUM application.
        :type name: str

        :param org_id: Org ID of the RUM application.
        :type org_id: int

        :param type: Type of the RUM application.
        :type type: str

        :param updated_at: Timestamp in ms of the last update date.
        :type updated_at: int

        :param updated_by_handle: Handle of the updater user.
        :type updated_by_handle: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.application_id = application_id
        self.created_at = created_at
        self.created_by_handle = created_by_handle
        self.name = name
        self.org_id = org_id
        self.type = type
        self.updated_at = updated_at
        self.updated_by_handle = updated_by_handle

    @classmethod
    def _from_openapi_data(
        cls,
        application_id,
        created_at,
        created_by_handle,
        name,
        org_id,
        type,
        updated_at,
        updated_by_handle,
        *args,
        **kwargs
    ):
        """Helper creating a new instance from a response."""

        self = super(RUMApplicationAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.application_id = application_id
        self.created_at = created_at
        self.created_by_handle = created_by_handle
        self.name = name
        self.org_id = org_id
        self.type = type
        self.updated_at = updated_at
        self.updated_by_handle = updated_by_handle
        return self