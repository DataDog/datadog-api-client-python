# flake8: noqa

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


__version__ = "0.1.0"

# import ApiClient
from datadog_api_client.v2.api_client import ApiClient

# import Configuration
from datadog_api_client.v2.configuration import Configuration

# import exceptions
from datadog_api_client.v2.exceptions import OpenApiException
from datadog_api_client.v2.exceptions import ApiAttributeError
from datadog_api_client.v2.exceptions import ApiTypeError
from datadog_api_client.v2.exceptions import ApiValueError
from datadog_api_client.v2.exceptions import ApiKeyError
from datadog_api_client.v2.exceptions import ApiException
