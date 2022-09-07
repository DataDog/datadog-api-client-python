# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMApplicationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application import RUMApplication

        return {
            "data": ([RUMApplication],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        RUM applications response.

        :param data: RUM applications array response.
        :type data: [RUMApplication], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
