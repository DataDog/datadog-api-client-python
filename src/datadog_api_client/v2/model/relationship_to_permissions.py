# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData

    globals()["RelationshipToPermissionData"] = RelationshipToPermissionData


class RelationshipToPermissions(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": ([RelationshipToPermissionData],),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Relationship to multiple permissions objects.

        :param data: Relationships to permission objects.
        :type data: [RelationshipToPermissionData], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToPermissions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
