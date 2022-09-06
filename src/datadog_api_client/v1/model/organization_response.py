# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.organization import Organization

        return {
            "org": (Organization,),
        }

    attribute_map = {
        "org": "org",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response with an organization.

        :param org: Create, edit, and manage organizations.
        :type org: Organization, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
