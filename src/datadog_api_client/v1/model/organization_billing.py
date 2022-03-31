# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationBilling(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "type": (str,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        A JSON array of billing type.

        :param type: The type of billing. Only `parent_billing` is supported.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OrganizationBilling, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
