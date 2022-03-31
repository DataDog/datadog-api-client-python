# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class SyntheticsDeletedTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_at": (datetime,),
            "public_id": (str,),
        }

    attribute_map = {
        "deleted_at": "deleted_at",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing a deleted Synthetic test ID with the associated
        deletion timestamp.

        :param deleted_at: Deletion timestamp of the Synthetic test ID.
        :type deleted_at: datetime, optional

        :param public_id: The Synthetic test ID deleted.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsDeletedTest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
