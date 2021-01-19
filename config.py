#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "4699d609-1034-436e-a9eb-bbfb0928d8ea")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "edbdbac0-a029-440c-bda5-e8956f4583f8")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://kien-duong.azurewebsites.net/qnamaker")
