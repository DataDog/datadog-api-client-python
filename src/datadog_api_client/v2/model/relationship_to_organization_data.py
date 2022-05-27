# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RelationshipToOrganizationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.organizations_type import OrganizationsType

        return {
            "id": (str,),
            "type": (OrganizationsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        Relationship to organization object.

        :param id: ID of the organization.
        :type id: str

        :param type: Organizations resource type.
        :type type: OrganizationsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToOrganizationData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
