# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.service_account_create_data import ServiceAccountCreateData

    globals()["ServiceAccountCreateData"] = ServiceAccountCreateData


class ServiceAccountCreateRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": (ServiceAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, data, *args, **kwargs):
        """
        Create a service account.

        :param data: Object to create a service account User.
        :type data: ServiceAccountCreateData
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceAccountCreateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
