# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.usage_data_object import UsageDataObject

    globals()["UsageDataObject"] = UsageDataObject


class UsageLambdaTracedInvocationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": ([UsageDataObject],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        Lambda Traced Invocations usage response.

        :param data: Response containing Lambda Traced Invocations usage.
        :type data: [UsageDataObject], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageLambdaTracedInvocationsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
